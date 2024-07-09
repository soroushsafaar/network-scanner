from scapy.all import ARP, Ether, srp, IP, TCP, sr1
import socket
import json
import argparse
from concurrent.futures import ThreadPoolExecutor

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return None

def scan(ip_range):
    print(f"Scanning IP range: {ip_range}")
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]
    print(f"Scan result: {result}")

    clients = []
    for sent, received in result:
        hostname = get_hostname(received.psrc)
        clients.append({'ip': received.psrc, 'mac': received.hwsrc, 'hostname': hostname})
        print(f"Found device: IP={received.psrc}, MAC={received.hwsrc}, Hostname={hostname}")

    return clients

def scan_ports(ip):
    open_ports = []
    print(f"Scanning ports for IP: {ip}")
    for port in range(0, 65535):  # Scan ports from 20 to 1024
        pkt = sr1(IP(dst=ip)/TCP(dport=port, flags='S'), timeout=0.5, verbose=0)
        if pkt and pkt[TCP].flags == 18:  # SYN-ACK
            open_ports.append(port)
            print(f"Port {port} is open on IP {ip}")
    print(f"Open ports for IP {ip}: {open_ports}")
    return open_ports

def scan_ports_concurrent(ip):
    with ThreadPoolExecutor(max_workers=50) as executor:
        future_to_port = {executor.submit(scan_single_port, ip, port): port for port in range(20, 1025)}
        open_ports = [future.result() for future in future_to_port if future.result()]
    print(f"Open ports for IP {ip}: {open_ports}")
    return open_ports

def scan_single_port(ip, port):
    pkt = sr1(IP(dst=ip)/TCP(dport=port, flags='S'), timeout=0.5, verbose=0)
    if pkt and pkt[TCP].flags == 18:  # SYN-ACK
        return port
    return None

def save_results(clients, filename='scan_results.json'):
    with open(filename, 'w') as file:
        json.dump(clients, file, indent=4)

def parse_args():
    parser = argparse.ArgumentParser(description='Network Scanner')
    parser.add_argument('ip_range', help='IP range to scan, e.g., 192.168.1.0/24 or an external IP range')
    parser.add_argument('-o', '--output', help='Output file', default='scan_results.json')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    ip_range = args.ip_range
    output_file = args.output

    clients = scan(ip_range)
    for client in clients:
        client['open_ports'] = scan_ports_concurrent(client['ip'])
    
    save_results(clients, output_file)
    
    print("Available devices in the network:")
    print("IP" + " "*18+"MAC" + " "*18 + "Hostname" + " "*18 + "Open Ports")
    for client in clients:
        hostname = client['hostname'] if client['hostname'] else "Unknown"
        print("{:16}    {:17}    {:20}    {}".format(client['ip'], client['mac'], hostname, client['open_ports']))

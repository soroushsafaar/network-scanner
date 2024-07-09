import socket
import json
import argparse
from concurrent.futures import ThreadPoolExecutor
from scapy.all import IP, ICMP, TCP, sr1

def resolve_domain(domain):
    try:
        print(f"Resolving domain: {domain}")
        ip = socket.gethostbyname(domain)
        print(f"Resolved {domain} to {ip}")
        return ip
    except socket.gaierror as e:
        print(f"Could not resolve domain: {domain}, Error: {e}")
        return None

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return None

def ping_host(ip):
    print(f"Pinging IP: {ip}")
    pkt = sr1(IP(dst=ip)/ICMP(), timeout=2, verbose=0)
    return pkt is not None

def scan_ports(ip):
    open_ports = []
    print(f"Scanning ports for IP: {ip}")
    for port in range(20, 1025):  # Scan ports from 20 to 1024
        pkt = sr1(IP(dst=ip)/TCP(dport=port, flags='S'), timeout=0.5, verbose=0)
        if pkt and pkt[TCP].flags == 18:  # SYN-ACK
            open_ports.append(port)
            print(f"Port {port} is open on IP {ip}")
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

def scan(ip_list):
    clients = []

    for ip_or_domain in ip_list:
        ip = resolve_domain(ip_or_domain) if not ip_or_domain.replace('.', '').isdigit() else ip_or_domain
        if not ip:
            continue

        is_pinged = ping_host(ip)
        hostname = get_hostname(ip) if is_pinged else None
        open_ports = scan_ports_concurrent(ip)
        
        clients.append({'ip': ip, 'hostname': hostname, 'ping': is_pinged, 'open_ports': open_ports})
        print(f"IP={ip}, Hostname={hostname}, Ping={is_pinged}, Open Ports={open_ports}")

    return clients

def save_results(clients, filename='scan_results.json'):
    with open(filename, 'w') as file:
        json.dump(clients, file, indent=4)

def parse_args():
    parser = argparse.ArgumentParser(description='External Network Scanner')
    parser.add_argument('ip_list', help='Comma-separated list of IPs or domain names to scan, e.g., 8.8.8.8,1.1.1.1,microsoft.com')
    parser.add_argument('-o', '--output', help='Output file', default='scan_results.json')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    ip_list = args.ip_list.split(',')
    output_file = args.output

    clients = scan(ip_list)
    
    save_results(clients, output_file)
    
    print("Available devices in the network:")
    print("IP" + " "*18 + "Hostname" + " "*18 + "Ping" + " "*10 + "Open Ports")
    for client in clients:
        hostname = client['hostname'] if client['hostname'] else "Unknown"
        print("{:16}    {:20}    {:10}    {}".format(client['ip'], hostname, client['ping'], client['open_ports']))

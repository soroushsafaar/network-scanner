from scapy.all import ARP, Ether, srp
import sys

def scan(ip):
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    return clients

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python network_scanner.py <ip_range>")
        sys.exit(1)

    ip_range = sys.argv[1]
    clients = scan(ip_range)
    
    print("Available devices in the network:")
    print("IP" + " "*18+"MAC")
    for client in clients:
        print("{:16}    {}".format(client['ip'], client['mac']))

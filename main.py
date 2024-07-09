import os
import argparse

def run_internal_scan(ip_range, output_file):
    os.system(f"sudo python3 internal_scanner.py {ip_range} -o {output_file}")

def run_external_scan(ip_list, output_file):
    os.system(f"sudo python3 external_scanner.py {ip_list} -o {output_file}")

def print_welcome_message():
    print("Welcome to the Network Scanner!")
    print("This tool allows you to scan internal and external networks for active devices and open ports.")
    print("Please use this tool responsibly and ensure you have permission to scan the networks you target.")
    print("\nUsage:")
    print("1. Scan Internal Network: Scans your local network for devices.")
    print("2. Scan External Network: Scans specified external IP addresses or domain names for devices and open ports.")
    print("\nExamples:")
    print("1. Internal Scan: Enter the IP range to scan, e.g., 192.168.1.0/24")
    print("2. External Scan: Enter a comma-separated list of IPs or domain names to scan, e.g., 8.8.8.8,google.com")
    print("\n")

def main():
    parser = argparse.ArgumentParser(description='Network Scanner')
    parser.add_argument('-o', '--output', help='Output file', default='scan_results.json')
    args = parser.parse_args()

    print_welcome_message()

    print("Network Scanner")
    print("1. Scan Internal Network")
    print("2. Scan External Network")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        ip_range = input("Enter the IP range to scan (e.g., 192.168.1.0/24): ")
        run_internal_scan(ip_range, args.output)
    elif choice == '2':
        ip_list = input("Enter a comma-separated list of IPs or domain names to scan (e.g., 8.8.8.8,google.com): ")
        run_external_scan(ip_list, args.output)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

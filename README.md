Sure! Below is a detailed and informative `README.md` for your `network-scanner` project. This README will provide an overview of the project, usage instructions, and other relevant information to help users understand and use your tool effectively.

### `README.md`

```markdown
# Network Scanner

Welcome to the Network Scanner project! This tool allows you to scan internal and external networks for active devices and open ports. It is designed to be user-friendly and efficient, providing useful information about the devices on your network.

## Features

- **Internal Network Scanning:** Scan your local network for active devices.
- **External Network Scanning:** Scan specified external IP addresses or domain names for active devices and open ports.
- **Hostname Resolution:** Resolve IP addresses to hostnames where possible.
- **Ping Results:** Display whether the target IP or domain responds to ping.
- **Concurrent Port Scanning:** Fast and efficient port scanning using concurrency.

## Usage

### Prerequisites

- Python 3.x
- Scapy library (`pip install scapy`)

### Running the Tool

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/soroushsafaar/network-scanner.git
   cd network-scanner
   ```

2. **Run the `main.py` Script:**

   ```sh
   sudo python3 main.py
   ```

3. **Follow the Prompts:**

   - **Choose Scan Type:** Enter `1` to scan the internal network or `2` to scan external IPs or domains.
   - **Provide Input:**
     - For internal scans, enter the IP range (e.g., `192.168.1.0/24`).
     - For external scans, enter a comma-separated list of IPs or domains (e.g., `8.8.8.8,google.com`).
   - **View Results:** The results will be saved to `scan_results.json` by default, or you can specify a different output file.

### Examples

#### Internal Scan

```sh
Enter your choice (1 or 2): 1
Enter the IP range to scan (e.g., 192.168.1.0/24): 192.168.1.0/24
```

#### External Scan

```sh
Enter your choice (1 or 2): 2
Enter a comma-separated list of IPs or domain names to scan (e.g., 8.8.8.8,google.com): 8.8.8.8,google.com
```

## Project Structure

- `main.py`: The main script that provides a user interface for selecting scan types and running scans.
- `internal_scanner.py`: Handles internal network scanning.
- `external_scanner.py`: Handles external IP and domain scanning.
- `LICENSE`: The project license.
- `README.md`: This readme file.
- `scan_results.json`: The default output file for scan results.

## Important Notes

- **Permissions:** Ensure you have permission to scan the networks you target.
- **Usage:** Use this tool responsibly and ethically. Unauthorized network scanning can be illegal.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Scapy](https://scapy.net/): The powerful Python library used for network packet manipulation.

## Contact

For any inquiries or support, please contact [your_email@example.com].

```

### Explanation:

1. **Project Overview:** Provides a brief description of the tool and its features.
2. **Usage Instructions:** Detailed steps on how to use the tool, including cloning the repository, running the script, and following prompts.
3. **Examples:** Shows example inputs for both internal and external scans.
4. **Project Structure:** Explains the structure of the repository and the purpose of each file.
5. **Important Notes:** Emphasizes the need for permission and responsible usage.
6. **Contributing:** Encourages contributions and provides guidelines.
7. **License:** Information about the project license.
8. **Acknowledgements:** Credits to the Scapy library.
9. **Contact:** Contact information for support or inquiries.

This `README.md` should provide a comprehensive overview of your project and help users understand how to use it effectively.
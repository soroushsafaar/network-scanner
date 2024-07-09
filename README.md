```markdown
# Network Scanner

This is a simple Python-based network scanner tool that scans a given IP range to identify active devices and their details (IP and MAC addresses). This project is intended to help build experience in network engineering.

## Features

- Scan a given IP range to find active devices.
- Display the IP address and MAC address of the devices.
- Simple command-line interface for interaction.

## Prerequisites

- Python 3.9 or later
- `scapy` library

## Installation

### Setting Up the Environment

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/network-scanner.git
    cd network-scanner
    ```

2. **Install the required Python packages:**

    ```sh
    pip install scapy
    ```

### Running the Script

#### On Linux or macOS:

1. **Open Terminal.**

2. **Navigate to your project directory:**

    ```sh
    cd /path/to/network-scanner
    ```

3. **Run the script with elevated privileges:**

    ```sh
    sudo python3 main.py <ip_range>
    ```

    Replace `<ip_range>` with the actual IP range you want to scan (e.g., `192.168.1.1/24`).

#### On Windows:

1. **Open Command Prompt with Administrator Privileges:**
   - Press `Win` + `S` and type `cmd`.
   - Right-click on `Command Prompt` and select `Run as administrator`.

2. **Navigate to your project directory:**

    ```sh
    cd C:\path\to\network-scanner
    ```

3. **Run the script:**

    ```sh
    python main.py <ip_range>
    ```

    Replace `<ip_range>` with the actual IP range you want to scan (e.g., `192.168.1.1/24`).

## Usage

To run the network scanner, execute the script with the desired IP range. For example:

```sh
sudo python3 main.py 192.168.1.1/24
```

or on Windows:

```sh
python main.py 192.168.1.1/24
```

## Example Output

```
Available devices in the network:
IP                 MAC
192.168.1.1        00:11:22:33:44:55
192.168.1.2        66:77:88:99:AA:BB
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

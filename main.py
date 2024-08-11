import socket
import requests
from scapy.all import sr1, IP, TCP

# Function to scan open ports
def scan_ports(target_ip, ports):
    open_ports = []
    for port in ports:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        # Try to connect to the port
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# Function to check for outdated software versions (mock implementation)
def check_software_versions(url):
    try:
        response = requests.get(url)
        headers = response.headers

        # Check for specific headers or patterns that might indicate outdated software
        if 'X-Powered-By' in headers:
            powered_by = headers['X-Powered-By']
            if 'PHP/7.0' in powered_by:
                return "PHP 7.0 detected - might be outdated."
            # Add more checks as needed
        return "Software versions appear up-to-date or not detectable."
    except requests.RequestException as e:
        return f"Error checking software versions: {e}"

# Function to check for misconfigurations (basic HTTP check)
def check_misconfigurations(url):
    try:
        response = requests.get(url)
        # Check for common misconfigurations, like default pages or sensitive info
        if "Index of" in response.text:
            return "Directory listing is enabled."
        if "404" in response.text:
            return "Possible misconfiguration or broken link."
        return "No obvious misconfigurations detected."
    except requests.RequestException as e:
        return f"Error checking misconfigurations: {e}"

# Main function
def main():
    # Target details
    target_ip = "192.168.1.1"  # Example IP
    ports_to_scan = [22, 80, 443]  # Common ports to check
    target_url = "http://youtube.com"  # Example URL

    print("Scanning for open ports...")
    open_ports = scan_ports(target_ip, ports_to_scan)
    print(f"Open ports: {open_ports}")

    print("Checking software versions...")
    software_status = check_software_versions(target_url)
    print(f"Software status: {software_status}")

    print("Checking for misconfigurations...")
    misconfiguration_status = check_misconfigurations(target_url)
    print(f"Misconfiguration status: {misconfiguration_status}")

if __name__ == "__main__":
    main()

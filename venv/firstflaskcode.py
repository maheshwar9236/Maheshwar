import sys
import re

def is_public_ipv4(ip):
    # Check if the IP is a valid IPv4 address
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    if not pattern.match(ip):
        return False
    
    # Split the IP into its 4 octets
    octets = list(map(int, ip.split('.')))
    
    # Ensure the octets are valid
    if any(octet > 255 for octet in octets):
        return False
    
    # Check if the IP is a public IPv4 address
    if (octets[0] == 10 or
        (octets[0] == 172 and 16 <= octets[1] <= 31) or
        (octets[0] == 192 and octets[1] == 168) or
        octets[0] == 127 or  # Loopback
        octets[0] == 169 and octets[1] == 254):  # Link-local
        return False
    
    return True

def main():
    for line in sys.stdin:
        ip = line.strip()
        if is_public_ipv4(ip):
            print(ip)

if __name__ == "__main__":
    main()

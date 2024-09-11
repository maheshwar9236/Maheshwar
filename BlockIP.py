import subprocess

def block_ip_address(ip_address):
    # Construct the netsh command to block the IP address in the Windows Firewall
    netsh_cmd = f"netsh advfirewall firewall add rule name='Block IP {ip_address}' dir=in interface=any action=block remoteip={ip_address}"

    # Execute the netsh command using subprocess
    try:
        subprocess.run(netsh_cmd, shell=True, check=True)
        print(f"IP address {ip_address} successfully blocked in the Windows Firewall.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to block IP address {ip_address} in the Windows Firewall.")
        print(e)

if __name__ == "__main__":
    ip_address = input("Enter the IP address to block: ")
    block_ip_address(ip_address)
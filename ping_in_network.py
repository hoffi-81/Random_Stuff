import socket
import subprocess


# Define the network range (modify this according to your network)
network_prefix = "192.168.178."  # Example network prefix

ip_adresses_array = []

# Iterate through all possible IP addresses in the network range
for i in range(1, 255):  # Assuming /24 subnet
    ip_address = network_prefix + str(i)
    try:
        # Create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Connect to the IP address and a common port (e.g., 80)
        s.connect((ip_address, 80))
        
        # Print the IP address if connection is successful
        ip_adresses_array.append(ip_address)
        
        # Close the socket
        s.close()
    except socket.error:
        # Ignore errors for unreachable hosts
        pass
    
for ip_adress_entry in ip_adresses_array:
     ping_cmd = ['ping', '-n', '1', ip_adress_entry]  # for Windows
     result = subprocess.run(ping_cmd)
     if result.returncode == 0:
         print("{} is reachable".format(ip_adress_entry))
     else:
         print("Not reachable")

from scapy.all import *

# Set the network interface, IP range, and broadcast MAC address
interface = "eth0"
''' please check the net interface before putting this! for
my case it was ens5'''

ip_range = "10.10.X.X/24" 
'''you might have to change the ip address or you can use the '''
broadcastMac = "ff:ff:ff:ff:ff:ff"

# Create an ARP request packet
packet = Ether(dst=broadcastMac) / ARP(pdst=ip_range)

# Send the packet and wait for responses
ans, unans = srp(packet, timeout=2, iface=interface, inter=0.1)

# Print the results
for send, receive in ans:
    print(receive.sprintf(r"%Ether.src% - %ARP.psrc%"))


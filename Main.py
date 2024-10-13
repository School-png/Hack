import subprocess
import socket
import threading

def create_wifi(ssid):
    # Command to create a temporary WiFi hotspot
    command = f'sudo iw dev {ssid} interface add wifi type station'
    subprocess.run(command, shell=True)
    
    # Command to set the WiFi configuration
    command = f'sudo ip link set dev {ssid} address <MAC_ADDRESS> up'
    subprocess.run(command, shell=True)
    
    # Command to enable WiFi broadcasting for 30 seconds
    command = f'sudo iw dev {ssid} set type managed'
    subprocess.run(command, shell=True)
    command = f'sudo iw dev {ssid} set channel <CHANNEL> fixed'
    subprocess.run(command, shell=True)
    command = f'sudo iw dev {ssid} set bitrates <BITRATES>'
    subprocess.run(command, shell=True)
    command = f'sudo iw dev {ssid} set txpower <TXPOWER>'
    subprocess.run(command, shell=True)
    
    # Command to start the WiFi
    command = f'sudo iw dev {ssid} up'
    subprocess.run(command, shell=True)
    
    # Wait for 30 seconds
    threading.Thread(target=lambda: sleep(30)).start()
    
    # Command to stop the WiFi
    command = f'sudo iw dev {ssid} down'
    subprocess.run(command, shell=True)

# List of SSIDs for the temporary Wifis
ssids = [f"temp_wifi_{i}" for i in range(1, 31)]

# Create the temporary Wifis
for ssid in ssids:
    threading.Thread(target=create_wifi, args=(ssid,)).start()

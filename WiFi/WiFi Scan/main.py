print("Scanning for WiFi networks, please wait...\n")

import network

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

authmodes = ['Open', 'WEP', 'WPA-PSK' 'WPA2-PSK4', 'WPA/WPA2-PSK']
print(sta_if.scan()))

print('Scan finished! :)')

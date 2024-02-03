try:
 import usocket as socket
except:
 import socket
import network         
import gc
gc.collect()

ssid = 'ESP32'           
password = '12345678'    


ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password)
ap.active(True)  

while ap.active() == False:
  pass
print('Connection is successful')
print(ap.ifconfig()a)
def web_page():
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
  <body><h1>Welcome to ESP32's page!</h1></body></html>"""
  return html
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #creating socket object
s.bind(('', 80))
s.listen(5)
while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  print('Content = %s' % str(request))
  response = web_page()
  conn.send(response)
  conn.close()

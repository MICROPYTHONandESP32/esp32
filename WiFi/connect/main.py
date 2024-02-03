def connect(ssid,passw):
    import network
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(ssid, passw)
            
import time

ssid = 'YOUR SSID'
passw = 'YOUR PASSWORD'

connect(ssid,passw)

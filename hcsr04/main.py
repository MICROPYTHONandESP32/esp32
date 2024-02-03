import hcsr04
import time

triger_pin = 2
echo_pin = 11
hc = hcsr04.HCSR04(triger_pin,echo_pin)

while True:
  dic = hc.distance_cm()
  print(dic)
  time.sleep(0.5)

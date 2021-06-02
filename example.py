import gy271compass as GY271
from time import sleep

sensor = GY271.compass(address=0x0d)

print('[Press CTRL + C to end the script!]')
try:
    while True:
        angle = sensor.get_bearing()       
        temp = sensor.read_temp()
    
        print('Heading Angle = {}°'.format(angle))
        print('Temperature = {:.1f}°C'.format(temp))
        sleep(2)

except KeyboardInterrupt:
    print('\nScript end!')

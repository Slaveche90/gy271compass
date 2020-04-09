# GY-271 module

Python 3 script for using GY-271 compass magnetometer with the Raspberry Pi. Tested on AZ-Delivery GY-271 compass magnetometer module with QMC5883L chip

# Connection
The module has I2C communication lines, connect it to the I2C interfce of the Raspberry Pi. Default I2C address of the module is 0x0d

# Usage
Just copy the gy271compass script into the same directory with the example script. In the example script, import the gy271compass script, and create the sensor object, like in the following lines of code:   
```
import gy271compass as GY271
sensor = GY271.compass(address=0x0d)
```
and then use the sensor object to read the compass data.

# eBook
If you want to know more about this sensor, and how to use it with an Arduino or Raspberry Pi, here is the eBook:
![alt](link)
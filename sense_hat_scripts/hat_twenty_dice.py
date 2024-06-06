from random import randint
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

pix = [randint(0,100),randint(0,100),randint(0,100)]

while True:
    gyro = sense.get_accelerometer_raw()
    for i in gyro:
        gyro[i] = round(gyro[i])
    
    if gyro['x'] != 0 or gyro['y'] != 0 or gyro['z'] != 1:
        sense.show_message(str(randint(0,20)), text_colour=[randint(0,100),randint(0,100),randint(0,100)])
        sense.clear()
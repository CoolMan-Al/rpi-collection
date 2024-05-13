from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(26)
l_btn = Button(21)
r_btn = Button(20)

count = 0

sleep(uniform(5,10))
led.on()

while True:
    count+= 1
    sleep(0.001)

    if l_btn.is_active == True or r_btn.is_active == True:
        print("Left Side Won!") if l_btn.is_active == True else print("Right Side Won!")
        print("You took " + str(count) + "ms.")
        finished = True
        quit()
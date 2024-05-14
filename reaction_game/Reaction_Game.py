from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(26)
l_btn = Button(21)
r_btn = Button(20)

count = 0

def start():
    print("Get ready...")
    sleep(uniform(5,10))
    led.on()

start()
while True:
    count+= 1
    sleep(0.001)

    if l_btn.is_active == True or r_btn.is_active == True:
        print("Left!") if l_btn.is_active == True else print("Right!")
        print("You took " + str(count) + "ms.")
        led.off()
        print("Do you want to continue? Press left to stop. Press right to continue.")
        sleep(1)
        while True:
            if l_btn.is_active == True:
                print("Stopping game...")
                quit()
            elif r_btn.is_active == True:
                count = 0
                start()
                break

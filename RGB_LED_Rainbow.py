from gpiozero import RGBLED, Button
from time import sleep
from colorzero import Color

rgb = RGBLED(17,27,22)
button = Button(26)

refresh = 1000

red = 255
green = 0
blue = 0

while True:
    
    while green != 255:
        if button.is_active == False:
            green += 1
        rgb.color = Color(red,green,blue)
        sleep(1/refresh)
    
    while red != 0:
        if button.is_active == False:
            red -= 1
        rgb.color = Color(red,green,blue)
        sleep(1/refresh)
    
    while blue != 255:
        if button.is_active == False:
            blue += 1
        rgb.color = Color(red,green,blue)
        sleep(1/refresh)
    
    while green != 0:
        if button.is_active == False:
            green -= 1
        rgb.color = Color(red,green,blue)
        sleep(1/refresh)
    
    while red != 255:
        if button.is_active == False:
            red += 1
        rgb.color = Color(red,green,blue)
        sleep(1/refresh)
    
    while blue != 0:
        if button.is_active == False:
            blue -= 1
        rgb.color = Color(red,green,blue)
        sleep(1/refresh)

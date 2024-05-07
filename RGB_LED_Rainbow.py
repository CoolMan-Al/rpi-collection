from gpiozero import RGBLED
from time import sleep
from colorzero import Color

rgb = RGBLED(17,27,22) 

refresh = 1000

red = 255
green = 0
blue = 0

while True:
    
    while green != 255:
        green += 1
        rgb.color = Color(red,green,blue)
        sleep(1/refresh)
    
    while red != 0:
        red -= 1
        rgb.color = Color(red,green,blue)
        sleep(1/refresh)
    
    while blue != 255:
        blue += 1
        rgb.color = Color(red,green,blue)
        sleep(1/refresh)
    
    while green != 0:
        green -= 1
        rgb.color = Color(red,green,blue)
        sleep(1/refresh)
    
    while red != 255:
        red += 1
        rgb.color = Color(red,green,blue)
        sleep(1/refresh)
    
    while blue != 0:
        blue -= 1
        rgb.color = Color(red,green,blue)
        sleep(1/refresh)

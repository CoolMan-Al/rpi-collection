from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

light = [100,100,100]
tcol = [100,0,0]
pcol = [0,100,0]
hcol = [0,0,100]

while True:
    temp = int((sense.get_temperature() + 
                sense.get_temperature_from_pressure() +
                sense.get_temperature_from_humidity()) / 3)
    for i in range(len(str(temp))):
        sense.show_letter(str(temp)[i],text_colour=tcol)
        sleep(0.5)
        sense.clear()
        sleep(0.1)
    sense.show_letter("C", text_colour=light)
    sleep(0.5)
    sense.clear()
    sleep(1)

    press = int(sense.get_pressure())
    for i in range(len(str(press))):
        sense.show_letter(str(press)[i],text_colour=pcol)
        sleep(0.5)
        sense.clear()
        sleep(0.1)
    sense.show_message("hPa", text_colour=light)
    sleep(0.5)
    sense.clear()
    
    humid = int(sense.get_humidity())
    for i in range(len(str(humid))):
        sense.show_letter(str(humid)[i],text_colour=hcol)
        sleep(0.5)
        sense.clear()
        sleep(0.1)
    sense.show_letter("%", text_colour=light)
    sleep(0.5)
    sense.clear()
    sleep(1)

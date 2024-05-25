from sense_hat import SenseHat
from time import sleep

# Initialisation
sense = SenseHat()
sense.clear()

# Font colors for each value
light = [100,100,100]
tcol = [100,0,0]
pcol = [0,100,0]
hcol = [0,0,100]

while True:
    # Temperature reading
    # Takes temperature value from all three sensors to form average
    temp = int((sense.get_temperature() + 
                sense.get_temperature_from_pressure() +
                sense.get_temperature_from_humidity()) / 3)
    
    # Shows each digit of Temperature reading
    for i in range(len(str(temp))):
        sense.show_letter(str(temp)[i],text_colour=tcol)
        sleep(0.5)
        sense.clear()
        sleep(0.1)

    # Shows unit of measure
    # Unit of measurement excludes degrees sign because sense hat does not have the character
    sense.show_letter("C", text_colour=light)
    sleep(0.5)

    # Blanks for a second to avoid numbers and letter getting blended together
    sense.clear()
    sleep(1)

    # Pressure reading
    press = int(sense.get_pressure())

    # Shows each digit of Pressure reading
    for i in range(len(str(press))):
        sense.show_letter(str(press)[i],text_colour=pcol)
        sleep(0.5)
        sense.clear()
        sleep(0.1)
    
    # Shows unit of measure
    # Will scroll through hPa because 3 letter for single unit of measure
    sense.show_message("hPa", text_colour=light)
    sleep(0.5)
    sense.clear()
    
    # Humidity reading
    humid = int(sense.get_humidity())

    # Shows each digit of Humidity reading
    for i in range(len(str(humid))):
        sense.show_letter(str(humid)[i],text_colour=hcol)
        sleep(0.5)
        sense.clear()
        sleep(0.1)
    
    # Shows unit of measure
    sense.show_letter("%", text_colour=light)
    sleep(0.5)
    sense.clear()
    sleep(1)

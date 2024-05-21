# Use the Sense Hat V2 Joystick to draw
# Move the stick around and draw
# Middle click for switching color
# Hold Middle Click for eraser. Tap middle click again to switch back to colors

from sense_hat import SenseHat
from time import sleep

row = 0
col = 0
color_set = [
[100,100,100],
[100,0,0],
[0,100,0],
[0,0,100],
[100,100,0],
[100,0,100],
[0,100,100],
[100,0,50],
[100,50,0]
]

color = color_set[0]


sense = SenseHat()
sense.clear()

def change(event):
    global color
    if event.action == 'pressed':
        if color == [0,0,0]:
            color = color_set[0]
        else:
            if color_set.index(color) == len(color_set) - 1:
                color = color_set[0]
            else:        
                color = color_set[color_set.index(color) + 1]
    elif event.action == 'held':
        color = [0,0,0]

def up(event):
    if event.action == 'pressed':
        global row
        global col
        if row == 0:
            sense.set_pixel(col,row,100,0,0)
        
        else:
            row -= 1
            sense.set_pixel(col,row,color)

def down(event):
    if event.action == 'pressed':
        global row
        global col
        if row == 7:
            sense.set_pixel(col,row,100,0,0)
        
        else:
            row += 1
            sense.set_pixel(col,row,color)

def left(event):
    if event.action == 'pressed':
        global row
        global col
        if col == 0:
            sense.set_pixel(col,row,100,0,0)
        
        else:
            col -= 1
            sense.set_pixel(col,row,color)

def right(event):
    if event.action == 'pressed':
        global row
        global col
        if col == 7:
            sense.set_pixel(col,row,100,0,0)
        
        else:
            col += 1
            sense.set_pixel(col,row,color)

sense.set_pixel(0,0, color)

sense.stick.direction_up     = up
sense.stick.direction_down   = down
sense.stick.direction_left   = left
sense.stick.direction_right  = right
sense.stick.direction_middle = change

while True:
    pass

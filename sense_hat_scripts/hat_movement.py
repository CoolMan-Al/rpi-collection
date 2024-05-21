from sense_hat import SenseHat
from time import sleep
from numpy import array, where

row = 0
col = 0
color_set = [
[100,100,100],
[100,0,0],
[0,100,0],
[0,0,100],
[100,100,0],
[100,0,100],
[0,100,100]
]
color = color_set[0]


sense = SenseHat()
sense.clear()

def change():
    global color
    if color_set.index(color) == len(color_set) - 1:
        color = color_set[0]
    else:        
        color = color_set[color_set.index(color) + 1]

def up(event):
    if event.action == 'pressed':
        global row
        global col
        if row == 0:
            sense.set_pixel(row,col,100,0,0)
        
        else:
            row -= 1
            sense.set_pixel(row,col,color)

def down(event):
    if event.action == 'pressed':
        global row
        global col
        if row == 7:
            sense.set_pixel(row,col,100,0,0)
        
        else:
            row += 1
            sense.set_pixel(row,col,color)

def left(event):
    if event.action == 'pressed':
        global row
        global col
        if col == 0:
            sense.set_pixel(row,col,100,0,0)
        
        else:
            col -= 1
            sense.set_pixel(row,col,color)

def right(event):
    if event.action == 'pressed':
        global row
        global col
        if col == 7:
            sense.set_pixel(row,col,100,0,0)
        
        else:
            col += 1
            sense.set_pixel(row,col,color)

sense.set_pixel(0,0, color)

sense.stick.direction_left   = up
sense.stick.direction_right  = down
sense.stick.direction_up     = left
sense.stick.direction_down   = right
sense.stick.direction_middle = change

while True:
    pass
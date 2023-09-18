from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
Direction = 'right'
what = 'circle'
pie = 3.1415926535897932384626433832795
radius = 200
vertex = 360
i = 0

while (1):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)

    if what == 'rect':
        if Direction == 'right':
            y = 90
            x = x + 2
            if x == 400:
                what = 'circle'
            if x == 800:
                Direction = 'up'
        if Direction == 'up':
            y = y + 2
            if y == 600:
                Direction = 'left'
        if Direction == 'left':
            x = x - 2
            if x == 0:
                Direction = 'down'
        if Direction == 'down':
            y = y - 2
            if y == 90:
                Direction = 'right'
                
    if what == 'circle':
        radian = i * 2 * pie / vertex
        x = radius * math.cos(radian) + 400
        y = radius * math.sin(radian) + 300
        i = i + 1
        if i == vertex:
            what = 'rect'
            x = 400
            y = 90
            i = 0
    
    delay(0.01)

close_canvas()

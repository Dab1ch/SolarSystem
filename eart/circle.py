from pygame import *
from math import *
import time

init()
earth = 'earth.png'
sun = 'sun.png'

window = display.set_mode((1600, 1000))
class Cosm(sprite.Sprite):
    def __init__(self, m, v, x, y, w, h, pic):
        super().__init__()
        self.m = m
        self.v = v
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.x_speed = self.v
        self.y_speed = 0
        self.picture = transform.scale(image.load(pic), (self.w, self.h))
    def paint(self):
        window.blit(self.picture, (self.x, self.y))


R = 150*(10**9)

earth = Cosm(6 * (10 ** 24)*450/R/100, 20, 800, 50, 20, 20, earth) 
sun = Cosm(2 * (10**30)*450/R/10000, 0, 800, 500, 100, 100, sun) 

run = True
r = ((earth.x - sun.x)**2 + (earth.y - sun.y)**2) ** 0.5
G = 6.67 * 10 ** -11
while run:
    
    for i in event.get(): 
        if i.type == QUIT: 
                run = False
    earth.paint()
    sun.paint()
    display.update()
    start_time = time.time()
    while time.time() - start_time <0.001:
        pass
    earth.x = earth.x + earth.x_speed * (0.001)
    earth.y = earth.y + earth.y_speed * (0.001)

    x1 = sun.x + sun.w/2
    y1 = sun.y + sun.h/2
    x2 = earth.x + earth.w/2
    y2 = earth.y + earth.h/2

    a = G*sun.m/((x1-x2)**2+(y1-y2)**2)
    
    ax = a * (x1-x2)/((x1-x2)**2+(y1-y2)**2)**0.5
    ay = a * (y1-y2)/((x1-x2)**2+(y1-y2)**2)**0.5


    earth.x_speed = earth.x_speed + ax * (0.001)
    earth.y_speed = earth.y_speed + ay * (0.001)
    window.fill((0, 0, 0))
    sun.paint()
    earth.paint()
    display.update()
    

import sys 
import pygame as pg

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,(120,20,220),(self.x,self.y,self.w,self.h))

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
x = 20
h = 20

while(run):
    screen.fill((255, 255, 255))

    firstObject = Rectangle(x,h,100,100)

    keys = pg.key.get_pressed()

    firstObject.draw(screen) # ใส่ screen เข้าไปด้วยเพราะว่าคำสั่ง pg.draw.rect จะเป็นจะต้องระบุระนาบว่าต้องการสร้างรูปบนระนาบใด
    pg.display.update()
    
    print(firstObject.x, firstObject.y)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    if keys[pg.K_w]:
         h -= 0.3
    if keys[pg.K_a]:
        x -= 0.3
    if keys[pg.K_s]:
        h += 0.3
    if keys[pg.K_d]:
        x += 0.3
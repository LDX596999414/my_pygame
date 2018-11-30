import pygame as pg
import sys

pg.init()
size = width, height = 640, 480
screen = pg.display.set_mode(size)

screen.fill((255, 255, 255))
background = pg.image.load("1.jpg")
screen.blit(background, (0, 0))

ali = pg.image.load("ali.png")
alirect = ali.get_rect()   # 获取矩形区域
speed = [50, 50]
clock = pg.time.Clock()  # 每秒执行60次
while True:  # 死循环保证窗口一直显示
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    #screen.fill(color)
    screen.blit(background, (0, 0))
    screen.blit(ali, alirect)
    pg.display.flip()  # 更新全部显示
    alirect = alirect.move(speed)
    # 碰撞检测；
    if alirect.left < 0 or alirect.right > width:  # 检测左右边缘
        speed[0] = -speed[0]
    if alirect.top < 0 or alirect.bottom > height:  # 检测上下边缘
        speed[1] = -speed[1]


pg.quit()

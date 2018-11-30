import pygame as pg
import sys


class Bird(object):
    def __init__(self):
        pass

    def bridUpdate(self):
        pass


class Pipeline(object):
    def __init__(self):
        pass

    def updatePipeline(self):
        pass


def createMap():
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    pg.display.update()


if __name__ == "__main__":
    pg.init()
    size = width, height = 384, 598
    screen =pg.display.set_mode(size)
    clock = pg.time.Clock()
    Pipeline = Pipeline()
    Bird = Bird()
    while True:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        background = pg.image.load("1.jpg")
        createMap()
    pg.quit()
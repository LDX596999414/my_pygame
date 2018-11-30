import pygame as pg
import sys


class Bird(object):
    def __init__(self):
        self.birdRect = pg.Rect(65, 50, 50, 50)  # pygame.Rect(left, top, width, height)
        self.birdStatus = [pg.image.load("ali.png"),
                           pg.image.load("ali.png"),
                           pg.image.load("ali.png")]
        self.status = 0
        self.birdX = 120
        self.birdY = 350
        self.jump = False
        self.jumpSpeed = 10
        self.gravity = 0
        self.dead = False

    def birdUpdate(self):
        if self.jump:
            self.jumpSpeed -= 1
            self.birdY -= self.jumpSpeed
        else:
            self.gravity = 0.01
            self.birdY += self.gravity
        self.birdRect[1] = self.birdY


class Pipeline(object):
    def __init__(self):
        self.wallx = 400
        self.pineUp = pg.image.load("ali.png")
        self.pineDown = pg.image.load("ali.png")

    def updatePipeline(self):
        self.wallx -= 5
        if self.wallx < - 80:
            global score
            score += 1
            self.wallx = 400


def createMap():
    screen.fill((255, 255, 255))
    background = pg.image.load("1.jpg")
    screen.blit(background, (0, 0))

    screen.blit(Pipeline.pineUp, (Pipeline.wallx, -300))
    screen.blit(Pipeline.pineDown, (Pipeline.wallx, 500))

    if Bird.dead:
        Bird.status = 2
    elif Bird.jump:
        Bird.status = 1
    screen.blit((Bird.birdStatus[Bird.status]), (Bird.birdX, Bird.birdY))


if __name__ == '__main__':
    pg.init()
    pg.font.init()
    font = pg.font.SysFont("Arial", 50)
    size = width, height = 400, 650
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()
    Pipeline = Pipeline()
    Bird =Bird()
    score = 0
    while True:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if (event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN) and not Bird.dead:
                Bird.jump = True
                Bird.gravity = 5
                Bird.jumpSpeed =15

        createMap()

    pg.quit()


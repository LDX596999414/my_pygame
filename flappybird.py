import pygame as pg
import sys


class Bird(object):
    def __init__(self):
        self.birdRect = pg.Rect(65, 50, 50, 50)  # pygame.Rect(left, top, width, height)
        self.birdStatus = [pg.image.load("ali.png"),
                           pg.image.load("ali.png"),
                           pg.image.load("ali.png")]
        self.status = 0      # 默认飞行状态
        self.birdX = 10     # 鸟所在X轴坐标，即是向右的飞行速度
        self.birdY = 10     # 鸟所在Y轴坐标，即上下飞行速度
        self.jump = False    # 默认情况小鸟自动降落
        self.jumpSpeed = 10  # 跳跃高度
        self.gravity = 0     # 重力
        self.dead = False    # 默认小鸟的生命状态为活着

    def bridUpdate(self):
        if self.jump:
            self.jumpSpeed -= 1            # 速度递减， 上升越来越慢
            self.birdY -= self.jumpSpeed   # 小鸟Y轴坐标减小， 小鸟上升
        else:
            # 小鸟掉落
            self.gravity = 0.01
            self.birdY += self.gravity     # 重力增加 下落越来越快
        self.birdRect[1] = self.birdY      # 更改Y轴位置


class Pipeline(object):
    def __init__(self):
        pass

    def updatePipeline(self):
        pass


def createMap():
    screen.fill((255, 255, 255))       # 填充颜色
    screen.blit(background, (0, 0))    # 填入背景
    # 显示ali
    screen.blit(Bird.birdStatus[0], (Bird.birdX, Bird.birdY))  # 设置ali坐标
    pg.display.update()                # 显示更新


if __name__ == "__main__":
    pg.init()
    size = width, height = 384, 598
    screen = pg.display.set_mode(size)
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
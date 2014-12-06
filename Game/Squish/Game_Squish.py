#__encoding:utf-8__#
import sys,pygame
from pygame.locals import *#import所有的常量名字
from random import randrange


class Weight(pygame.sprite.Sprite):#都是从pygame.sprite.Sprite中继承下来的

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #在画sprite时使用的图像和矩形
        self.image = weight_image
        self.rect=self.image.get_rect()
        self.reset()
    def reset(self):
        '''
        将石头移动到屏幕顶端的随机位置
        '''
        self.rect.top=-self.rect.height
        self.rect.centerx=randrange(screen_size[0])

    def update(self):
        #更新石头，显示下一帧
        self.rect.top+=1
        if self.rect.top>screen_size[1]:
            self.reset()

#初始化
pygame.init()
screen_size = 800,600
pygame.display.set_mode(screen_size,FULLSCREEN)
pygame.mouse.set_visible(False)#用false可以吗？
#载入石头的图像
weight_image=pygame.image.load('banana.png').convert()#转化
#创建一个子图像组（sprite group），增加weight
sprites=pygame.sprite.RenderUpdates()#sprites对象名可以自己起
sprites.add(Weight())
#获取屏幕表面，并且填充
screen = pygame.display.get_surface()
bg=(255,255,255)#白色
screen.fill(bg)
pygame.display.flip()#全屏更新

#用于清除子图形
def clear_callback(surf,rect):
    surf.fill(bg,rect)

while True:
    #检查退出事件
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
        if event.type==KEYDOWN and event.key==K_ESCAPE:
            sys.exit()
#清除前面的位置
sprites.clear(screen,clear_callback)
#更新所有子图形
sprites.update()
#绘制所有子图形
updates=sprites.draw(screen)
#更新所有需要显示的部分
pygame.display.update(updates)



        
    

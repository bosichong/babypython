import pygame # 引入pygame游戏框架包
from pygame.locals import * #导入游戏常量

pygame.init()# 游戏初始化

screen =pygame.display.set_mode([800,600])#设置游戏屏幕的大小
pygame.display.set_caption("游戏测试")#设置游戏窗口的标题。
gameStart = True#游戏循环的触发 true
BLACK = (0,0,0)
RED = (255,0,0)

##游戏开始
while gameStart:
    screen.fill(BLACK)#场景背景色

   


    #判断游戏是否结束
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameStart = False
            
    pygame.display.update()#刷新游戏场景


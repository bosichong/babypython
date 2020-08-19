#弹球小游戏制作过程
'''
1.新建一个Python文件，起名tqball.py.
2.复制游戏框架。
3.创建小球的变量。
4.创建一个球拍
5.场景里绘制小球
6.场景绘制球拍
7.让小球动起来
8.让小球反弹
9.让球拍跟随鼠标动起来。
10.处理小球和球拍的碰撞

'''





import pygame # 引入pygame游戏框架包
from pygame.locals import * #导入游戏常量

pygame.init()# 游戏初始化

screen =pygame.display.set_mode([800,600])#设置游戏屏幕的大小
pygame.display.set_caption("弹球小游戏")#设置游戏窗口的标题。
gameStart = True#游戏循环的触发 true
BLACK = (0,0,0)
RED = (255,0,0)
ball = pygame.image.load('/Users/mac/Documents/垚垚python/smiley.png')
ballx = 0
bally = 0
ballw = 100
ballh = 100
speedx = 5
speedy = 5


padx = 300
pady = 500
padw = 200
padh = 25


##游戏开始
while gameStart:
    screen.fill(BLACK)#场景背景色
    screen.blit(ball,(ballx,bally))#绘制小球
    #绘制球拍
    padx = pygame.mouse.get_pos()[0]#获取鼠标的坐标X
    padx -= padw/2#控制球拍的X值
    pygame.draw.rect(screen,RED,(padx,pady,padw,padh))

    ballx += speedx
    bally += speedy

        #控制小球的上下反弹。
    if bally >=500  or bally<=0 :
        speedy = -speedy
    #控制小球的左右反弹
    if ballx >=700 or ballx <= 0:
        speedx = -speedx

    #处理小球和球拍的碰撞
    #小球碰到球拍反弹
    #小球的中心坐标必需同时满足打球拍X还得小于X+球拍的宽度。
    if ballx + ballw/2 >= padx and ballx + ballw/2 <= padx+padw:
        if bally+ballh >= pady:
            speedy = -speedy#小球遇到球拍反弹
   


    #判断游戏是否结束
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameStart = False
            
    pygame.display.update()#刷新游戏场景


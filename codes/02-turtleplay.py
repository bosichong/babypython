# 运动命令:
# forward(d)                            向前移动距离d代表距离
# backward(d)                         向后移动距离d代表距离
# right(degree)                        向右转动多少度
# left(degree)                          向左转动多少度
# goto(x,y)                              将画笔移动到坐标为(x,y)的位置
# stamp()                                绘制当前图形
# speed(speed)                      画笔绘制的速度范围[0,10]整数

# 画笔控制命令:

# down()                                 画笔落下，移动时绘制图形
# up()                                     画笔抬起，移动时不绘制图形
# setheading(degree)            海龟（turtle）朝向，degree代表角度
# reset()                                 恢复所有设置
# pensize(width)                    画笔的宽度
# pencolor(colorstring)          画笔的颜色
# fillcolor(colorstring)             绘制图形的填充颜色
# circle(radius,extent)            绘制一个圆形，其中radius为半径，extent为度数，例如若extent为120，则画一个三分之一圆；





import turtle #引入海龟图形功能包
import random
t = turtle.Pen() #使用海龟的画笔，这个时候t就是海龟的画笔
t.speed(10)
# t.forward(100) #画笔运行 其中X是距离

def hz():
    '''画一个正方形'''
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.up()
    t.goto(random.randint(-200,200),random.randint(-200,200))
    t.down()



def luxi(a,b):
    '''画线'''
    t.forward(a)
    t.left(b)

for i in range(91):
    luxi(200,91)
    # hz()
    






input()#防止终端退出

# turtle.getscreen()._root.mainloop()  # <-- run the Tkinter main loop
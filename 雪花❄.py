import turtle
import random

# 全局设置
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)  # 全屏窗口
screen.bgcolor("black")               # 黑色背景更衬雪花
screen.tracer(0)                      # 关闭自动刷新，提升速度
turtle.colormode(255)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# 递归科赫曲线
def koch(length, level):
    if level == 0:
        pen.forward(length)
    else:
        seg = length / 3
        koch(seg, level - 1)
        pen.left(60)
        koch(seg, level - 1)
        pen.right(120)
        koch(seg, level - 1)
        pen.left(60)
        koch(seg, level - 1)

# 绘制单朵雪花
def draw_snowflake(x, y, size, depth):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    # 随机彩色
    r = random.randint(150, 255)
    g = random.randint(200, 255)
    b = random.randint(220, 255)
    pen.pencolor(r, g, b)
    pen.pensize(1)
    # 绘制三角雪花
    for _ in range(3):
        koch(size, depth)
        pen.right(120)

# 生成满屏雪花
def create_full_snow():
    screen_width = screen.window_width()
    screen_height = screen.window_height()
    snow_count = 80  # 雪花数量，可增减
    
    for _ in range(snow_count):
        # 随机位置、大小、递归层数
        rand_x = random.randint(-screen_width//2, screen_width//2)
        rand_y = random.randint(-screen_height//2, screen_height//2)
        rand_size = random.randint(20, 80)
        rand_level = random.randint(1, 3)
        
        draw_snowflake(rand_x, rand_y, rand_size, rand_level)
    screen.update()  # 统一刷新画面

if __name__ == "__main__":
    create_full_snow()
    turtle.done()

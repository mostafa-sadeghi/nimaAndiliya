# exercise 1:
# سه رنگ قرمز، سبز و آبی داریم
# می خواهیم یک ستاره با کمک ترتل بکشیم
# هر یک از خط های ستاره باید یکی از رنگ های بالا را داشته باشد.
# هربار که برنامه اجرا می شود، می بایست یک رنگ به عنوان رنگ پر کردن ستاره انتخاب شود
# این رنگ به صورت تصادفی می بایست انتخاب گردد
#exercise2 : rotated squares  هر یک از مربع ها یکی از رنگ های سبز، ابی و یا قرمز را داشته باشند

# import random
# import turtle

# print(random.random())
# for i in range(50):
#     print(random.randrange(1,50))
# COLORS = ("red","green","blue")
# # random_index = random.randrange(len(COLORS))
# # print(COLORS[random_index])
# fill_color = random.choice(COLORS)
# # print(random.choice(COLORS))
# screen = turtle.Screen()
# screen.bgcolor("black")
# pen = turtle.Turtle()
# pen.pensize(4)
# pen.fillcolor(fill_color)
# pen.begin_fill()
# for i in range(5):
#     pen.pencolor(COLORS[i % 3])
#     pen.forward(150)
#     pen.right(144)

# pen.end_fill()

# turtle.done()


import turtle

def draw_rotated_squares(color,x,y,speed):
    pen.pencolor(color)
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.speed(speed)
    for i in range(12):
        for j in range(4):
            pen.forward(100)
            pen.lt(90)
        pen.left(30)
def draw_rotated_squares2(x,y):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    for i in range(12):
        for j in range(4):
            pen.forward(100)
            pen.lt(90)
        pen.left(30)

screen = turtle.Screen()
screen.setup(800, 750)
pen = turtle.Turtle()
pen.shape('turtle')
# draw_rotated_squares('red',200,200,'fastest')
# draw_rotated_squares('green',-200,-200,'fast')
pen.onclick(draw_rotated_squares2)
turtle.done()


# سایز قلم را هم به عنوان پارامتر اضافه کنید
# لیست رنگ را به عنوان پارامتر به تابع اضافه کنید
# به گونه ای که لیست فقط شامل سه رنگ باشد
# draw_rotated_squares(['red','green','blue'],200,200,'fastest')
# draw_rotated_squares(['cyan','brown','blue'],-200,-200,'fast')
# 

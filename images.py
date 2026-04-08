'''from turtle import *

bgcolor("black")
pensize(2)
color("green")
left(90)
backward(100)
speed(200)
shape("turtle")

def tree(i):
    if i<10:
        return
    else:
        forward(i)
        color("orange")
        circle(2)
        color("brown")
        left(30)
        tree(3*i/4)
        right(60)
        tree(3*i/4)
        left(30)
        backward(i)
tree(100)
done()'''

'''import turtle

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('#000000')
t.speed(10)

for _ in range(36):
    t.pencolor("red")
    t.circle(100)
    t.left(10)

turtle.done()'''


'''import turtle as r 
import colorsys as sm
r.tracer(2)
r.bgcolor("black")
r.pensize(2)
n=100
h=0
for i in range(500):
    for i in range(4):
        c=sm.hsv_to_rgb(h,1,1)
        h+=1/n
        r.color(c)
        r.circle(49+i*5,90)
        r.forward(100)
        r.left(90)
    r.right(10)
r.done()'''


'''from turtle import *
from colorsys import * 
tracer(20)
bgcolor("black")
h=0.95
for i in range(400):
    pencolor(hsv_to_rgb(h,1,1))
    h+=0.0011
    right(119)
    circle(-i*0.3,120)
    circle(i*0.3,120)
    circle(-i*0.1,120)
done()'''


'''from turtle import *
bgcolor("black")
color("orange")
speed(0)
for i in range(200):
    goto(0,0)
    fd(250)
    lt(3)
    circle(150,-90)
    rt(90)
    hideturtle()
done()'''


from turtle import *
from colorsys import *
tracer(10)
bgcolor("black")
pensize(2)
h=0
def draw(int,t):
    circle(5+t,90)
    left(int)
    circle(5+t,60)

for i in range(200):
    c=hsv_to_rgb(h,1,1)
    color(c)
    up()
    draw(90,i/50)
    draw(180,i/4)
    down()
    fillcolor("black")
    begin_fill()
    draw(1/2,0)
    draw(180,i/4)
    draw(90,i/4)
    end_fill()
    draw(60,i/2)
    hideturtle()
done()

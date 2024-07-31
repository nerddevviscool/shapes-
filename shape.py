import turtle
turtle.title('my turtle')
turtle.bgcolor("green")
turtle.setup(500, 300)
turtle.shape("turtle")


screen = turtle.Screen()
fork = turtle.Turtle()

def star(length, color):
    fork.fillcolor(color)
    fork.begin_fill()
    x = 0
    while x <5:
        fork.forward(int(length))
        fork.right(144)
        x = x + 1
    fork.end_fill()


def triangle(length, color):
    fork.fillcolor(color)
    fork.begin_fill()
    x = 0
    while x <3:
        fork.forward(int(length))
        fork.right(120)
        x = x + 1
    fork.end_fill()


def hex(length, color):
    fork.fillcolor(color)
    fork.begin_fill()
    x = 0
    while x <6:
        fork.forward(int(length))
        fork.right(60)
        x = x + 1
    fork.end_fill()


def circle(lenght, color):
    fork.fillcolor(color)
    fork.begin_fill()
    fork.circle(int(lenght))
    fork.end_fill()









 


shape = input('what is a cool shae you like ')
size = input('how bigg:')
color = input ('what color')
if shape == "star":
    star(size, color)

if shape == "triangle":
    triangle(size, color)
if shape == "circle":
    circle(size, color)        

if shape == "hex":
    hex(size, color)    
    
turtle.done()

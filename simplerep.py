# import turtle
# screen = turtle.Screen()
# screen.bgcolor("white")

# t = turtle.Turtle()
# t.color("black")
# t.speed(1)  

# for i in range(4):
#     t.forward(200)
#     t.left(90)

# turtle.done()

# def square(t,length):
#     for i in range(4):
#         t.forward(length)
#         t.left(90)  

def polygon(t,length,n):
    angle=360.0/n
    print(angle)
    for i in range(n):
        t.forward(length)
        t.left(angle) 


import turtle
screen = turtle.Screen()
screen.bgcolor("white")
bob=turtle.Turtle()
# square(bob,300)
polygon(bob,70,7)
turtle.done()



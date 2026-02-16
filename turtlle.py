# import turtle
# bob=turtle.Turtle()
# print(bob)
# turtle.mainloop()
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)

import turtle
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.color("black")
t.speed(1)        # 👈 IMPORTANT: slow enough to see movement

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
turtle.done()

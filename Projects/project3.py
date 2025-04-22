# setup
import turtle

t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("purple")
t.pendown()
t.speed(100)
 # directions
for i in range(100):
    t.forward(10 + i)
    t.left(10)

for i in range(100):
    t.forward(20 + i)
    t.left(10)

for i in range(100):
    t.forward(30 + i)
    t.left(10)

for i in range(100):
    t.forward(40 + i)
    t.left(10)

for i in range(100):
    t.forward(50 + i)
    t.left(10)

for i in range(100):
    t.forward(60 + i)
    t.left(10)

for i in range(100):
    t.forward(70 + i)
    t.left(10)

for i in range(100):
    t.forward(80)
    t.left(10)

t.goto(-100, -70)

for i in range(100):
    t.forward(10)
    t.left(10)

for i in range(100):
    t.forward(20)
    t.left(10)

for i in range(100):
    t.forward(30)
    t.left(10)

for i in range(100):
    t.forward(40)
    t.left(10)

for i in range(100):
    t.forward(50)
    t.left(10)

for i in range(100):
    t.forward(60)
    t.left(10)

for i in range(100):
    t.forward(70)
    t.left(10)

for i in range(100):
    t.forward(80)
    t.left(10)


# ending
turtle.exitonclick()


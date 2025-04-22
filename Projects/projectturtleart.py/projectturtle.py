
# setup
import turtle

t = turtle.Turtle()

t.color ( "yellow" )
turtle.Screen().bgcolor("yellow")

t.penup()
t.goto(0, -100)
t.color("black")
t.pendown()
t.speed(100)
t.pensize(4)
# directions
for i in range(100):
    t.forward(30)
    t.left(10)

t.penup()
t.goto(-40, -40)
t.pendown()
t.setheading(90)
for i in range(10):
    t.forward(30)
    t.right(10)


t.penup()
t.goto(-110, 50)
t.pendown()
t.setheading(90)
for i in range(100):
    t.forward(5)
    t.right(10)

t.penup()
t.goto(-70, 140)
t.pendown()
t.setheading(90)
for i in range(100):
    t.forward(5)
    t.right(10)

t.penup()
t.goto(-70, 140)
t.pendown()
t.setheading(50)
for i in range(100):
    t.forward(5)
    t.right(10)





# ending

turtle.exitonclick()
import turtle
t = turtle.Turtle()

# setup
t.speed(1000)
turtle.Screen().bgcolor("light blue")
H = 500

# stripes

# move to stripe 1
t.penup
t.goto(-250, -100)
t.pendown

# stripe 1
t.color("dark green")
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(H)
t.left(90)
t.forward(150)
t.left(90)
t.forward(H)
t.left(90)
t.end_fill()

t.penup
t.goto(-100, -100)
t.pendown

# stripe 2
t.color("white")
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(H)
t.left(90)
t.forward(150)
t.left(90)
t.forward(H)
t.left(90)
t.end_fill()

t.penup
t.goto(50, -100)
t.pendown

# stripe 3
t.color("dark red")
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(H)
t.left(90)
t.forward(150)
t.left(90)
t.forward(H)
t.left(90)
t.end_fill()






turtle.exitonclick()

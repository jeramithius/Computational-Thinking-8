import turtle

t = turtle.Turtle()
t.penup()
t.goto(0, 0)
t.color("purple")
t.pendown()
t.speed(100)



colors = ["pink", "cyan", "purple"]
for i in range(139):
    t.color( colors[ i % 3 ] )
    t.forward(56 + i)
    t.left(75)


turtle.exitonclick()
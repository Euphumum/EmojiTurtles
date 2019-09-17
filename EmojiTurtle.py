import turtle


bobby = turtle.Turtle()
scn = turtle.Screen()
billy = turtle.Turtle()
randy = turtle.Turtle()
juliana = turtle.Turtle()
bobby.speed(10)
randy.speed(10)
billy.speed(10)
juliana.speed(10)


bobby.color("yellow")
bobby.pencolor("black")
bobby.penup()
bobby.begin_fill()
bobby.goto(-0, -280)
bobby.pendown()
bobby.circle(300)
bobby.end_fill()

billy.penup()
billy.begin_fill()
billy.goto(120, 90)
billy.pendown()
billy.circle(75)
billy.end_fill()


randy.penup()
randy.begin_fill()
randy.goto(-120, 90)
randy.pendown()
randy.circle(75)
randy.end_fill()

billy.pencolor("white")
billy.color("white")
billy.penup()
billy.begin_fill()
billy.goto(120, 115)
billy.pendown()
billy.circle(50)
billy.end_fill()

randy.pencolor("white")
randy.color("white")
randy.penup()
randy.goto(-120, 115)
randy.pendown()
randy.begin_fill()
randy.circle(50)
randy.end_fill()


juliana.goto(0, -225)
juliana.pencolor("white")
juliana.begin_fill()
juliana.color("black")
juliana.circle(150)
juliana.end_fill()

turtle.exitonclick()
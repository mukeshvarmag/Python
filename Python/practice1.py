import turtle

def draw_spiderman(pen):
    pen.penup()
    pen.goto(-100,0)
    pen.pendown()

    # Draw the head
    pen.circle(50)

    # Draw the eyes
    pen.penup()
    pen.goto(-60, 60)
    pen.pendown()
    pen.circle(10)
    pen.penup()
    pen.goto(-80, 60)
    pen.pendown()
    pen.circle(10)

    # Draw the mouth
    pen.penup()
    pen.goto(-70, 40)
    pen.pendown()
    pen.right(140)
    pen.forward(30)
    pen.right(100)
    pen.forward(30)

    # Draw the body
    pen.penup()
    pen.goto(-100, -50)
    pen.pendown()
    pen.right(90)
    pen.forward(100)

    # Draw the legs
    pen.penup()
    pen.goto(-100, -50)
    pen.pendown()
    pen.right(45)
    pen.forward(50)
    pen.right(90)
    pen.forward(50)
    pen.right(45)
    pen.forward(70)

    pen.penup()
    pen.goto(-100, -50)
    pen.pendown()
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(50)
    pen.left(45)
    pen.forward(70)

turtle.speed(0)
draw_spiderman(turtle)
turtle.done()

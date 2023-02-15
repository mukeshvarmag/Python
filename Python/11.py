import turtle 

ninja = turtle.Turtle()

ninja.speed(10)

for i in range(180):

    if i%3==0:
        ninja.pencolor("red")
    elif i%3==1:
        ninja.pencolor("green")
    elif i%3==2:
        ninja.pencolor("blue") 

    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)

        
    
turtle.done()
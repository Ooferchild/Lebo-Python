#Josh
#10-14
import turtle

window = turtle.Screen()
window.screensize(1000,1000)
window.title("Checkerboard")

t = turtle.Turtle()
t.speed(0)

square_size = 50

t.penup()
t.goto(-200, 200)

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            t.fillcolor("black")
        else:
            t.fillcolor("red")
        t.begin_fill()
        for _ in range(4):
            t.forward(square_size)
            t.left(90)
        t.end_fill()
        t.forward(square_size)
    t.backward(8 * square_size)
    t.right(90)
    t.forward(square_size)
    t.left(90)

t.goto(-300,300)

t.hideturtle()

turtle.exitonclick()
#Josh
#Dec 12 .. Drawing1... How to make out turtle move
##################################################
import turtle as t

window = t.Screen()
window.screensize(50,50)
window.bgcolor("black")
window.title("Turtle Art")

t.shape("circle")
t.color("white")
t.turtlesize(.5)

#drawing
t.speed(1)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)

t.penup()
t.fd(100)

t.pencolor("red")
t.pensize(5)
t.pendown()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)

t.penup()
t.fd(100)

t.pencolor("orange")
t.pensize(5)
t.pendown()

t.fd(100)
t.lt(72)
t.fd(100)
t.lt(72)
t.fd(100)
t.lt(72)
t.fd(100)
t.lt(72)
t.fd(100)
#-----
t.penup()
t.fd(100)
t.pencolor("pink")
t.pendown()

t.fd(50)
t.lt(60)
t.fd(50)
t.lt(60)
t.fd(50)
t.lt(60)
t.fd(50)
t.lt(60)
t.fd(50)
t.lt(60)
t.fd(50)

window.exitonclick()#end line
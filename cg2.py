import turtle

# Initialize the graphics window
screen = turtle.Screen()
screen.title("Basic Shapes")
screen.bgcolor("white")

t = turtle.Turtle()
t.color("black")
t.width(2)
t.speed(3)

# Draw a line
t.penup()
t.goto(-200, 0)
t.pendown()
t.forward(100)

# Draw a rectangle
t.penup()
t.goto(-50, -50)
t.pendown()
for _ in range(2):
    t.forward(120)
    t.left(90)
    t.forward(60)
    t.left(90)

# Draw a circle
t.penup()
t.goto(150, -50)
t.pendown()
t.circle(40)

# Keep the window open
screen.exitonclick()
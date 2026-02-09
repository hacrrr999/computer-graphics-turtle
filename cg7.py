import turtle

# Initialize graphics window
screen = turtle.Screen()
screen.title("Midpoint Line Drawing Algorithm")
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# Input endpoints
x1, y1 = -100, -40
x2, y2 = 100, 60

# Midpoint Line Algorithm (slope between 0 and 1)
dx = x2 - x1
dy = y2 - y1

d = dy - (dx / 2)

x, y = x1, y1

# Plot first point
t.goto(x, y)
t.dot(3, "black")

# Plot remaining points
while x < x2:
    x += 1
    if d < 0:
        d += dy
    else:
        y += 1
        d += dy - dx

    t.goto(x, y)
    t.dot(3, "black")

# Keep window open
screen.exitonclick()
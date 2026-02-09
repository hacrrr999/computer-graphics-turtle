import turtle

# Initialize graphics window
screen = turtle.Screen()
screen.title("Bresenham's Line Drawing Algorithm")
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# Input endpoints
x1, y1 = -120, -80
x2, y2 = 120, 60

# Bresenham's Algorithm (for slope between 0 and 1)
dx = x2 - x1
dy = y2 - y1

p = 2 * dy - dx

x, y = x1, y1

# Plot first point
t.goto(x, y)
t.dot(3, "black")

# Plot remaining points
for _ in range(dx):
    x += 1
    if p < 0:
        p += 2 * dy
    else:
        y += 1
        p += 2 * (dy - dx)

    t.goto(x, y)
    t.dot(3, "black")

# Keep window open
screen.exitonclick()
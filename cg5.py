import turtle

# Initialize graphics window
screen = turtle.Screen()
screen.title("DDA Line Drawing Algorithm")
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# Input endpoints
x1, y1 = -100, -50
x2, y2 = 100, 80

# DDA Algorithm
dx = x2 - x1
dy = y2 - y1

steps = max(abs(dx), abs(dy))

x_increment = dx / steps
y_increment = dy / steps

x = x1
y = y1

# Plot the line
for _ in range(steps + 1):
    t.goto(round(x), round(y))
    t.dot(3, "black")   # plotting pixel
    x += x_increment
    y += y_increment

# Keep window open
screen.exitonclick()
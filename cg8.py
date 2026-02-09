import turtle

# Initialize graphics window
screen = turtle.Screen()
screen.title("Bresenham's Circle Drawing Algorithm")
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# Circle parameters
xc, yc = 0, 0     # Center of circle
r = 80            # Radius

# Function to plot all 8 symmetric points
def plot_circle_points(x, y):
    points = [
        ( xc + x, yc + y), ( xc - x, yc + y),
        ( xc + x, yc - y), ( xc - x, yc - y),
        ( xc + y, yc + x), ( xc - y, yc + x),
        ( xc + y, yc - x), ( xc - y, yc - x)
    ]
    for px, py in points:
        t.goto(px, py)
        t.dot(3, "black")

# Bresenham's circle algorithm
x = 0
y = r
d = 3 - 2 * r

while x <= y:
    plot_circle_points(x, y)
    if d < 0:
        d = d + 4 * x + 6
    else:
        d = d + 4 * (x - y) + 10
        y -= 1
    x += 1

# Keep window open
screen.exitonclick()
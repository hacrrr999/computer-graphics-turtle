import turtle

# Initialize graphics window
screen = turtle.Screen()
screen.title("Midpoint Circle Drawing Algorithm")
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# Circle parameters
xc, yc = 0, 0   # Center
r = 80          # Radius

# Function to plot 8 symmetric points
def plot_circle_points(x, y):
    points = [
        (xc + x, yc + y), (xc - x, yc + y),
        (xc + x, yc - y), (xc - x, yc - y),
        (xc + y, yc + x), (xc - y, yc + x),
        (xc + y, yc - x), (xc - y, yc - x)
    ]
    for px, py in points:
        t.goto(px, py)
        t.dot(3, "black")

# Midpoint circle algorithm
x = 0
y = r
d = 1 - r

plot_circle_points(x, y)

while x < y:
    x += 1
    if d < 0:
        d += 2 * x + 1
    else:
        y -= 1
        d += 2 * (x - y) + 1
    plot_circle_points(x, y)

# Keep window open
screen.exitonclick()
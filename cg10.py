import turtle

# Initialize graphics window
screen = turtle.Screen()
screen.title("Midpoint Ellipse Drawing Algorithm")
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# Ellipse parameters
xc, yc = 0, 0   # Center of ellipse
rx, ry = 100, 60  # Radii along x and y

# Function to plot 4 symmetric points of the ellipse
def plot_ellipse_points(x, y):
    points = [
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y)
    ]
    for px, py in points:
        t.goto(px, py)
        t.dot(3, "red")

# Midpoint Ellipse Algorithm
x = 0
y = ry

# Decision parameter for region 1
rx2 = rx * rx
ry2 = ry * ry
two_rx2 = 2 * rx2
two_ry2 = 2 * ry2

px = 0
py = two_rx2 * y

# Region 1
d1 = ry2 - (rx2 * ry) + (0.25 * rx2)
while px < py:
    plot_ellipse_points(x, y)
    x += 1
    px += two_ry2
    if d1 < 0:
        d1 += ry2 + px
    else:
        y -= 1
        py -= two_rx2
        d1 += ry2 + px - py

# Region 2
d2 = ry2 * ((x + 0.5) ** 2) + rx2 * ((y - 1) ** 2) - rx2 * ry2
while y >= 0:
    plot_ellipse_points(x, y)
    y -= 1
    py -= two_rx2
    if d2 > 0:
        d2 += rx2 - py
    else:
        x += 1
        px += two_ry2
        d2 += rx2 - py + px

# Keep window open
screen.exitonclick()
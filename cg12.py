import turtle

# Initialize screen
screen = turtle.Screen()
screen.title("Scanline Polygon Fill Algorithm")
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# Define polygon vertices (clockwise or counter-clockwise)
polygon = [(-100, -50), (-50, 100), (50, 100), (100, -50), (0, -100)]

# Draw polygon boundary
t.color("black")
t.pensize(2)
t.goto(polygon[0])
t.pendown()
for vertex in polygon[1:]:
    t.goto(vertex)
t.goto(polygon[0])  # Close polygon
t.penup()

# Scanline fill
# Find min and max y
ys = [y for x, y in polygon]
ymin = min(ys)
ymax = max(ys)

# Fill polygon scanline by scanline
for y in range(ymin, ymax + 1, 2):  # step 2 for visibility
    # Find intersections with polygon edges
    intersections = []
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]
        if y1 == y2:  # horizontal edge
            continue
        if y1 < y2:
            ymin_edge, ymax_edge = y1, y2
            x_at_ymin = x1
        else:
            ymin_edge, ymax_edge = y2, y1
            x_at_ymin = x2
        if ymin_edge <= y < ymax_edge:
            x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            intersections.append(x)

    intersections.sort()

    # Draw horizontal lines between pairs of intersections
    for i in range(0, len(intersections), 2):
        if i + 1 < len(intersections):
            t.goto(intersections[i], y)
            t.pendown()
            t.goto(intersections[i + 1], y)
            t.penup()

# Keep window open
screen.mainloop()

import turtle

# Initialize screen
screen = turtle.Screen()
screen.title("Sutherland-Hodgman Polygon Clipping")
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# Define clipping window
xmin, ymin = -100, -100
xmax, ymax = 100, 100

# Draw clipping rectangle
t.color("black")
t.pensize(2)
t.penup()
t.goto(xmin, ymin)
t.pendown()
t.goto(xmin, ymax)
t.goto(xmax, ymax)
t.goto(xmax, ymin)
t.goto(xmin, ymin)
t.penup()

# Original polygon (some vertices outside the window)
polygon = [(-150, -50), (-50, 150), (50, 120), (150, -20), (70, -150), (-100, -100)]

# Draw original polygon in blue
t.color("blue")
t.penup()
t.goto(polygon[0])
t.pendown()
for pt in polygon[1:]:
    t.goto(pt)
t.goto(polygon[0])
t.penup()

# --- Sutherland-Hodgman Algorithm ---
def clip_polygon(poly, edge):
    """Clip polygon against one edge"""
    clipped = []
    for i in range(len(poly)):
        curr = poly[i]
        prev = poly[i-1]
        if edge(curr):
            if not edge(prev):
                # Entering, add intersection
                clipped.append(intersect(prev, curr, edge))
            clipped.append(curr)
        elif edge(prev):
            # Leaving, add intersection
            clipped.append(intersect(prev, curr, edge))
    return clipped

def intersect(p1, p2, edge):
    x1, y1 = p1
    x2, y2 = p2
    # Determine intersection with edge
    if edge == inside_left:
        x = xmin
        y = y1 + (y2 - y1)*(xmin - x1)/(x2 - x1)
    elif edge == inside_right:
        x = xmax
        y = y1 + (y2 - y1)*(xmax - x1)/(x2 - x1)
    elif edge == inside_bottom:
        y = ymin
        x = x1 + (x2 - x1)*(ymin - y1)/(y2 - y1)
    elif edge == inside_top:
        y = ymax
        x = x1 + (x2 - x1)*(ymax - y1)/(y2 - y1)
    return (x, y)

# Edge functions
inside_left   = lambda p: p[0] >= xmin
inside_right  = lambda p: p[0] <= xmax
inside_bottom = lambda p: p[1] >= ymin
inside_top    = lambda p: p[1] <= ymax

# Apply clipping against all four edges
clipped_poly = polygon
for edge in [inside_left, inside_right, inside_bottom, inside_top]:
    clipped_poly = clip_polygon(clipped_poly, edge)

# Draw clipped polygon in red
t.color("red")
t.penup()
t.goto(clipped_poly[0])
t.pendown()
for pt in clipped_poly[1:]:
    t.goto(pt)
t.goto(clipped_poly[0])
t.penup()

screen.mainloop()

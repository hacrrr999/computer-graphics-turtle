import turtle

# Initialize screen
screen = turtle.Screen()
screen.title("Line Clipping: Cohen-Sutherland vs Liang-Barsky")
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# Clipping window
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

# Sample lines to clip
lines = [
    (-150, 0, 150, 0),     # Horizontal
    (0, -150, 0, 150),     # Vertical
    (-150, -150, 150, 150),# Diagonal
    (150, -150, -150, 150) # Another diagonal
]

# Draw original lines (blue)
t.color("blue")
t.pensize(1)
for x1, y1, x2, y2 in lines:
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
t.penup()

# ------------------ COHEN-SUTHERLAND ------------------

INSIDE, LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 4, 8

def compute_out_code(x, y):
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code

def cohen_sutherland_clip(x1, y1, x2, y2):
    out1 = compute_out_code(x1, y1)
    out2 = compute_out_code(x2, y2)
    accept = False

    while True:
        if out1 == 0 and out2 == 0:  # Both inside
            accept = True
            break
        elif out1 & out2 != 0:       # Logical AND != 0, trivially reject
            break
        else:
            # At least one endpoint outside
            outcode_out = out1 if out1 != 0 else out2
            if outcode_out & TOP:
                x = x1 + (x2 - x1)*(ymax - y1)/(y2 - y1)
                y = ymax
            elif outcode_out & BOTTOM:
                x = x1 + (x2 - x1)*(ymin - y1)/(y2 - y1)
                y = ymin
            elif outcode_out & RIGHT:
                y = y1 + (y2 - y1)*(xmax - x1)/(x2 - x1)
                x = xmax
            elif outcode_out & LEFT:
                y = y1 + (y2 - y1)*(xmin - x1)/(x2 - x1)
                x = xmin
            # Replace outside point
            if outcode_out == out1:
                x1, y1 = x, y
                out1 = compute_out_code(x1, y1)
            else:
                x2, y2 = x, y
                out2 = compute_out_code(x2, y2)
    if accept:
        return x1, y1, x2, y2
    return None

# Draw Cohen-Sutherland clipped lines (red)
t.color("red")
for x1, y1, x2, y2 in lines:
    clipped = cohen_sutherland_clip(x1, y1, x2, y2)
    if clipped:
        t.penup()
        t.goto(clipped[0], clipped[1])
        t.pendown()
        t.goto(clipped[2], clipped[3])
t.penup()

# ------------------ LIANG-BARSKY ------------------

def liang_barsky_clip(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]
    u1, u2 = 0, 1

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None
        else:
            u = q[i]/p[i]
            if p[i] < 0:
                u1 = max(u1, u)
            else:
                u2 = min(u2, u)
    if u1 > u2:
        return None
    nx1 = x1 + u1*dx
    ny1 = y1 + u1*dy
    nx2 = x1 + u2*dx
    ny2 = y1 + u2*dy
    return nx1, ny1, nx2, ny2

# Draw Liang-Barsky clipped lines (green)
t.color("green")
t.pensize(2)
for x1, y1, x2, y2 in lines:
    clipped = liang_barsky_clip(x1, y1, x2, y2)
    if clipped:
        t.penup()
        t.goto(clipped[0], clipped[1])
        t.pendown()
        t.goto(clipped[2], clipped[3])
t.penup()

screen.mainloop()

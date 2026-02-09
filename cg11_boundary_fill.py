import turtle

# Initialize screen
screen = turtle.Screen()
screen.title("Boundary Fill Algorithm")
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# Draw a rectangle (boundary)
t.goto(-100, -50)
t.pendown()
t.pensize(2)
t.color("black")
t.begin_fill()
for _ in range(2):
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
t.end_fill()
t.penup()


# Simplified boundary fill function
def boundary_fill(x, y, fill_color, boundary_color):
    t.goto(x, y)
    t.dot(4, fill_color)

    # Move in 4 directions
    directions = [(4, 0), (-4, 0), (0, 4), (0, -4)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        t.goto(nx, ny)
        # Check if not boundary before filling
        if t.color()[0] != boundary_color:
            boundary_fill(nx, ny, fill_color, boundary_color)


# Start filling inside the rectangle
# WARNING: Recursive turtle filling is slow; use a small area
# boundary_fill(0, 0, "yellow", "black")

screen.mainloop()

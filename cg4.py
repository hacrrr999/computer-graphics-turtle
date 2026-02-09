import turtle

# Initialize graphics window
screen = turtle.Screen()
screen.title("Grid of Points and Lines")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.color("black")
t.width(1)

grid_size = 200     # size of the grid
step = 40           # distance between lines/points

# Draw vertical lines
for x in range(-grid_size, grid_size + 1, step):
    t.penup()
    t.goto(x, -grid_size)
    t.pendown()
    t.goto(x, grid_size)

# Draw horizontal lines
for y in range(-grid_size, grid_size + 1, step):
    t.penup()
    t.goto(-grid_size, y)
    t.pendown()
    t.goto(grid_size, y)

# Draw points at intersections
t.penup()
for x in range(-grid_size, grid_size + 1, step):
    for y in range(-grid_size, grid_size + 1, step):
        t.goto(x, y)
        t.dot(4, "black")

t.hideturtle()

# Keep window open
screen.exitonclick()
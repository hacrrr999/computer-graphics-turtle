import turtle

# Initialize screen
screen = turtle.Screen()
screen.title("Flood Fill Algorithm")
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# Draw a rectangle as the region
t.goto(-100, -50)
t.pendown()
t.fillcolor("white")
t.begin_fill()
for _ in range(2):
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
t.end_fill()
t.penup()


# Flood fill function (recursive)
def flood_fill(x, y, fill_color, boundary_color):
    t.goto(x, y)
    current_color = screen.getcanvas().winfo_rgb(screen.bgcolor())

    # Only fill if current pixel is background (white)
    if screen.getcanvas().winfo_rgb(screen.bgcolor()) != screen.getcanvas().winfo_rgb(fill_color):
        t.goto(x, y)
        t.dot(4, fill_color)
        flood_fill(x + 4, y, fill_color, boundary_color)
        flood_fill(x - 4, y, fill_color, boundary_color)
        flood_fill(x, y + 4, fill_color, boundary_color)
        flood_fill(x, y - 4, fill_color, boundary_color)


# Start filling inside rectangle
# flood_fill(0, 0, "yellow", "black")  # Note: Turtle has limitations with pixel-level fill

screen.exitonclick()

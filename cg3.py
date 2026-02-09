import turtle

# Initialize the graphics window
screen = turtle.Screen()
screen.title("Plotting a Pixel")
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.penup()

# Coordinates of the pixel
x, y = 50, 50

# Move to the pixel position and plot it
t.goto(x, y)
t.dot(5, "black")   # dot(size, color)

# Keep the window open
screen.exitonclick()
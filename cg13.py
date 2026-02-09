import turtle
import math

# Initialize screen
screen = turtle.Screen()
screen.title("2D Transformations")
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# Function to draw polygon given list of points
def draw_polygon(points, color="black"):
    t.color(color)
    t.penup()
    t.goto(points[0])
    t.pendown()
    for pt in points[1:]:
        t.goto(pt)
    t.goto(points[0])
    t.penup()

# Original polygon
polygon = [(-50, -50), (-50, 50), (50, 50), (50, -50)]
draw_polygon(polygon, "black")

# 1️⃣ Translation
tx, ty = 100, 50
translated_polygon = [(x + tx, y + ty) for x, y in polygon]
draw_polygon(translated_polygon, "red")

# 2️⃣ Scaling (about origin)
sx, sy = 1.5, 0.5
scaled_polygon = [(x * sx, y * sy) for x, y in polygon]
draw_polygon(scaled_polygon, "green")

# 3️⃣ Rotation (about origin)
angle = 45  # degrees
theta = math.radians(angle)
rotated_polygon = [(x*math.cos(theta) - y*math.sin(theta),
                    x*math.sin(theta) + y*math.cos(theta)) for x, y in polygon]
draw_polygon(rotated_polygon, "blue")

# 4️⃣ Reflection
# About X-axis
reflected_x = [(x, -y) for x, y in polygon]
draw_polygon(reflected_x, "orange")
# About Y-axis
reflected_y = [(-x, y) for x, y in polygon]
draw_polygon(reflected_y, "purple")

# 5️⃣ Shearing
# Shear along X-axis
shx = 1.0
sheared_x = [(x + shx*y, y) for x, y in polygon]
draw_polygon(sheared_x, "brown")
# Shear along Y-axis
shy = 0.5
sheared_y = [(x, y + shy*x) for x, y in polygon]
draw_polygon(sheared_y, "pink")

screen.mainloop()

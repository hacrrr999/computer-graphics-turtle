import turtle
import math

# Initialize screen
screen = turtle.Screen()
screen.title("Composite 2D Transformation using Homogeneous Coordinates")
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# Function to draw polygon
def draw_polygon(points, color="black"):
    t.color(color)
    t.penup()
    t.goto(points[0][0], points[0][1])
    t.pendown()
    for pt in points[1:]:
        t.goto(pt[0], pt[1])
    t.goto(points[0][0], points[0][1])
    t.penup()

# Matrix multiplication
def multiply_matrix_vector(M, P):
    x = M[0][0]*P[0] + M[0][1]*P[1] + M[0][2]*P[2]
    y = M[1][0]*P[0] + M[1][1]*P[1] + M[1][2]*P[2]
    w = M[2][0]*P[0] + M[2][1]*P[1] + M[2][2]*P[2]
    return [x/w, y/w, 1]

# Original polygon (as homogeneous coordinates [x, y, 1])
polygon = [[-50, -50, 1], [-50, 50, 1], [50, 50, 1], [50, -50, 1]]

draw_polygon(polygon, "black")  # Original polygon

# --- Composite Transformation ---
# 1️⃣ Translation by (tx, ty)
tx, ty = 100, 50
T = [
    [1, 0, tx],
    [0, 1, ty],
    [0, 0, 1]
]

# 2️⃣ Scaling by (sx, sy)
sx, sy = 1.5, 0.5
S = [
    [sx, 0, 0],
    [0, sy, 0],
    [0, 0, 1]
]

# 3️⃣ Rotation by theta degrees
theta = math.radians(45)
R = [
    [math.cos(theta), -math.sin(theta), 0],
    [math.sin(theta), math.cos(theta), 0],
    [0, 0, 1]
]

# 4️⃣ Shearing along X-axis
shx = 0.5
Sh = [
    [1, shx, 0],
    [0, 1, 0],
    [0, 0, 1]
]

# --- Combine matrices (Composite: T * R * S * Sh)
def multiply_matrices(A, B):
    result = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            result[i][j] = sum(A[i][k]*B[k][j] for k in range(3))
    return result

# Composite matrix
M = multiply_matrices(T, multiply_matrices(R, multiply_matrices(S, Sh)))

# Apply composite transformation
transformed_polygon = [multiply_matrix_vector(M, pt) for pt in polygon]

draw_polygon(transformed_polygon, "red")  # Transformed polygon

screen.mainloop()

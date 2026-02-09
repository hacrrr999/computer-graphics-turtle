import turtle
import math

# Initialize screen
screen = turtle.Screen()
screen.title("Sequential 3D Transformations on Cube")
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# Draw 3D polygon projected to 2D
def draw_3d_polygon(points, color="black"):
    t.color(color)
    t.penup()
    x, y, z = points[0]
    t.goto(x, y)
    t.pendown()
    for pt in points[1:]:
        x, y, z = pt
        t.goto(x, y)
    t.goto(points[0][0], points[0][1])
    t.penup()

# Matrix-vector multiplication (4x4 * 4x1)
def multiply_matrix_vector(M, P):
    return [sum(M[i][j]*P[j] for j in range(4)) for i in range(4)]

# Apply transformation matrix to points
def apply_transformation(points, M):
    transformed = []
    for x, y, z in points:
        vec = [x, y, z, 1]
        tx, ty, tz, tw = multiply_matrix_vector(M, vec)
        transformed.append((tx/tw, ty/tw, tz/tw))
    return transformed

# Multiply two 4x4 matrices
def multiply_matrices(A, B):
    result = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            result[i][j] = sum(A[i][k]*B[k][j] for k in range(4))
    return result

# Original cube vertices
cube = [
    (-50, -50, -50), (-50, -50, 50),
    (-50, 50, -50), (-50, 50, 50),
    (50, -50, -50), (50, -50, 50),
    (50, 50, -50), (50, 50, 50)
]

# Cube edges
edges = [
    (0,1),(0,2),(0,4),(1,3),(1,5),
    (2,3),(2,6),(3,7),(4,5),(4,6),
    (5,7),(6,7)
]

# Draw original cube
for start, end in edges:
    draw_3d_polygon([cube[start], cube[end]], "black")

# --- Define Transformation Matrices ---

# Translation
tx, ty, tz = 100, 50, 30
T = [
    [1,0,0,tx],
    [0,1,0,ty],
    [0,0,1,tz],
    [0,0,0,1]
]

# Scaling
sx, sy, sz = 1.2, 1.5, 0.8
S = [
    [sx,0,0,0],
    [0,sy,0,0],
    [0,0,sz,0],
    [0,0,0,1]
]

# Rotation about X-axis
theta_x = math.radians(30)
Rx = [
    [1,0,0,0],
    [0,math.cos(theta_x), -math.sin(theta_x),0],
    [0,math.sin(theta_x), math.cos(theta_x),0],
    [0,0,0,1]
]

# Rotation about Y-axis
theta_y = math.radians(45)
Ry = [
    [math.cos(theta_y),0,math.sin(theta_y),0],
    [0,1,0,0],
    [-math.sin(theta_y),0,math.cos(theta_y),0],
    [0,0,0,1]
]

# Reflection about XY-plane (z -> -z)
Ref = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,-1,0],
    [0,0,0,1]
]

# --- Apply Sequential Transformations ---

# Start with original cube
current_cube = cube.copy()

# 1️⃣ Scaling
current_cube = apply_transformation(current_cube, S)

# 2️⃣ Rotation X
current_cube = apply_transformation(current_cube, Rx)

# 3️⃣ Rotation Y
current_cube = apply_transformation(current_cube, Ry)

# 4️⃣ Reflection
current_cube = apply_transformation(current_cube, Ref)

# 5️⃣ Translation
current_cube = apply_transformation(current_cube, T)

# Draw transformed cube
for start, end in edges:
    draw_3d_polygon([current_cube[start], current_cube[end]], "red")

screen.mainloop()
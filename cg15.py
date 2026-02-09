import turtle
import math

# Initialize screen
screen = turtle.Screen()
screen.title("3D Transformations")
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# Function to draw a 3D polygon (projected to 2D)
def draw_3d_polygon(points, color="black"):
    t.color(color)
    t.penup()
    x, y, z = points[0]
    # Orthographic projection (ignore z)
    t.goto(x, y)
    t.pendown()
    for pt in points[1:]:
        x, y, z = pt
        t.goto(x, y)
    t.goto(points[0][0], points[0][1])
    t.penup()

# Function to multiply 4x4 matrix with 4x1 vector
def multiply_matrix_vector(M, P):
    result = [0, 0, 0, 0]
    for i in range(4):
        result[i] = sum(M[i][j]*P[j] for j in range(4))
    return result

# Function to apply a transformation matrix to a list of points
def apply_transformation(points, M):
    transformed = []
    for x, y, z in points:
        vec = [x, y, z, 1]
        tx, ty, tz, tw = multiply_matrix_vector(M, vec)
        transformed.append((tx/tw, ty/tw, tz/tw))
    return transformed

# Original 3D cube (8 vertices)
cube = [
    (-50, -50, -50),
    (-50, -50,  50),
    (-50,  50, -50),
    (-50,  50,  50),
    ( 50, -50, -50),
    ( 50, -50,  50),
    ( 50,  50, -50),
    ( 50,  50,  50)
]

# Draw original cube edges
edges = [
    (0,1),(0,2),(0,4),(1,3),(1,5),
    (2,3),(2,6),(3,7),(4,5),(4,6),
    (5,7),(6,7)
]

# Draw original cube
for start, end in edges:
    draw_3d_polygon([cube[start], cube[end]], "black")

# --- 1️⃣ Translation ---
tx, ty, tz = 100, 50, 30
T = [
    [1,0,0,tx],
    [0,1,0,ty],
    [0,0,1,tz],
    [0,0,0,1]
]

# --- 2️⃣ Scaling ---
sx, sy, sz = 1.5, 0.5, 2
S = [
    [sx,0,0,0],
    [0,sy,0,0],
    [0,0,sz,0],
    [0,0,0,1]
]

# --- 3️⃣ Rotation about X-axis ---
theta = math.radians(30)
Rx = [
    [1,0,0,0],
    [0,math.cos(theta), -math.sin(theta),0],
    [0,math.sin(theta), math.cos(theta),0],
    [0,0,0,1]
]

# --- 4️⃣ Rotation about Y-axis ---
theta = math.radians(45)
Ry = [
    [math.cos(theta),0,math.sin(theta),0],
    [0,1,0,0],
    [-math.sin(theta),0,math.cos(theta),0],
    [0,0,0,1]
]

# --- 5️⃣ Reflection about XY-plane (z -> -z) ---
Ref = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,-1,0],
    [0,0,0,1]
]

# --- Combine transformations: Translation * RotationY * RotationX * Scaling * Reflection
def multiply_matrices(A, B):
    result = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            result[i][j] = sum(A[i][k]*B[k][j] for k in range(4))
    return result

# Composite matrix
M = multiply_matrices(T, multiply_matrices(Ry, multiply_matrices(Rx, multiply_matrices(S, Ref))))

# Apply transformation
transformed_cube = apply_transformation(cube, M)

# Draw transformed cube edges
for start, end in edges:
    draw_3d_polygon([transformed_cube[start], transformed_cube[end]], "red")

screen.mainloop()

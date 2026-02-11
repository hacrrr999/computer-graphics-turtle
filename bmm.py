import turtle
import math

# ================= Screen =================
screen = turtle.Screen()
screen.title("BMM Dynamic Flag Hoisting Scene")
screen.setup(width=1150, height=720)
screen.bgcolor("skyblue")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

wind = 6
rope_pull = 0

# ============== Helpers ==============
def draw_pole():
    p = turtle.Turtle()
    p.hideturtle(); p.speed(0)

    # pole
    p.penup(); p.goto(-360, -220); p.pendown()
    p.color("#5a3a1b"); p.pensize(12)
    p.goto(-360, 240)

    # rope
    p.pensize(2); p.color("#e0d5a8")
    for y in range(-200, 230, 18):
        p.penup(); p.goto(-358, y + rope_pull); p.pendown()
        p.goto(-348, y + 8 + rope_pull)

# draw a person with simple motion
def draw_person(x, y, arm_up=False):
    pen.penup(); pen.goto(x, y); pen.color("black"); pen.pendown()

    # body
    pen.goto(x, y - 70)

    # legs
    pen.penup(); pen.goto(x, y - 70); pen.pendown(); pen.goto(x - 20, y - 110)
    pen.penup(); pen.goto(x, y - 70); pen.pendown(); pen.goto(x + 20, y - 110)

    # arms
    pen.penup(); pen.goto(x, y - 25); pen.pendown()
    if arm_up:
        pen.goto(x + 50, y + 10)
    else:
        pen.goto(x + 40, y - 10)

    pen.penup(); pen.goto(x, y - 25); pen.pendown(); pen.goto(x - 35, y - 10)

    # head
    pen.penup(); pen.goto(x, y + 8); pen.pendown(); pen.circle(12)

# torch symbol
def draw_torch(x, y):
    pen.penup(); pen.goto(x, y); pen.pendown()
    pen.color("#5a3a1b"); pen.begin_fill()
    for _ in range(2):
        pen.forward(14); pen.right(90); pen.forward(60); pen.right(90)
    pen.end_fill()

    pen.penup(); pen.goto(x - 8, y + 10); pen.color("orange")
    pen.begin_fill(); pen.circle(14); pen.end_fill()

    pen.penup(); pen.goto(x - 4, y + 18); pen.color("yellow")
    pen.begin_fill(); pen.circle(8); pen.end_fill()

# ============== Flag ==============
def draw_flag(offset):
    pen.clear()

    # green field
    pen.color("#006600")
    pen.penup(); pen.goto(-350, 150 + rope_pull); pen.pendown(); pen.begin_fill()

    for x in range(0, 701, 20):
        y = math.sin((x + offset) / 40) * wind
        pen.goto(-350 + x, 150 + y + rope_pull)

    for x in range(700, -1, -20):
        y = math.sin((x + offset) / 40) * wind
        pen.goto(-350 + x, -150 + y + rope_pull)

    pen.end_fill()

    # white strip
    pen.color("white"); pen.begin_fill()
    for x in range(0, 121, 20):
        y = math.sin((x + offset) / 40) * wind
        pen.goto(-350 + x, 150 + y + rope_pull)

    for x in range(120, -1, -20):
        y = math.sin((x + offset) / 40) * wind
        pen.goto(-350 + x, -150 + y + rope_pull)
    pen.end_fill()

    # crescent
    pen.penup(); pen.goto(80, 10 + rope_pull); pen.color("white"); pen.pendown()
    pen.begin_fill(); pen.circle(95); pen.end_fill()

    pen.penup(); pen.goto(110, 35 + rope_pull); pen.color("#006600"); pen.pendown()
    pen.begin_fill(); pen.circle(70); pen.end_fill()

    # star
    pen.penup(); pen.goto(170, 70 + rope_pull); pen.color("yellow"); pen.pendown()
    pen.begin_fill()
    for i in range(5):
        pen.forward(60); pen.right(144)
    pen.end_fill()

    # torch logo
    draw_torch(-240, 10 + rope_pull)

# ============== Static Text ==============
title = turtle.Turtle(); title.hideturtle(); title.penup(); title.goto(0, 260)
title.write("ବିଜୟ ମୁକ୍ତି ମୋର୍ଚ୍ଚା - BMM", align="center", font=("Arial", 24, "bold"))

footer = turtle.Turtle(); footer.hideturtle(); footer.penup(); footer.goto(0, -260)
footer.write("न्याय • पहचान • प्रगति   |   Founded: 2018", align="center", font=("Arial", 18, "bold"))

# ============== Controls ==============
def faster():
    global wind; wind = min(wind + 2, 16)

def slower():
    global wind; wind = max(wind - 2, 2)

screen.listen(); screen.onkey(faster, "Up"); screen.onkey(slower, "Down")

# ============== Draw Scene ==============
draw_pole()

# ============== Animation ==============
offset = 0
while True:
    # simulate pulling rope
    rope_pull = int(math.sin(offset/30) * 8)

    draw_flag(offset)

    # people
    draw_person(-400, -40, arm_up=True)   # Bijaya Babu main
    draw_person(-460, -50, arm_up=False)  # supporter 1
    draw_person(-320, -45, arm_up=False)  # supporter 2

    offset += 6
    screen.update()

screen.mainloop()
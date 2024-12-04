import turtle
import time
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Animated Heart")

# Turtle setup
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)  # Fastest speed
pen.pensize(2)

# Function to draw a line with animation
def draw_line(x1, y1, x2, y2):
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    
    # Calculate distance and animation steps
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    steps = int(distance / 5)  # Adjust for animation speed
    
    for _ in range(steps):
        pen.color(random.choice(["red", "pink", "magenta"]))  # Random color
        pen.goto(pen.xcor() + (x2 - x1) / steps, pen.ycor() + (y2 - y1) / steps)
        time.sleep(0.01)  # Adjust for animation speed

# Heart coordinates (adjust as needed)
heart_points = [
    (0, 100),
    (50, 150),
    (100, 100),
    (100, 0),
    (50, -50),
    (0, 0),
    (-50, -50),
    (-100, 0),
    (-100, 100),
    (-50, 150),
    (0, 100)
]

# Draw the heart with animated lines
while True:
    for i in range(len(heart_points) - 1):
        draw_line(*heart_points[i], *heart_points[i + 1])
    
    pen.clear()  # Clear the screen for the next animation
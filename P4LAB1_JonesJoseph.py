# Joseph Jones
# 11/7/2024
# P4LAB1
# Write a turtle graphics programs that draws a triangle and a square using loops

import turtle
win =turtle.Screen()
t =turtle.Turtle()
win.bgcolor("black")

# Add some display options
t.pensize(10)
t.pencolor("green")
t.shape("turtle")

# While loop to make square
num =0

while num < 4:
    t.forward(150)
    t.right(90)
    num += 1
print("While loop ends")

# For loop to draw a triangle
for tr in range(0,3):
    t.forward(150)
    t.left(120)
print("For loop ends")

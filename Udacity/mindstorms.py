# MindStorms.py
# Uses Turtle to draw a square, circle and triangle
import turtle
window = turtle.Screen()
window.bgcolor("red")
def draw_square():
    frank = turtle.Turtle()
    frank.shape("triangle")
    frank.color("blue")
    frank.speed(1)
    i=0
    while i<=3:
        frank.forward(90)
        frank.right(90)
        i=i+1
draw_square()
def draw_circle():
    mustard = turtle.Turtle()
    mustard.shape("arrow")
    mustard.color("green")
    mustard.circle(60)
draw_circle()
def draw_triangle():
    ketchup = turtle.Turtle()
    ketchup.shape("turtle")
    ketchup.color("yellow")
    ketchup.speed(2)
    ketchup.right(-45)
    t=0
    while t<=2:
        ketchup.bk(90)
        ketchup.right(120)
        t=t+1
draw_triangle()
window.exitonclick()

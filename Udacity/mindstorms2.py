import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("triangle")
    brad.color("blue")
    brad.speed(10)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()

draw_art()

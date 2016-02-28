import turtle

def draw_petal(some_turtle):
    for i in range(1,2):
        some_turtle.forward(100)
        some_turtle.left(35)
        some_turtle.forward(100)
        some_turtle.left(145)
        some_turtle.forward(100)
        some_turtle.left(35)
        some_turtle.forward(100)
        some_turtle.left(145)
def draw_flower():
    window = turtle.Screen()
    window.bgcolor("grey")
    Jack = turtle.Turtle()
    Jack.shape("circle")
    Jack.color("blue")
    Jack.speed(10)
    for i in range(1,37):
        draw_petal(Jack)
        Jack.right(10)
    Jack.goto(0,-300)
    window.exitonclick()

draw_flower()

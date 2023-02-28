import turtle

turtle.speed(0)
turtle.bgcolor('black')

for i in range (6):
    for colours in ['magenta', 'red', 'green', 'cyan', 'blue', 'yellow', 'orange', 'pink', 'purple', 'white' ]:
        turtle.color(colours)
        turtle.pensize(2)
        turtle.left(12)
        turtle.forward (200)
        turtle.left(90)
        turtle.forward (200)
        turtle.left(90)
        turtle.forward (200)
        turtle.left(90)
        turtle.forward (200)
        turtle.left(90)

turtle.hideturtle()

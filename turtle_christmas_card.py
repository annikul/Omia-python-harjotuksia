import turtle

turtle.bgcolor('darkblue')

def draw_rectangle(turtle, color, x, y, widght, height): # Voit nimetä miksi haluat. Tähän tulee ne mitä tarvitset puuta varten.
    turtle.penup() # kynä ei piirrä kokoaikaa
    turtle.color(color) # Raja värit
    turtle.fillcolor(color) # Täyte väri
    turtle.goto(x,y) # Sijainti
    turtle.pendown()
    turtle.begin_fill()

    for i in range (2):     # Koodi menee 2 kertaa
        turtle.forward(width)
        turtle.

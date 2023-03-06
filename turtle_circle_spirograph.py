# Otetaan käyttöön turtle kirjasto
import turtle

# Valitaan taustaväri, kynän koko, piirtämisnopeus(0)nopein (ei animaatiota) NÄiden järjestykselllä ei ole väliä
turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(0)

# Ympyröiden tekeminen
for i in range(6):  # Ensimmäinen loop
    for colours in ['magenta', 'red', 'green', 'blue', 'yellow', 'orange', 'pink', 'purple', 'white' ]: # Ensimmäisen loopin sisään toinen loop, joka tekee ympyrät eri värisiksi listan avulla.
        turtle.color(colours)
        turtle.circle(100) # Ympyrän koko
        turtle.left(10) # Ympyrän kulma

turtle.hideturtle()

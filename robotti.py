# Robotti
import turtle as t

def rectangle (horizontal, vertical, color, teksti):
    t.pendown()
    t.pensize(1)
    t.color (color)
    t.begin_fill()
    print(str(t.pos()) + " = " + teksti)

    for counter in range (1, 3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup ()
t.speed ('fastest')
# t.bgcolor ('Dodger blue')
t.bgcolor ('black')

# Tulostetaan ikkunan koordinaatit
print('ikkunan korkeus =',t.window_height())
print('ikkunan leveys =',t.window_width())

# Oikea jalkaterä
t.goto(-30, -90)
rectangle (50, 20, '#ed265b', 'teksti')

# Vasen jalkaterät
t.goto(-100, -90)
rectangle (50, 20, '#02e3f7', 'teksti')

# Oikea jalka
t.goto(-25, -30)
rectangle (15, 60, 'blue', 'oikea jalka')

# Vasen jalka
t.goto(-55, -30)
rectangle(-15 ,60, 'darkblue', 'vasen jalka')

# Oikea käsivarsi
t.goto(0, 90)
rectangle (60, 15, 'purple', 'oikea kasivarsi')

# Oikea käsi
t.goto (50, 200)
rectangle (15, 125, 'purple', 'oikea kasi')

# Vasen käsivarsi
t.goto(-130, 90)
rectangle (60, 15, '#8d51f5', 'vasen kasivarsi')

# Vasen käsi
t.goto (-145, 200)
rectangle (15, 125, '#8d51f5', 'vasen kasi')

# Kaula 
t.goto(-50, 120)
rectangle (10, 30, 'orange', 'kaula')

# Ruumis
t.goto(-40, -60)

# set the fillcolor
t.fillcolor('#d2fa0a')
  
# start the filling color
t.begin_fill()
  
# drawing the circle of radius r
t.circle(80)
  
# ending the filling of the color
t.end_fill()

# Pää
t.goto(-85, 170)
rectangle (80, 50, '#02f727', 'pää')

# Hiukset
t.goto(-50, 200)
rectangle (2, 30, '#1002d1', 'keskel_hiukset')

t.goto(-53, 181)
rectangle (2, 10, '#07fad1', 'vasen_hiukset')

t.goto(-56, 190)
rectangle (2, 10, '#07fad1', 'vasen_hiukset')

t.goto(-43, 181)
rectangle (2, 10, '#fa07cd', 'oikea_hiukset')

t.goto(-40, 190)
rectangle (2, 10, '#fa07cd', 'oikea_hiukset')

# Silmät
while True:
    # Tämä pitäisi tehdä funktiossa kuten tehtävä esimerkissä
    # eli piirtää yhdellä kertaa silmät
    t.goto(-60, 160)
    rectangle (30, 10, 'white','silmien valkoinen tausta')
    t.goto(-55, 155)
    rectangle (5, 5, 'black','silmat')
    t.goto(-40, 155)
    rectangle (5, 5, 'black','silmat')

    # Suu
    t.goto(-70, 130)
    rectangle (50, 5, '#f7021f', 'suu')

    t.goto(-70, 140)
    rectangle (5, 10, '#f7021f', 'suu')

    t.goto(-25, 140)
    rectangle (5, 10, '#f7021f', 'suu')

   # Kyltti
    t.goto (-345, 360)
    rectangle (600, 157, 'white', 'kyltti')

    # E kirjain
    t.goto(-330, 330)
    rectangle (10, 90, 'black', 'E')

    t.goto(-320, 330)
    rectangle (40, 10, 'black', 'E_yla_viiva')

    t.goto(-320, 290)
    rectangle (40, 10, 'black', 'E_keski_viiva')

    t.goto(-320, 250)
    rectangle (40, 10, 'black', 'E_ala_viiva')

    # N kirjain
    t.goto(-250, 330)
    rectangle (10, 90, 'black', 'N_vas')

    t.goto(-240, 330)
    rectangle (10, 10, 'black', 'N_vas')

    t.goto(-235, 320)
    rectangle (10, 10, 'black', 'N_vas')

    t.goto(-230, 310)
    rectangle (10, 10, 'black', 'N_vas')

    t.goto(-225, 300)
    rectangle (10, 10, 'black', 'N_vas')

    t.goto(-220, 290)
    rectangle (10, 10, 'black', 'N_vas')

    t.goto(-215, 280)
    rectangle (10, 10, 'black', 'N_vas')

    t.goto(-210, 270)
    rectangle (10, 10, 'black', 'N_vas')

    t.goto(-205, 260)
    rectangle (10, 10, 'black', 'N_vas')

    t.goto(-200, 250)
    rectangle (10, 10, 'black', 'N_vas')

    t.goto(-200, 330)
    rectangle (10, 80, 'black', 'N_vas')

    # T kirjain
    t.goto(-140, 330)
    rectangle (60, 10, 'black', 'T_yla_viiva')

    t.goto(-115, 330)
    rectangle (10, 90, 'black', 'T_viiva')

    # U kirjain
    t.goto(-60, 330)
    rectangle (10, 90, 'black', 'U_vas_viiva')

    t.goto(-60, 250)
    rectangle (50, 10, 'black', 'U_ala_viiva')

    t.goto(-10, 330)
    rectangle (10, 90, 'black', 'U_oik_viiva')

    # L kirjain
    t.goto(30, 330)
    rectangle (10, 80, 'black', 'L_viiva')

    t.goto(30, 250)
    rectangle (60, 10, 'black', 'L')

    # E kirjain
    t.goto(110, 330)
    rectangle (10, 90, 'black', 'E')

    t.goto(120, 330)
    rectangle (40, 10, 'black', 'E_viiva')

    t.goto(120, 290)
    rectangle (40, 10, 'black', 'E_viiva')

    t.goto(120, 250)
    rectangle (40, 10, 'black', 'E_viiva')

    # !-merkki
    t.goto(200, 340)
    rectangle (20, 60, 'black', '!')

    t.goto(200, 260)
    rectangle (20, 20, 'black', 'piste') 

    t.hideturtle()

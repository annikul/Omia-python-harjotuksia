from random import randint

# Asetetaan muuttujat
vastaus = randint(0,100)
peli = False

# Printataan pelin alku
print('*' * 20)
print ('Tervetuloa pelaamaan!')
print('*' * 20)

# Kysytään haluaako käyttäjä pelata ja asetetaan peli-muuttuja sen mukaan
kysymys = input('Haluatko pelata? (kyllä/ei): ')
if kysymys == 'kyllä':
    peli = True
    print('Aloitetaan peli!')
    print('Arvaa oikea luku!')
else:
    print('Nähdään pian!')

while peli == True:
    arvaus = int(input('Syötä arvauksesi: '))
    if arvaus < vastaus:
        print('Oikea vastaus on suurempi!')
    elif arvaus > vastaus:
        print('Oikea vastaus on pienempi!')
    else:
        print('Arvasit oikein!')
        peli = False
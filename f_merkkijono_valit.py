# f käyttämistä merkkijonossa, tyhjän rivin tekeminen. Helpompi tapa.

nimi = "Teppo Testaaja"
ika = 20
taito1 = "python"
taso1 = "aloittelija"
taito2 = "java"
taso2 = "veteraani"
taito3 = "ohjelmointi"
taso3 = "puoliammattilainen"
ala = 2000
yla = 3000

print(f"nimeni on {nimi}, olen {ika}-vuotias")
print() # Tyhjän rivin merkki
print("taitoihini kuuluvat")
print(f' - {taito1} ({taso1})')
print(f' - {taito2} ({taso2})')
print(f' - {taito3} ({taso3})\n') # \n tyhjän rivin merkki
print(f'haen työtä, josta maksetaan palkkaa {ala}-{yla} euroa kuussa') # helpompi tapa
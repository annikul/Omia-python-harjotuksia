class Koodari:

    # Oliomuodostin, argumentteina etu- ja sukunimi, self viittaa luokasta luotavaan olioon
    def __init__(self, etunimi, sukunimi):
        self.etunimi = etunimi
        self.sukunimi = sukunimi
    
    # Metodi joka tulostaa ruudulle viestin
    def oma_kehu(self):
        print('Mä oon', self.etunimi, 'ja oon paras koodari ikinä')

# Luodaan koodari1-olio muodostimella
koodari1 = Koodari('Jonne', 'Janttari')

# Kutsutaan koodari1:n oma_kehu-metodia
koodari1.oma_kehu()
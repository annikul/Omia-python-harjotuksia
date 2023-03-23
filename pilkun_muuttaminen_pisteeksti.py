# Pilkun muuttaminen pisteeksi automaattisesti
# Jos vaikka käyttäjältä kysytään painoa ja käyttäjä vastaa 
# 65,5 niin replace(',', '.') tämä muuttaa sen automaattisesti 65.5 eikä niin 
# että tulee virheilmoitus ja käyttäjä joutuu uudestaan laittamaan luvun
# Tässä yksinkertainen esimerkki

txt = '65,5'

x = txt.replace(',', '.')

print(x)
# Pilkun muuttaminen pisteeksi automaattisesti
# Jos vaikka käyttäjältä kysytään painoa ja käyttäjä vastaa 
# 65,5 niin replace(',', '.') tämä muuttaa sen automaattisesti 65.5 eikä niin 
# että tulee virheilmoitus ja käyttäjä joutuu uudestaan laittamaan luvun
# Tässä yksinkertainen esimerkki

txt = '65,5'

x = txt.replace(',', '.')

print(x)


# Toinen esimerkki. Muuttaa molempien luvut pisteille

txt = '1,75 cm paino 65,5 kg'

x = txt.replace(',', '.')

print(x)

# Opi lukemaan syntax
# string.replace(oldvalue, newvalue, count)
# string on muuttuja eli teksti (käyttäjä syöttää)
# replace on metodi
# sitten tulee sulkuihin 3 arvoa eli käyttäjä syöttää ne
# oldvalue on vanha arvo (pakollinen)
# newvalue on uusi arvo (pakollinen)
# count on määrä (vapaaehtonen)
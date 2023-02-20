pituus = float(input('Anna pituus: '))
paino = float(input('Anna paino: '))

pituus = pituus / 100
bmi = paino /pituus ** 2

print(f'Painoindeksi on {bmi}')
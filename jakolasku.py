pituus = 172.5
paino = 68.55

# Painoindeki lasketaan jakamalla paino pituuden neliöllä
# Pituus ilmoitetaan kaavassa metreinä
bmi = paino / (pituus / 100) ** 2

print(f'Painoindeksi on {bmi}')
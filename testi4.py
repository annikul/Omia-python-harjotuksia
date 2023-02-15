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

print(f'nimeni on {nimi}, olen {ika} -vuotias \n') # saat välin näkymään terminaalissa kun laitat \n

print('taitoihini kuuluvat')
print(f' - {taito1} ({taso1})')
print(f' - {taito2} ({taso2})')
print(f' - {taito3} ({taso3})')

print('haen työtä, josta maksetaan palkkaa ' + str(ala) + ('-') + str(yla) + ' euroa kuussa' )

# Tarvittaessa jätä väli hipsu ja teksti väli esim: 'euroa = 2000-3000euroa  ja ' euroa = 2000-3000 euroa.
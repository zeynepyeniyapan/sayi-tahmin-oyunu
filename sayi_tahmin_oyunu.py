import random

sayi = random.randint(1,20)
hak = 4

while hak > 0:
    hak -= 1
    tahmin = int(input('Tahminin: '))
    if (tahmin == sayi):
        print('Tahminin doğru')
        break
    elif hak == 0:
        print('Doğru sayı: ')
        print(sayi)
    elif tahmin>sayi :
        print('Fazla oldu')
        continue
    elif tahmin<sayi:
        print('Az oldu')
        continue
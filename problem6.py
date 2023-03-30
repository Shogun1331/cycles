n = int(input('Сколько хотите накопить? '))

summa = 0


while summa < n:
 vznos = int(input('Взнос: '))
 summa = summa + vznos


print('Поздравляю! Вы накопили ', summa, 'сомов!')

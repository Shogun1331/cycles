q = 0
w = 0
while q < 1000:
    q += w
    w += 1
    print(w)

q = int(input('Vvedite chislo: '))

while q < 100:
    w = int(input('cislo:  '))
    w += 1
    if w > 100:
        print('Вы ввели число больше 100')



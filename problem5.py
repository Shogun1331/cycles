from random import random
N = 1000
q = 0
for i in range(N):
    if int(random()*100) % 2 == 0:
        q += 1
print("%.2f%%" % (q / N * 100))

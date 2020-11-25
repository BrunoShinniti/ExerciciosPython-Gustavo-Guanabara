#contagem regressiva

from time import sleep

for c in range(10, -1, -1):
    sleep(1)
    print('{} ...'.format(c))

print('Happy New Year!!!')

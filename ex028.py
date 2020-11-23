#fazer o pc pensar em um numero de 1 a 5 e o usuario tenta adivinhar

from random import randint

num = int(input('Digite um número: '))
n = randint(1, 5)

if num == n:
    print('Ambos escolheram o número {}. Parabéns!!!'.format(num))
else:
    print('O pc escolheu o número {}. E você escolheu o número {}. You Lose!!!'.format(n, num))

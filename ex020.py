#sortear a ordem de apresentação de 4 alunos

from random import shuffle

a = 'bruno'
b = 'toto'
c = 'andrea'
d = 'kitty'

list = [a, b, c, d]
shuffle(list)

print('A ordem de apresentação será {}.'.format(list))

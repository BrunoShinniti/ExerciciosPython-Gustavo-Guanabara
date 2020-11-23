#calculo da hipotenusa

from math import hypot

adj = float(input('Digite o valor da Adjacente:'))
cat = float(input('Digite o valor do Cateto Oposto:'))
hip = hypot(adj, cat)
print('O valor da hipotenusa é {:.2f}'.format(hip))

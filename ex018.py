#leia um angulo qualquer e calcula seno, cosseno e tangente

from math import radians, sin, cos, tan

ang = float(input('Digite um angulo: '))
rad = radians(ang)

seno = sin(rad)
coss = cos(rad)
tang = tan(rad)

print('Seno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}'.format(seno, coss, tang))

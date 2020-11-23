# crie um algoritmo que leia um numero e mostre o dobro, triplo e raiz quadrada

n = int(input('Digite um número: '))
print('O dobro do valor {} é {}.'.format(n, (n*2)))
print('O triplo do valor {} é {}.'.format(n, (n*3)))
print('A raiz quadradada do valor {} é {:.2f}.'.format(n, (n**(1/2))))

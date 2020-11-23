#programa q leia 3 tamanho de retas e verifica se forma um triangulo

r1 = int(input('Valor da primeira reta: '))
r2 = int(input('Valor da segunda reta: '))
r3 = int(input('Valor da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('é possível formar um triângulo!')
else:
    print('não é possível formar um triângulo')

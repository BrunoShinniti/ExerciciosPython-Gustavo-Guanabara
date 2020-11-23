#melhorar ex035
#dizer qual tipo de triangulo será formado: euquilátero, isósceles ou escaleno

r1 = int(input('Valor da primeira reta: '))
r2 = int(input('Valor da segunda reta: '))
r3 = int(input('Valor da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('é possível formar um triângulo!')

    if r1 == r2 and r2 == r3:
        print('O triângulo é Equilátero!')
    if (r1 == r2 and r2 != r3) or (r1 == r3 and r3 != r2) or (r2 == r3 and r3 != r1):
        print('O triângulo é Isósceles!')
    if r1 != r2 and r1 != r3 and r2 != r3:
        print('O triângulo é Escaleno!')

else:
    print('não é possível formar um triângulo')


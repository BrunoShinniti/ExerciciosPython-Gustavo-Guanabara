# leia de 0 a 9999 e mostre cada digito separado

numero = input('Digite um numero de 0 a 9999: ')

print('unidade:{}' .format(numero[len(numero)-1]))
print('dezena:{}'.format(numero[len(numero)-2]))
print('centena:{}'.format(numero[len(numero)-3]))
print('milhar:{}'.format(numero[len(numero)-4]))

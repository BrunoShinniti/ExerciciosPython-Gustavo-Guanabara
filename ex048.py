#calcule a soma entre todos os numeros impares multiplos de 3 entre 1 ate 500

valor = 0

for c in range(0, 500, 3):

    if c % 2 == 1:
        valor = valor + c

print('A soma dos numeros impares sao: {}'.format(valor))

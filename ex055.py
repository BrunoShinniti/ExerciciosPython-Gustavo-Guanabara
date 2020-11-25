#ler o peso de 5 pessoas. Mostrar qual foi o maior e o menor peso

maior = 0
menor = 9999

for count in range(1, 6):
    peso = float(input('Digite o {}º peso: '.format(count)))

    if peso >= maior:
        maior = peso
    elif peso <= menor:
        menor = peso

print('O maior peso e {}.'.format(maior))
print('O menor peso eh {}.'.format(menor))

#leia o ano de nascimento de 7 pessoas e diga quantas atingiram a maioridade e quantas nao

from datetime import date

data = date.today()
maior = 0
menor = 0

for count in range(1, 8):
    calc = 0
    num = int(input('Digite o ano da {}º pessoa: '.format(count)))
    calc = data.year - num

    if calc >= 21:
        maior = maior + 1
    else:
        menor = menor + 1

print('Maior de idade{}'.format(maior))
print('Menor de idade{}'.format(menor))

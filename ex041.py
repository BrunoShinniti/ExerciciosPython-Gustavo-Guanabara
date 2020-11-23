#leia ano de nascimento de atleta e mostre sua categoria
#ate 9 anos mirim
#ate 14 anos infantil
#ate 19 anos junior
#ate 20 anos senior
#acima Master

from datetime import date

data = date.today()
nasc = int(input('Insira o ano de nascimento: '))
dif = data.year - nasc

if (dif <= 9):
    print('Categoria Mirim')
if (dif > 9) and (dif <= 14):
    print('Categoria Infantil')
if (dif > 14) and (dif <= 19):
    print('Categoria Junior')
if (dif > 19) and (dif <= 20):
    print('Categoria Sênior')
if (dif > 20):
    print('Categoria Master')

#verificar se um ano é bissexto

ano = int(input('Digite o ano a ser verificado: '))

calc = ano // 1 % 100

if calc % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('É Bissexto!')
else:
    print('Não é Bissexto!')

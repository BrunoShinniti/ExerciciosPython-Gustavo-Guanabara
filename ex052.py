#verificar se e numero primo

print('Verificando se eh numero primo!')
num = int(input('Digite o numero a ser verificado: '))

res = 0

if num == 0 or num == 1:
    print('nao eh numero primo.')

else:
    for c in range(2, num):

        if num % c == 0:
            res = 1

    if res == 0:
        print('eh numero primo.')
    else:
        print('nao eh numero primo.')

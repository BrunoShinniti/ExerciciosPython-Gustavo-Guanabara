#ler primeiro termo e a razao de uma PA. mostre os 10 primeiros termos dessa progressao

print('Progressao Aritmetica')
pt = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))

for c in range(0, 10):

    print('{}'.format(pt), end='...')
    pt = pt + razao

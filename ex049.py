#fazer uma tabuada utilizando For

num = int(input('Numero da tabuada: '))

for c in range(1, 11):
    print('{} x {} = {}'.format(c, num, num*c))

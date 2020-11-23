#leia 2 números inteiros, e compare: qual é maior, menor ou se são iguais

pvalor = int(input('Digite o primeiro valor: '))
svalor = int(input('Digite o segundo valor: '))

if pvalor > svalor:
    print('O primeiro valor ({}) é o maior!'.format(pvalor))

if pvalor < svalor:
    print('O segundo valor ({}) é o maior!'.format(svalor))

if pvalor == svalor:
    print('Os valores ({}) são iguais!'.format(pvalor))

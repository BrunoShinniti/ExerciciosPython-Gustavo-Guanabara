#programa que leia um numero inteiro e fale se é par ou impar

num = int(input('Digite um número: '))

if num % 2 == 0:
    print('O número {} é par.'.format(num))
else:
    print('O número {} é ímpar'.format(num))

#ler um numero inteiro, e usuário escolhe a base de conversão (binario, octal, hexadecimal)
numero = int(input('Digite um número inteiro: '))

escolha = int(input('Escolha a base de conversão:\n(1) - Binário\n(2) - Octal\n(3) - Hexadecimal\n...'))

if escolha == 1:
    print('{} convertido para binario {}'.format(numero, bin(numero)))
elif escolha == 2:
    print('{} convertido para octal {}'.format(numero, oct(numero)))
elif escolha == 3:
    print('{} convertido para hexadecimal {}'.format(numero, hex(numero)))
else:
    print('Escolha inválida!')

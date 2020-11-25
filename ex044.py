# calcular o valor a ser pago por um produto
# a vista (dinheiro) - 10% de desconto
# a vista (cartão) - 5% de desconto
# ate 2x no cartão - preço normal
# ate 3x ou mais no cartão - 20% de juros

valor = float(input('Digite o valor do produto R$ '))

escolha = int(input('Digite uma opção:\n[1] - A Vista no Dinheiro\n[2] - A Vista no Cartão\n[3] - 2x no Cartão\n[4] - 3x no Cartão\nEscolha......'))

if escolha == 1:
    print('Total de R$ {:.2f}.'.format(valor * .90))
elif escolha == 2:
    print('Total de R$ {:.2f}.'.format(valor * .95))
elif escolha == 3:
    print('Total de R$ {:.2f}.'.format(valor))
elif escolha == 4:
    print('Total de R$ {:.2f}.'.format(valor * 1.2))

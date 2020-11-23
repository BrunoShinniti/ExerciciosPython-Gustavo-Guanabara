# programa que calcula aluguel de carro, KM rodados e dias alugados
# Dia custa R$60 e R$0,15 por km rodado

dias = int(input('Digite quantos dias foram alugados.'))
km = float(input('Digite quantos Km foram rodados.'))

totaldias = dias * 60
totalkm = km * 0.15

print('Para tantos dias deu R${:.2f}\nPara tantos km deu R${:.2f}\nSendo o valor total de R${:.2f}.'.format(totaldias, totalkm, (totalkm+totaldias)))

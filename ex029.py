#ler a velocidade de um carro, se ultrapasar 80km/h multa- multa cobrada R$7,00 a cada km excedente

km = float(input('Digite o Km/h ultrapassado no radar: '))

if km > 80:
    print('O valor ultrapassado no radar foi de {}km/h e você tomou um MULTA no valor de R${:.2f}.'.format(km, (km-80)*7))
else:
    print('Dentro do limite da velocidade. Sem multa.')

#calculo de viagem. Se viagem até 200km, cobrar R$ 0,50. Acima de 200km cobrar R$0,45

km = int(input('Digite a quilometragem da viagem.'))

if km > 200:
    print('O custo da viagem para {}km é de R${:.2f}'.format(km, (km*.45)))
if km <= 200:
    print('O custo da viagem para {}km é de R${:.2f}'.format(km, (km * .50)))

# Calcular o IMC de alguem
# 18.5 - abaixo do peso
# 18,5 - 25 - peso ideal
# 25 - 30 - sobrepeso
# 30 - 40 - obesidade
# 40+ obesidade morbida

peso = float(input('Qual seu peso(kl)? '))
altura = float(input('Qual sua altura(m)? '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('IMC = {:.2f}......Abaixo do peso!'.format(imc))
if 18.5 <= imc < 25:
    print('IMC = {:.2f}......Peso Ideal!'.format(imc))
if 25 <= imc < 30:
    print('IMC = {:.2f}......Sobrepeso!'.format(imc))
if 30 <= imc < 40:
    print('IMC = {:.2f}......Obesidade'.format(imc))
if imc >= 40:
    print('IMC = {:.2f}......Obesidade Mórbida'.format(imc))

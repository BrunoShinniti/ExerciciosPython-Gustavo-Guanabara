#programa para aprovar emprestimo para compra de 1 casa
#perguntar o valor da casa, o salario do comprador e quantos anos vai pagar
#calcular o valor da prestação mensal sabendo que não pode exceder de 30% do salário ou então o emprestimo será negado

valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
ano = int(input('Quantos anos vai pagar? '))

trinta = salario * .3
meses = ano * 12
resultado = valor / meses

if trinta > resultado:
    print('Empréstimo Aprovado com Sucesso!\nValor da prestação é R${:.2f}'.format(resultado))
else:
    print('Empréstimo Recusado.\nValor da prestação é R${:.2f}'.format(resultado))

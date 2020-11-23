# digite salario. Acima de R$1250 aumento de 10%. Menor aumento de 15%.

salario = float(input('Digite o salário: R$'))

if salario > 1250:
    print('O salário de R${:.2f} aumentou para R${:.2f}.'.format(salario, (salario*1.1)))
else:
    print('O salário de R${:.2f} aumentou para R${:.2f}.'.format(salario, (salario*1.15)))

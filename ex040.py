#leia duas notas de um aluno e tire a media
#abaixo de 5 reprovado
#entre 5 e 6.9 recuperação
#7+ aprovado

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('A média é de {:.2f}. Reprovado! '.format(media))

elif (media >= 5) and (media < 7):
    print('A média é de {}. Recuperação!'.format(media))

elif (media >= 7):
    print('A média é de {}. Aprovado!'.format(media))

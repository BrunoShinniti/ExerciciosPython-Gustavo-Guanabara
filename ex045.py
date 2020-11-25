# programa de jakenpô

from random import randint

pc = randint(1, 3)

escolha = int(input('[1] - Papel\n[2] - Tesoura\n[3] - Pedra\nChoose your destiny....'))

if pc == 1 and escolha == 3:
    print('Pc escolheu Papel e você escolheu Pedra.\nVocê Perdeu!')

elif pc == 2 and escolha == 3:
    print('Pc escolheu Tesoura e você escolheu Pedra.\nVocê Ganhou!')

elif pc == 3 and escolha == 3:
    print('Pc escolheu Pedra e você escolheu Pedra.\nEmpatou!')

elif pc == 1 and escolha == 2:
    print('Pc escolheu Papel e você escolheu Tesoura.\nVocê Ganhou!!')

elif pc == 2 and escolha == 2:
    print('Pc escolheu Tesoura e você escolheu Tesoura.\nEmpatou!')

elif pc == 3 and escolha == 2:
    print('Pc escolheu Pedra e você escolheu Tesoura.\nVocê Perdeu!')

elif pc == 1 and escolha == 1:
    print('Pc escolheu Papel e você escolheu Papel.\nEmpatou!')

elif pc == 2 and escolha == 1:
    print('Pc escolheu Tesoura e você escolheu Papel.\nVocê Perdeu!')

elif pc == 3 and escolha == 1:
    print('Pc escolheu Pedra e você escolheu Papel.\n Você Ganhou!')

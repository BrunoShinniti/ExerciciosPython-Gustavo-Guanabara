#ler ano de nascimento e informe: se ainda vai se alistar - já é hora de se alistar ou já passou do tempo
#deverá apresentar a diferença de tempo - ou +

from datetime import date

nasc = int(input('Qual seu ano de nascimento? '))
data = date.today()

dif = data.year - nasc

if dif < 18:
    print('O tempo que falta para se alistar é de {}ano(s).'.format(18-dif))

elif dif == 18:
    print('Está no ano de se alistar!')

elif dif > 18:
    print('Já passou {} ano(s) do tempo de se alistar'.format(dif-18))

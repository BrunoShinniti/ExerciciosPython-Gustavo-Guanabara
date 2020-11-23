#leia o nome de uma cidade e diz se começa com Santo

cidade = input('Digite o nome de uma cidade: ').upper().strip().split()
print('SANTO' == cidade[0])

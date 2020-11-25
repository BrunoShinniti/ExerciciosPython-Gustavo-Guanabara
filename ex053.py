#verificar se uma palavra eh palindromo
res = 0
count = 0
palavra = input('Digite a palavra: ').strip().upper().replace(' ', '')

for c in range((len(palavra)-1), -1, -1):

    if palavra[c] == palavra[count]:
        res += 0
        count += 1

    else:
        res += 1
        count += 1

if res == 0:
    print('Palindromo')
else:
    print('NOT')

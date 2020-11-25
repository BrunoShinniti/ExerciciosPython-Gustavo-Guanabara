#ler 6 numeros inteiros, mostrar a soma dos que forem pares e desconsiderar impares

soma=0

for c in range(0, 6):
    num = int(input('Digite numeros: '))

    if num % 2 == 0:
        soma = soma + num

print(soma)

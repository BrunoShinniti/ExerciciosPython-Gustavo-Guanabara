# um programa que leia a largura e a altura de uma  parede em metros, calcule a sua area e a quantidade de tinta
# necessaria para pintar - cada litro de tinta pinta uma area de 2m²

largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))
quadrado = largura * altura
litro = quadrado / 2

print('O total é de {}m² e será necessário {:.2f} Litros de tinta para pintar a parede.'.format(quadrado, litro))

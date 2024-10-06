# Faça um programa que leia a largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

# QUE VIAGEM FOI ESSA???? - CÓDIGO HORRÍVEL, DEIXADO PARA A POSTERIDADE...
# p = float(input('Digite a largura da parede: '))
# ap = p ** 2
# print(f'A área da parede é: {ap} m²')
# t = 2 ** 2 / ap
# print(f'Você vai gastar: {t} lts. de tinta')

# E ESSE ENTÃO...VERGONHOSO...
# p = float(input('Digite a largura da parede: '))
# ap = p * 4
# print(f'A parede tem {ap} m²')
# t = 2 ** 2 / ap
# print(f'Você consegue pintar uma área de: {t}  m²')

# Código Professor

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
tinta = area / 2
print('Sua parede tem a dimensão de {}m x {}m e sua área é de: {} m²'.format(larg, alt, area))
print('Para pintar sua parede você vai precisar de {} lts de tinta'.format(tinta))

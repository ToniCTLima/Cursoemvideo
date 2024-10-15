# Faça um programa que leia o comprimento do cateto adjacente e do cateto oposto de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'A hipotenusa mede: {hi}')

# Outra forma de resolução

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digiteo comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa mede: {:.2f}'.format(hi))


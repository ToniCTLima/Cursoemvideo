# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# import math
# cos = float(input('Digite um ângulo para o cosseno: '),math.cos())
# sen = float(input('Digite um ângulo para o seno: '))
# tang = float(input('Digite um ângulo para a tangente: '))
# print('O valor do cosseno é: {}, o valor do seno é: {} e o valor da tangente é: {}'.format(cos, sen, tang),math)

# Resolução do professor: O grau têm que ser representado em radiano.

import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))

cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))

tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))







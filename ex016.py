# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira

import math
num = float(input('Digite um número: '))
int = math.trunc(num)
print(f'O número {num} tem a parte inteira: {int}')

# Outras forma de resolver

from math import trunc
num = float(input('Digite um número: '))
int = trunc(num)
print(f'O valor digitado foi: {num} e sua porção inteira é: {int}'.format(num, trunc(num)))


num = float(input('Digite um número: '))
print('O valor digitado {}, tem sua parte inteira: {}'.format(num, int(num)))
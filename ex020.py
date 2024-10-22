# Faça um programa que leia o nome de quatro alunos e mostre a ordem sorteada.

import random
# Primeira solução errada, usei o random.choice, ao invés do random.shuffle
# n1 = input('Digite o primeiro nome para o sorteio: ')
# n2 = input('Digite o segundo nome para o sorteio: ')
# n3 = input('Digite o terceiro nome para o sorteio: ')
# n4 = input('Digite o quarto nome para o sorteio: ')
# lista = [n1, n2, n3, n4]
# escolhido = random.choice(lista)
# print(f'O primeiro sorteado é: {escolhido}')


# Outra forma. Erro pois usei o random.choice, ao invés do random.shuffle

# n1 = input('Digite o primeiro nome: ')
# n2 = input('Digite o segundo nome: ')
# lista = [n1, n2, n3, n4]
# escolhido = random.choice(lista)
# print('O escolhido foi: {}'.format(escolhido))

# Solução do professor:

n1 = str(input('Primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)


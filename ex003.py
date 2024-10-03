# Desafio 003 Crie um script que leia dois números e tente mostrar a soma entre eles.

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
s = n1+n2
print('A soma de: {}'.format(n1), 'e {}'.format(n2), 'é: {}'.format(s))

# Outra forma de simplificar o código:

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('A soma de: {} e {}, é igual a: {}'.format(n1, n2, s))


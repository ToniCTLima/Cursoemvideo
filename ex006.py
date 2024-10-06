#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada
n1 = int(input('Digite um número: '))
print('O número é: {}!'.format(n1))
print('O dobro desse número é: {}!'.format(n1*2))
print('O triplo desse número é: {}!'.format(n1*3))
print('A raiz quadrada desse número é: {}!'.format(n1**(1/2)))

#outra forma do código
n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}. A raiz quadrada de {} é igual a {:.2f}'.format(n, t, n, r))

# Usando o f-string para substituir o .format

n = int(input('Digite um número: '))
dobro = n*2
triplo = n*3
raiz = n**(1/2)
print(f'O dobro de {n} é: {dobro}')
print(f'O triplo de {n} é: {triplo}')
print(f'A raiz quadrada de {n} é igual a: {raiz}')

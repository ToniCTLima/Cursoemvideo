# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.

n = int(input('Digite um número: '))
r1 = n * 1
r2 = n * 2
r3 = n * 3
r4=  n * 4
r5 = n * 5
r6 = n * 6
r7 = n * 7
r8 = n * 8
r9 = n * 9
r10 = n * 10
print(f'A tabuada do número: {n} é:',r1 ,r2, r3, r4, r5, r6, r7, r8, r9, r10)

# Outra forma...bem grande do código, muitas variáveis

n = int(input('Digite um número para ver sua tabuada: '))
t1 = n * 1
t2 = n * 2
t3 = n * 3
t4 = n * 4
t5 = n * 5
t6 = n * 6
t7 = n * 7
t8 = n * 8
t9 = n * 9
t10 = n * 10
print(f'{n} x 1 =',t1)
print(f'{n} x 2 =',t2)
print(f'{n} x 3 =',t3)
print(f'{n} x 4 =',t4)
print(f'{n} x 5 =',t5)
print(f'{n} x 6 =',t6)
print(f'{n} x 7 =',t7)
print(f'{n} x 8 =',t8)
print(f'{n} x 9 =',t9)
print(f'{n} x 10 =',t10)

# Código do Professor - usando .format

num = int(input('Digite um número para ver sua tabuada: '))
print('{} x {} = {}'.format(num, 1, num*1))
print('{} x {} = {}'.format(num, 2, num*2))
print('{} x {} = {}'.format(num, 3, num*3))
print('{} x {} = {}'.format(num, 4, num*4))
print('{} x {} = {}'.format(num, 5, num*5))
print('{} x {} = {}'.format(num, 6, num*6))
print('{} x {} = {}'.format(num, 7, num*7))
print('{} x {} = {}'.format(num, 8, num*8))
print('{} x {} = {}'.format(num, 9, num*9))
print('{} x {} = {}'.format(num, 10, num*10))


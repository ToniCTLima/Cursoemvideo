# Tipos primitivos
# int = números inteiros: 1, 2, 3...
# float = números reais, com casa decimal: 1.2, 2.0...
# bool = boleanos, valores lógicos, True ou False
# str = string, ou linha de texto
#from idlelib.configdialog import is_int

n1 = int(input('Digite um valor: ')) # int colocado na linha de comando, "transforma" toda a linha em um número inteiro.
print(type(n1)) # com a função type, mostramos qual o tipo da variável, no caso vai mostrar que é um número inteiro.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
print('A soma de: {} mais {}, é igual a: {}'.format(n1, n2, soma))

# Desafio 1: Crie um programa que leia d dois números e mostre a soma entre eles.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma de {}, mais {} é igual a: {}'.format(n1, n2, s))

# Desafio 2: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
x = input('Digite algo: ')
print(x.isnumeric()) # utilizando is..., conseguimos ver o tipo da variável.
print(x.isalpha())
print(x.isalnum())

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print(f'A soma de: {n1} mais {n2} é igual a {s}')

x = input('Digite algo: ')
print(x,'é alfa-numérico?',(x.isalnum())) # colocando a variável 'x' logo depois do print, mostramos na tela o que o usuário 'inputou' na variável 'x'
print(x,'é numérico?',(x.isnumeric()))
print(x,'é um digito?',(x.isdigit()))
print(x,'está maiúsculo?',(x.isupper()))

n = float(input('Digite algo: '))
print(n,type(n))

n1 = bool(input('Digite algo: '))
print(n1, type(n1))

n2 = int(input('Digite algo: ' ))
print(n2, type(n2))

n3 = str(input('Digite algo: '))
print(n3, type(n3))










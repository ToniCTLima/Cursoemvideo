# Faça um algoritmo que leia o preço de um produto e mostre o novo preço, com 5% de desconto.

pr = float(input('Digite o preço do produto: R$ '))
de = (pr * 0.95)
print(f'O novo preço com 5% de desconto é: R$ {de:.2f}')

# Código do Professor:

preço = float(input('Qual o preço do produto? R$ '))
novo = preço - (preço * 5 / 100)
print('O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar: R$ {:.2f}'.format(preço, novo))
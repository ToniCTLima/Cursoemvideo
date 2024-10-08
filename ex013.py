# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

sa = float(input('Digite seu salário: R$ '))
au = sa * (1 + 0.15)
print(f'Seu salário de R$ {sa}, com o aumento de 15% passará a ser: R$ {au:.2f}')

# Outra forma do código:

sa = float(input('Digite seu salário atual: R$ '))
au = sa + (sa * 15 / 100)
print(f'Seu novo salário com 15% de aumenta passará a ser: R$ {au:.2f}')

# Outro exercício:
# Um produto pago a vista recebe 10% de desconto e parcelado recebe um aumento de 12%

pr = float(input('Digite o valor do produto: R$ '))
avista = pr - (pr * 10 / 100) # com desconto de 10%
aprazo = pr + (pr * 12 / 100) # com aumento de 12%
print(f'O valor do produto com 10% de desconto é: R$ {avista}')
print(f'o vaor do produto com aumento de 12% é: R$ {aprazo}')



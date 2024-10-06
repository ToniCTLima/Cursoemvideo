# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere o dólar a $ 3.27

r = float(input('Digite o valor para a conversão em dólares: R$ '))
dol = r * 5.46
dol2 = r / 5.46
print(f'Você pode comprar: $ {dol} dólares.')
print(f'Seu {r} Real está valendo: $ {dol2:.1f} dólares.')
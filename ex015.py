# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelo quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado.

km = float(input('Digite a quilometragem rodada: '))
dias = int(input('Digite a quantidade de dias que o carro esteve alugado: '))
preço = dias * 60 + km * 0.15
print('O veículo rodou por: {} km e por um total de {} dias.'.format(km, dias))
print('O preço total a pagar é: R$ {}'.format(preço))
# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros

n1 = float(input('Digite uma medida em metros para ser convertida em cm e mm: '))
cm = n1 * 100
mm = n1 * 1000
print(f'O valor de {n1} metros em centímetros é: {cm} cm e em milímetros é: {mm} mm')

# Código do Professor:

medida = float(input('Digite uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))

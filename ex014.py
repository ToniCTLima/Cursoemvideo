# Escreva um programa que converta uma temperatura digitada em C° e converta para F°.and

c = float(input('Digite a temperatura em Celsius para ser convertida em Farenheit: ')) 
f = 9 * c /5 + 32
print('A temperatura {}c°, corresponde a {}f°'.format(c, f))

# Convertendo de F° para C°

f = float(input('Digite a temperatura: '))
c = (f - 32)  * 5 / 9
print('A temperatuta {} f°, corresponde a {} c°'.format(f, c))

           

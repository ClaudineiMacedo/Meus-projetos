#Desenvolva um programa que leia o comprimentos de três retas e
#diga ao usuario se ele pode ou não forma um triangulo.
r1 = float(input('primeira segmento: '))
r2 = float(input('segunda segmento: '))
r3 = float(input('terceira segmento: '))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 +r2:
    print('Os segmentos podem formar um TRIANGULO')
else:
    print('Os segmentos não pode formar um TRIANGULO')
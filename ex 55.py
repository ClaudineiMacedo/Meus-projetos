#Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi maior eo menor peso lido.
maior = 0
menor = 0
for pessoas in range(1,6):
    peso = float(input('Peso da {}º pessoa: '.format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}KG'.format(maior))
print('O menor peso lido foi {}KG'.format(menor))
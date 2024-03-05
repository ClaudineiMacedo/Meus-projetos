# Faça um programa que leia três numeros e mostre qual é maior e menor.
a = int(input('primeiro numero: '))
b = int(input('segundo numero: '))
c = int(input('terceiro numero: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor numero é {}'.format(menor))
print('O maior numero é {}'.format(maior))
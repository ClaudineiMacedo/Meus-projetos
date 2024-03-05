#Crie um programa que leia o ano de nascimento de setes pessoas. No final, mostre quantas pessoas ainda não atingiram
#o maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
for pessoas in range(1,8):
    nasc = int(input('Em que ano a pessoa nasceu: '))
    idade = atual - nasc
    if idade >= 18:
        print('Essa pessoa é maior de idade {}'.format(idade))
    else:
        print('Essa pessoa é menor e de idade {}'.format(idade))
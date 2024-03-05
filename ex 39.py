#Faça um programa que leia o an de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai si
#alistar ao serviço militar, se é hora de se alistar ou se ja passou o tempo do alistamento.
#Seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo de alistamento.
from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Voçê tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voçê deveria ter se alistado a {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
#Crie um programa que faça o computador jogar JOKENPÔ com voçê.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'tesoura')
computador = randint(0, 2)
print('''Suas Opção:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!!!')
sleep(1)
print('<>' * 13)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('<>' * 13)
if computador == 0: #computador jogou PEDRA

   if jogador == 0:
       print('EMPATE')
   elif jogador == 1:
       print('JOGADOR VENCEU')
   elif jogador == 2:
        print('COMPUTADOR VENCEU')
   else:
       print('JOGADA INVALIDA')
elif computador == 1: #computador jogou PAPEL

    if jogador == 0:
       print('COMPUTADOR VENCEU')
    elif jogador == 1:
       print('EMPATE')
    elif jogador == 2:
       print('JOGADOR VENCEU')
    else:
        print('JOGADA INVALIDA')
elif computador == 2: #computador jogou TESOURA

    if jogador == 0:
       print('JOGADOR VENCEU')
    elif jogador == 1:
       print('COMPUTADOR VENCEU')
    elif jogador == 2:
       print('EMPATE')
    else:
        print('JOGADA INVALIDA')
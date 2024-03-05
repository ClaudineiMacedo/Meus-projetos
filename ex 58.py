#Melhore o jogo do desafio 28 onde o jogador vai 'pensar' em um numero de 0 á 10. Só que agora o jogador vai tentar
#adivinhar até acertar, mostrando no final quantos palpites foram nessecários para vencer.
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em numero entre 0 e 10.')
print('Sera que voçê consegui adivinha qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos... tente mais uma')
print('ACERTOU!!!')
print('Voçê conseguiu acertar depois de {} tentativas'.format(palpites))
#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifícios, indo de 10 até 0,
#coom uma pausa de 1 segundo entre eles.
from time import sleep
import emoji
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize("FELIZ ANO NOVO !!!!:party_popper: :sparkler:"))


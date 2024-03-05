#Escreva um programa que leia 2 numeros inteiros e compare-os, monstrado na tela uma menssagem:
#  O primeiro valor é maior
#  O segundo valor é maior
#  Não existe valor maior os dois não iguais.
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('O primeiro valor é maior que o segundo')
elif n2 > n1:
    print('O segundo valor é maior que o primeiro')
else:
    print('Não existe valor maior, os dois são iguais.')
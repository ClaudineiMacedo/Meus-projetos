#Crie um programa que leia um numero inteiro e mostre se ele é numero PAR ou IMPAR.
num = int(input('Digite um numero: '))
resultado = num % 2
if resultado == 0:
    print('O numero {} é PAR'.format(num))
else:
    print('O numero {} é IMPAR'.format(num))

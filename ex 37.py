#Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual vai ser a base de
#conversão. 1 para binario - 2 para octal - 3 para hexadecimal
num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das base de conversão:
[ 1 ] Converter para BINARIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('sua opção: '))
if opção == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida, tente novamente')
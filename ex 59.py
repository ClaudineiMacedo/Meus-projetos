#Crie um programa que leia dois valores e mostre um menu como ao lado da tela: Seu programa devera realizar a operção
#solicitada em cada caso. [1]SOMAR, [2]MULTIPLICAR, [3]MAIOR [4]NOVOS NÚMEROS, [5]SAIR DO PROGRAMA.
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA''')
    opção = int(input('>>>>>>>>>>>>>Qual sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} = {}'.format(n1, n2, soma))
    elif opção == 2:
        multiplicacao = n1 * n2
        print('O resultado de {} * {} = {}'.format(n1, n2, multiplicacao))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os numeros novamente:')
        n1 = int(input('Digite o primeiro: '))
        n2 = int(input('Digite o segundo: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção invalida, tente novamente!')
    print('=-=' * 12)
print('FIM DO PROGRAMA!!!')
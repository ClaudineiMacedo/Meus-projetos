n1 = int(input('\033[0;35mDigite um numero: '))
n2 = int(input('\033[0;31mDigite outro numero: '))
s = n1 + n2
print('A soma entre \033[0;32m{}\033[m e \033[0;36m{}\033[m vale \033[1;31m{}\033[m'.format(n1, n2, s))
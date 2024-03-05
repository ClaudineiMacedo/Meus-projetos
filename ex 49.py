#Mostre a tabuada de um numero que usuário escolher, só que agora utilizando um laço for.
n = int(input('digite um numero: '))
for c in range(1, 11):
    print('{} * {} = {}'.format(n, c, n*c))

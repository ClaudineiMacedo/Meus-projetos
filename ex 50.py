#Desenvolva um programa que leia seis numeros inteiros e monstre a soma apenas daquele que forem pares. se o valor
#digitado for imparr, desconsidere-o.
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Voçê informou {} PARES valores e a soma foi {}'.format(cont, soma))
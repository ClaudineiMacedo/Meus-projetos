#Desenvolva um programa que leia primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
#progressão.
print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
primeiro = int(input('primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{} -> '.format(c), end='')
print('ACABOU')
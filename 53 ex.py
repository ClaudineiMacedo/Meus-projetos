#crie um programa que leia uma frase qualquer e diga se ela é um palindramo, desconsidere os peços.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDRAMO!')
else:
    print('A frase digitada não é um PALÍNDRAMO')
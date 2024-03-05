import random
import time
computador = random.randint(0,5)
num = int(input('Digite um numero que o computador esta pensando de 0 a 5 ? '))
print('PROCESSANDO...')
time.sleep(2)
if computador==num:
    print('voçê acertou PARABENS!')
else:
    print('voçê errou, pensei {} e voçê digitou {}'.format(computador,num))
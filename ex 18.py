import math
ângulo = float(input('Digite o ângulo que deseja: '))
seno = math.sin(math.radians(ângulo))
print('o ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ãngulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))
import math
co = float(input('O comprimento do cateto oposto: '))
ca = float(input('O comprimento do cateto adjacente: '))
hi = math.hypot(co,ca)
print('A hipotenusa é {:.2f}'.format(hi))

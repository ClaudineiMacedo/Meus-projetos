speed = float(input('qual sua velocidade atual do carro? '))
if speed > 80:
    print('MULTADO!')
    multa = (speed - 80) * 7
    print(' voçê excedeu o limite permitido de 80km/h, foi altuado em R$ {:.2f}'.format(multa))
else:
    print('PAREBENS, dirija com segurança')
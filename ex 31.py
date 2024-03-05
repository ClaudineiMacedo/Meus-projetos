#Densolva um programa pergunte sua viagem em KM. Calcule o preço da passagem, cobrando R$0.50 por km para
#viagem de até 200km e R$0.45 para viagens mais longas.
distancia = float(input('qual a distancia da sua viagem? '))
print('Voçê vai começar uma viagem de {:.2f}km .'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O valor da sua passagem vai custar R${:.2f}'.format(preco))
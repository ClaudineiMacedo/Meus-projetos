#Elabore um programa que calcule o valor a ser pago por um produto, considerando o preço normal e condição de pagamento:
# - á vista dinheiro/cheque: 10% de desconto
# - á vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format(' LOJAS CARVALHO '))
preço = float(input('Preços das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual á opção de forma de pagamento? '))
if opção == 1:
    total = preço - (preço * 0.10)
elif opção == 2:
    total = preço - (preço * 0.05)
    print('sua compra R${:.2f} com desconto fica R${:.2f}'.format(preço, total))
elif opção == 3:
    total = preço / 2
    print('sua compra no valor R${:.2f} ficou parcelado em 2x de R${:.2f} sem desconto!'.format(preço, total))
elif opção == 4:
    total = preço + (preço * 0.20)
    parc = int(input('Quantas parcelas? '))
    parcelas = total / parc
    print('sua compra parcelada em {}x de R${:.2f} COM JUROS'.format(parc, parcelas))

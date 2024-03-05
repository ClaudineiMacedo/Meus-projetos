#Escreva um programa para aprovar o emprestimo bancario para o comprador de uma casa. O programa vai pergunta o salario
#do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ele não pode execeder
#30% do salario ou entaõ o emprestimo ser nagado.

casa = float(input('Digite o valor da casa:R$ '))
salario = float(input('Quanto voçê recebe por mês:R$ '))
anos = int(input('Em quantos anos pretende pagar a casa: '))
prestação = casa / (anos * 12)

if prestação <= salario * 0.3:
    print('Seu imprestimo foi aprovado com a parcela, de R${:.2f} com percelas fixa ate a quitação do imovel.'
          .format(prestação))
else:
    print('Seu imprestimo foi negado devido a parcela, ser maior que 30% do seu salario de {:.3f}'.format(salario))
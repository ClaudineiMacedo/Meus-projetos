#Escreva um programa que pergunte o salario do funcionario e
#calcule o valor do seu aumento, para salarios superiores a R$1250,00
#calcule uma amunro de 10% e para salarios inferiores ou igual o aumento é 15%.
s = float(input('Informe seu salario: '))
if s >= 1250.00:
    novo = s + (s * 0.10)
    print('Seu salario com aumento de 10% fica {:.2f}'.format(novo))
else:
    s < 1250.00
    novo = s + (s * 0.15)
    print('Seu salario com aumento de 15% fica {:.2f}'.format(novo))
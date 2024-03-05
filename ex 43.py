#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
#tabela abaixo:
# - abaixo de 18.5: ABAIXO DO PESO!
# - entre 18.5 e 25: PESO IDEAL!
# - 25 até 30: SOBREPESO!
# - 30 até 40: OBESIDADE!
# - acima de 40: OBESIDADE MÓRBIDA!
peso = float(input('Digite seu peso?(kg) '))
altura = float(input('Qual a sua altura?(m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.2f}' .format(imc))
if imc < 18.5:
    print('Voçê esta ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print('Voçê esta no PESO IDEAL!')
elif imc >= 25 and imc < 30:
    print('Voçê esta SOBREPESO!')
elif imc >= 30 and imc < 40:
    print('Voçê esta OBESIDADE!')
elif imc > 40:
    print('Voçê esta OBESIDADE')
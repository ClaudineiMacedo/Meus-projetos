#Faça um programa que leia o sexo de uma pessoa, só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
#novamente  até ter um valor correto.
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('Dados invalidos! Informe seu sexo: [M/F] ')).strip().upper()
print('Sexo {} registrado com sucesso!'.format(sexo))
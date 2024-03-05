#Crie um programa que leia duas notas de um aluno e calcule sua media, monstrando uma menssagem no final, de acordo
#com sua média atingida:
# - Média baixa  de 0 a 5: REPROVADO
# - Média entre 5 a 6.9: RECUPERAÇÃO
# - Média 7 ou superior: APROVADO
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Somando as notas {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if media <= 5:
    print('Sua media foi {:.1f} voçê REPROVADO!'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua media foi {:.1f} voçê de RECUPERAÇÃO!'.format(media))
elif media >= 7:
    print('Sua media foi {:.1f} voçê APROVADO!'.format(media))
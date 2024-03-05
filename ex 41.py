#A confederação nacional de natação prescisa de um programador que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com sua idedade:
# - até 9 anos: MIRIM
# - até 14 anos: INFANTIL
# - até 19 anos: JUNIOR
# - até 25 anos: SÊNIOR
# - Acima: PROFISSIONAL
from datetime import date
atual = date.today().year
nascimento = int(input('Data de nascimento: '))
nome = str(input('Digite seu nome: '))
idade = atual - nascimento
print('Voçê {} tem {} anos de idade'.format(nome, idade))
if idade <= 9:
    print('{} sua categoria é a MIRIM!'.format(nome))
elif idade <= 14:
    print('{} Sua categoria é a INFANTIL!'.format(nome))
elif idade <= 19:
    print('{} Sua categoria é a JUNIOR!'.format(nome))
elif idade <= 25:
    print('{} sua categoria é a SENIOR!'.format(nome))
elif idade >= 25:
    print('{} sua categoria é a PROFISSIONAL!'.format(nome))
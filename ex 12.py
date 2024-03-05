p = float(input('Qual valor do produto? '))
s = p - (p*0.05)
print('O produto custava {} com desconto de 5% no valor do produto que ficou em R${:.2f}'.format(p, s))
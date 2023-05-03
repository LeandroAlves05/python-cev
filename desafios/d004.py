n = input('Digite algo: ')
print (f'É apenas um número? {n.isnumeric()}')
print (f'São apenas letras? {n.isalpha()}')
print (f'São apenas espaços? {n.isspace()}')
print (f'Está em caixa alta? {n.isupper()}')
print (f'É um número decimal? {n.isdecimal()}')
print (f'É alfanumérico? {n.isalnum()}')
print (f'Está capitalizada? {n.istitle()}')


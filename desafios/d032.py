from datetime import date
ano = int(input('Digite um ano, Coloque 0 para analisar o ano atual:  '))
if ano == 0:
    ano = date.today().year
print(f'O ano de {ano} é bissexto!' if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else f'O ano de {ano} não é bissexto.')
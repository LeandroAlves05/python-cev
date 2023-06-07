from datetime import date
nasc = int(input('Em que ano você nasceu? '))
anoAtual = date.today().year
idade = anoAtual - nasc
print(f'Quem nasceu em {nasc} possui {idade} anos em {anoAtual}.')
if idade == 18:
    print('Opa! neste ano você precisa se apresentar para o alistamento.')
elif idade < 18:
    print(f'O ano do seu alistamento ainda não chegou, faltam {18 - idade} anos!')
    print(f'Seu alistamento será em {anoAtual + (18 - idade)}')
else:
    print(f'O seu tempo de alistamento já passou FAZEM {idade - 18} ANOS!')
    print(f'O ano de alistamento deveria ser em {anoAtual - (idade - 18)}')
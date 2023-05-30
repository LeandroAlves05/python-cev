idade = int(input('Qual a sua idade? '))
if idade == 18:
    print('Opa! neste ano você precisa se apresentar para o alistamento.')
elif idade < 18:
    print(f'O ano do seu alistamento ainda não chegou, faltam {(idade -18) *(-1)} anos!')
else:
    print(f'O seu tempo de alistamento já passou FAZEM {idade -18} ANOS!')
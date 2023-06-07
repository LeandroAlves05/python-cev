from datetime import date
nasc = int(input('Digite em qual ano você nasceu: '))
anoAtual = date.today().year
idade = anoAtual - nasc
if idade > 20:
    print('Sua categoria é MASTER!')
elif idade > 19:
    print('Sua categoria é SÊNIOR!')
elif idade > 14:
    print('Sua categoria é JUNIOR!')
elif idade > 9:
    print('Sua categoria é INFANTIL!')
elif idade <= 9:
    print('Sua categoria é MIRIM!')
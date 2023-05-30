valorCasa = float(input('Digite o valor da casa: '))
salario = float(input('Qual o valor do seu salário: '))
quantAnos = int(input('Em quantos anos você pretende pagar: '))
prestMensal = valorCasa / (quantAnos * 12)
salario30p = 30/100 * salario
if salario30p > prestMensal:
    print(f'O valor da prestação mensalmente será de R${prestMensal:.2f}')
else:
    print('Infelizmente você não pode financiar esta casa por este período de tempo.')
    print(f'Neste período o valor mensal seria de R${prestMensal:.2f} , o requerido é que no mínimo 30% do seu salário pague este valor.')

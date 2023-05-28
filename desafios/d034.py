salario = float(input('Digite o valor do salário do funcionário: '))
if salario > 1250.00:
    aumento = salario + (10/100*salario)
else:
    aumento = salario + (15/100*salario)
print(f'Quem ganhava {salario} agora receberá R${aumento:.22f}.')
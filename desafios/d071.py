print('='*30)
print('           BANCO LV')
print('='*30)
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0
valor = int(input('Qual valor você quer sacar? R$'))
while True:
    if valor > 0:
        if valor - 50 >= 0:
            valor -= 50
            nota50 += 1
        elif valor - 20 >= 0:
            valor -= 20
            nota20 += 1
        elif valor - 10 >= 0:
            valor -= 10
            nota10 += 1
        elif valor - 1 >= 0:
            valor -= 1
            nota1 += 1
    else:
        break
print(f'Total de {nota50} cédulas de R$50')
if nota20 > 0:
    print(f'Total de {nota20} cédulas de R$20')
if nota10 > 0:
    print(f'Total de {nota10} cédulas de R$10')
if nota1 > 0:
    print(f'Total de {nota1} cédulas de R$1')    
print('='*30)
print('Volte sempre ao BANCO LV! Faça bom proveito!')
num = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
# Verificando quem é menor
menor = num
if num2<num and num2<num3:
    menor = num2
if num3<num and num3<num2:
    menor = num3
# Verificando quem é maior
maior = num
if num2>num and num2>num3:
    maior = num2
if num3>num and num3>num2:
    maior = num3
print(f'O menor valor foi {menor} e o maior valor foi {maior}')
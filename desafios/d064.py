cont = valor = num = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    valor += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {valor}')
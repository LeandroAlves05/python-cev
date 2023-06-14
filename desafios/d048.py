soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'A soma de todos os ímpares entre os numeros 1 e 500 é igual a: {soma}')
print(f'Os valores somados foram em total {cont}')

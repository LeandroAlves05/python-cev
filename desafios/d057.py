sexo = str(input('Informe seu sexo [M/F]: ')).strip()
while sexo not in 'MmFf':
    print('Valor Inválido')
    sexo = str(input('Por favor, informe seu sexo [M/F]: ')).upper().strip()[0]
print(f'Sexo {sexo.upper()} registrado com sucesso')
while True:
    print('-'*30)
    print('     CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: '))
    if sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F]: '))
    continua = str(input('Quer continuar? [S/N] '))
    if continua in 'Ss':
        print('-'*30)
        print('     CADASTRE UMA PESSOA')
        print('-'*30)
        idade = int(input('Idade: '))
        sexo = str(input('Sexo: [M/F]: '))
        if sexo not in 'MmFf':
            sexo = str(input('Sexo: [M/F]: '))
        continua = str(input('Quer continuar? [S/N] '))
    elif continua in 'Nn':
        break
menosVinte = 0
maiorDeIdade = 0
homens = 0
while True:
    print('-'*30)
    print('     CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: '))
    if idade > 18:
        maiorDeIdade += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        menosVinte += 1
    print('-'*30)
    continua = str(input('Quer continuar? [S/N]: '))
    while continua not in 'SsNn':
        continua = str(input('Quer continuar? [S/N]: '))
    if continua in 'Nn':
        break
print('='*6,'FIM DO PROGRAMA','='*6)
print(f"""Total de pessoas com mais de 18 anos: {maiorDeIdade}
Ao todo temos {homens} homens cadastrados
E temos {menosVinte} mulheres com menos de 20 anos""")

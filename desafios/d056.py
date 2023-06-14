somaIdade = 0
nomeVelho = 0
mediaIdade = 0
maisVelho = 0
totMulher20 = 0
for p in range(1,5):
    print('-'*5, f'{p}ª Pessoa', '-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maisVelho = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maisVelho:
        maisVelho = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1
mediaIdade = somaIdade / 4
print(f'A média de idade do grupo é de {mediaIdade} anos.')
print(f'O homem mais velho tem {maisVelho} anos e se chama {nomeVelho}')
print(f'Ao todo há {totMulher20} mulheres com menos de 20 anos.')
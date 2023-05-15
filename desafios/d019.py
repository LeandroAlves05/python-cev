from random import choice
al1 = str(input('Digite o nome do primeiro aluno: '))
al2 = str(input('Agora Digite o nome do segundo aluno: '))
al3 = str(input('Digite o nome do terceiro aluno: '))
al4 = str(input('Por fim, digite o nome do quarto aluno: '))
seq = [al1,al2,al3,al4]
sorteio = choice(seq)
print(f'O aluno sorteado foi o {sorteio}!!!')
from random import shuffle
al1 = str(input('Nome do primeiro aluno: '))
al2 = str(input('Nome do segundo aluno: '))
al3 = str(input('Nome do terceiro aluno: '))
al4 = str(input('Nome do quarto (e último) aluno: '))
seq = [al1, al2, al3, al4]
shuffle(seq)
print(f'A sequência escolhida foi: {seq}')

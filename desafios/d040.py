nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'Você ficou com {media} na média, ESTÁ REPROVADO!')
elif media > 5.0 and media < 6.9:
    print(f'Você ficou com {media} na média, ESTÁ DE RECUPERAÇÃO!')
else:
    print(f'Você ficou com {media} na média, está APROVADO! parabéns!')
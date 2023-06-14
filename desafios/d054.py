from datetime import date
anoAtual = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    ano = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = anoAtual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Destas datas, {maior} são maiores de idade e {menor} são menores de idade')

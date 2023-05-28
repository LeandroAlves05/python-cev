valor = float(input('Digite a distância do seu embarque até o ponto de chegada em Km: '))
passagem = valor*0.5 if valor <= 200 else valor*0.45
print(f'O valor da sua passagem no total é de R${passagem:.2f}')


print('-'*30)
print('       LV SUPERMERCADOS')
print('-'*30)
produto = 0
valor = 0
total = 0
maisDeMil = 0
maisBarato = 99999
while True:
    produto = str(input('Nome do Produto: '))
    valor = float(input('Preço: R$'))
    total += valor
    if valor < maisBarato:
        maisBarato = valor
        nomeMaisBarato = produto
    if valor > 1000:
        maisDeMil += 1
    continuar = str(input('Quer continuar? [S/N] '))[0]
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] '))[0]
    if continuar in 'Nn':
        break
print('-'*5,'FIM DO PROGRAMA','-'*5)
print(f"""O total da compra foi R${total:.2f}
temos {maisDeMil} produtos custando mais de R$1000.00
O produto mais barato foi {nomeMaisBarato} que custa R${maisBarato:.2f}""")
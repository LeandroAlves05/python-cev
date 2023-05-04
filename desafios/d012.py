print('Seja Bem vindo a minha querida Loja! \n \nVassoura         R$10.00 \nPá de ferro      R$20.00 \nFerro de passar  R$50.00')
valor = float(input('\n Hoje estamos com 5% de desconto! digite o valor do que deseja para saber quanto ficará! : '))
promo = valor - (valor * 0.05) 
print(f'O valor final será de R${promo}!') 
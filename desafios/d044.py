valor = float(input('Digite o valor do produto desejado: '))
metodo = str(input('''Como você deseja pagar?
[ 1 ] Para pagar no dinheiro/cheque
[ 2 ] Para pagar á vista no cartão
[ 3 ] Para pagar 2x no cartão
[ 4 ] Para pagar 3x ou mais no cartão
-=-=-=-Qual o método escolhido?-=-=-=- '''))
if metodo == '1' or metodo == 1:
    promo = valor - (10 / 100 * valor)
    print(f'O valor com desconto ficará R$ {promo:.2f} ')
elif metodo == '2' or metodo == 2:
    promo = valor - (5 / 100 * valor)
    print(f'O valor com desconto ficará R$ {promo:.2f}')
elif metodo == '3' or metodo == 3:
    print(f'O valor total da compra será R$ {valor:.2f}')
elif metodo == '4'or metodo == 4:
    parcelas = int(input('Quantas parcelas serão? '))
    juros = valor + (20 / 100 * valor)
    parc = juros / parcelas
    print(f'O valor das parcelas em {parcelas}x é de R${parc:.2f} com Juros')
    print(f'O valor total será de R${juros:.2f}')
else:
    print('Este método de pagamento não existe.')

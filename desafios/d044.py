valor = float(input('Digite o valor do produto desejado: '))
metodo = str(input('''Como você deseja pagar?
para á dinheiro ou cheque digite "a vista"
para á vista no cartão digite    "1x cartao"
para 2x no cartão digite         "2x"
para 3x ou mais digite           "3x"
-=-=-=-Qual o método escolhido?-=-=-=- '''))
if metodo == 'a vista':
    promo = valor - (10 / 100 * valor)
    print(f'O valor com desconto ficará R$ {promo:.2f} ')
if metodo == '1x cartao':
    promo = valor - (5 / 100 * valor)
    print(f'O valor com desconto ficará R$ {promo:.2f}')
if metodo == '2x':
    print(f'O valor total da compra será R$ {valor:.2f}')
if metodo == '3x':
    juros = valor + (20 / 100 * valor)
    print(f'O valor total com o juros será de R$ {juros:.2f}')
dias = int(input('Quantos dias alugados? '))
kmRod = float(input('Quantos Km rodados? '))
total = (dias * 60) + (kmRod * 0.15)
print(f'O total a pagar é de R${total:.2f}')
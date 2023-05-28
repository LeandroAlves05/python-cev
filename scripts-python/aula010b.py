n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m:.1f}')
print('Sua média foi boa, Parabéns!' if m >= 6.0 else 'Sua média foi uma merreca, ESTUDE MAIS!')
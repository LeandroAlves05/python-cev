primTermo = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite o valor da razão da P.A: '))
print(f'Os primeiros 10 valores da P.A deste valor são respectivamente: ')
decimo = primTermo + (10 -1) * razao
for c in range(primTermo, decimo+razao, razao):
    print(c, end=' → ')
print('FIM')
print('Gerador de PA')
print('-=-' * 5)
primTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da P.A: '))
termo = primTermo
cont = 1
while cont <= 10:
    print(f'{termo} → ', end='')
    termo += razao
    cont += 1
print('FIM')
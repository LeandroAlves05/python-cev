print('-'*10, 'SEQUENCIA DE FIBONACCI', '-'*10)
num = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*50)
print(f'{t1} → {t2}', end='')
cont = 3
while cont <= num:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')
print('~'*50)

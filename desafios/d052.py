num = int(input('\033[mDigite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO número {num} foi divisível por {total} vezes')
if total == 2:
    print('O que confirma que ele é um número primo!')
else:
    print('O que prova que ele NÃO é um número primo')
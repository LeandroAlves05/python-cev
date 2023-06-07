print('-=-' * 17)
print(' ' * 16, 'CONVERSOR DE VALORES')
print('-=-' * 17)

num = int(input('Digite um número inteiro: '))
print(''' Escolha a base da conversão:
[ 1 ] para Binário
[ 2 ] para Octal
[ 3 ] para Hexadecimal''')
base = int(input('Sua opção: '))

if base == 1:
    print(f'O valor {num} em binário é igual á {bin(num)[2:]}')
elif base == 2:
    print(f'O valor {num} em octal é igual á {oct(num)[2:]}')
elif base == 3:
    print(f'O valor {num} em hexadecimal é {hex(num)[2:]}')
else:
    print('Esta opção não existe, tente novamente')
         

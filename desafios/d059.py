from time import sleep
escolha = 0
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
while escolha != 5:
    sleep(2)
    print('Escolha uma das opcões á seguir!')
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Qual o Maior
[ 4 ] Digitar novos números
[ 5 ] Sair do Programa''')
    escolha = int(input('Opção escolhida: '))
    if escolha == 1:
        print(f'A soma de {n1} e {n2} é igual á {n1 + n2}')
    if escolha == 2:
        print(f'A multiplicação entre {n1} e {n2} é igual á {n1 * n2}')
    if escolha == 3:
        if n1 == n2:
            print('Os valores são iguais!')
        elif n1 > n2:
            print(f'O maior é {n1} e o menor é {n2}')
        else:
            print(f'O maior é {n2} e o menor é {n1}')
    if escolha == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    else:
        print('Opção inválida, tente novamente.')
print('Fim da execução')

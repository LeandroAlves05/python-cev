n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print(f'''O primeiro número é maior que o segundo número,
pois {n1} é maior que {n2}.''')
elif n2 > n1:
    print(f'''O segundo número é maior que o primeiro número,
pois {n2} é maior que {n1}.''')
else:
    print('''Os valores digitados são iguais!''')

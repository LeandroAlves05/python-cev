num = int(input('Digite um número de 0 á 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"""Analisando o valor, vemos que: 
Valor da Unidade: {u}
Valor da Dezena: {d}
Valor da Centena: {c}
Valor do Milhar: {m}
""")

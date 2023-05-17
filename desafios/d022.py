nome = str(input('Digite seu nome completo: ')).strip()
quantNome = len(nome) - nome.count(' ')
corte = nome.split()
print(f""" 
Seu nome em caixa alta é {nome.upper()}.
Seu nome em letras pequenas é {nome.lower()}.
Seu nome possui {quantNome} letras ao todo.
Seu primeiro nome é {corte[0]} possui {len(corte[0])} letras.
""")

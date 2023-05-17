n = str(input('Digite seu nome: ')).strip()
nome = n.split()

print(f"""Seu primeiro nome é {nome[0]}
E seu último nome é {nome[-1]}""")

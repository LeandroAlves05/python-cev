nome = str(input('Qual é o seu nome? '))
if nome == 'Leandro' or nome == 'Jean':
    print('Que nome bonito, fiu fiu')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo' or nome == 'Enzo' or nome == 'Valentina':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana Raluca':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia {nome}!')
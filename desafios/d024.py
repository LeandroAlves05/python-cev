cidade = str(input('Digite o nome da sua cidade natal: ')).strip().lower()
temSanto = 'santo' in cidade[:5]
print(f'Sua cidade começa com Santo? {temSanto}')

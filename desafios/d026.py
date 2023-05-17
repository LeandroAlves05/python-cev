frase = str(input('Digite uma frase: ')).strip().lower()
letraA = frase.count('a')
primPosicao = frase.find('a')
ultPosicao = frase.rfind('a')
print(f"""Sua frase possui {letraA} letras "a".
A primeira letra "a" aparece na  posição {primPosicao + 1}.
E a última letra "a" aparece na  posição {ultPosicao + 1}.""")
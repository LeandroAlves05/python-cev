from random import randint
tent = 0
numRob = randint(0, 10)
acertou = False
print('Vou Pensar em um número de 1 á 10 Tente adivinhar!')
while not acertou:
    palpite = int(input('Qual o seu palpite? '))
    tent += 1
    if palpite == numRob:
        acertou = True
    else:
        if palpite > numRob:
            print('Nãaao, um pouco menos!')
        elif palpite < numRob:
            print('Nãaao, um pouco mais!')
print(f'Você acertou! foram necessárias {tent} tentativas para acertar')

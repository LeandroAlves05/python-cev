from random import randint
from time import sleep
print('-=-' * 18)
print('Tente adivinhar em qual número de 0 á 5 estou pensando')
print('-=-' * 18)
num = int(input('Qual você acha que é? '))
print('PROCESSANDO...')
sleep(2)
num2 = randint(0, 5)
if num == num2:
    print(f'PARABÉNS VOCÊ ACERTOU! ERA {num2}!')
else:
    print(f'Você errou era {num2}, blééé')
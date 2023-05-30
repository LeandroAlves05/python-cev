from random import choice
from time import sleep
print('-=-' * 24)
print(' ' * 32, 'JOKEMPÔ')
print('-=-' * 24)
print('Vamos jogar jokempô! escolha pedra, papel ou tesoura e veremos quem ganha!')
escolha = str(input('Qual sua escolha? pedra, papel ou tesoura? '))
print('DEIXE ME ESCOLHER...')
sleep(2)
seq = 'pedra', 'papel', 'tesoura'
escolhaR = choice(seq)
escolhaRobo = escolhaR
print(f'Eu escolhi {escolhaRobo}')
if escolha == escolhaRobo:
    print(f'Há! Você também escolheu {escolha} EMPATAMOS!')
elif escolhaRobo == 'pedra' and escolha == 'tesoura' or escolhaRobo == 'papel' and escolha == 'pedra' or escolhaRobo == 'tesoura' and escolha == 'papel':
    print('A Há!! Eu ganhei!! PERDEDOR MUAHAHAHAHA')
elif escolhaRobo == 'tesoura' and escolha == 'pedra' or escolhaRobo == 'pedra' and escolha == 'papel' or escolhaRobo == 'papel' and escolha == 'tesoura':
    print('Aaah você ganhou, parabéns! bléééé ')
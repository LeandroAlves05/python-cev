from random import choice
from time import sleep
print('-=-' * 20)
print(' ' * 25, 'JOKEMPÔ')
print('-=-' * 20)
print('''Vamos jogar jokempô! escolha:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
escolha = str(input('Qual sua escolha? pedra, papel ou tesoura? '))
print('DEIXE ME ESCOLHER...')
sleep(2)
seq = 'pedra', 'papel', 'tesoura'
escolhaR = choice(seq)
escolhaRobo = escolhaR
print(f'Eu escolhi {escolhaRobo}')
if escolhaRobo == 'pedra' and escolha == '2' or escolhaRobo == 'papel' and escolha == '0' or escolhaRobo == 'tesoura' and escolha == '1':
    print('A Há!! Eu ganhei!! PERDEDOR MUAHAHAHAHA')
elif escolhaRobo == 'tesoura' and escolha == '0' or escolhaRobo == 'pedra' and escolha == '1' or escolhaRobo == 'papel' and escolha == '2':
    print('Aaah você ganhou, parabéns! bléééé ')
else:
    print(f'Há! Você também escolheu {escolhaRobo} EMPATAMOS!')
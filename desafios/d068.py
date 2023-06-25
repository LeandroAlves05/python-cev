from random import randint
robo = randint(1, 10)
vitorias = 0
print('-='*20)
print('        O Jogo de PAR ou ÌMPAR!')
print('-='*20)
while True:
    player = int(input('Digite qual valor você escolheu: '))
    jogadorEscolha = str(input('Digite sua escolha! PAR ou ÌMPAR! [P/I]: '))
    print('-'*50)
    if (player + robo) % 2 == 0:
        print(f'Você jogou {player} e o computador {robo}. o Total de {robo+player} DEU PAR')
        if jogadorEscolha in 'Pp':
            print('-'*50)
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('-'*50)
            print('Você PERDEU!')
            print('-='*23)
            print(f'FIM DE JOGO! Você venceu {vitorias} vezes')
            break            
    else:
        print(f'Você jogou {player} e o computador {robo}. o Total de {robo+player} DEU ÍMPAR')
        if jogadorEscolha in 'Ii':
            print('-'*50)
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('-'*50)
            print('Você PERDEU!')
            print('-='*23)
            print(f'FIM DE JOGO! Você venceu {vitorias} vezes')
            break 
    print('Vamos jogar denovo...')
    print('-'*50)
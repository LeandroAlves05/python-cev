vel = float(input('Imagine que você esta num passeio, Qual seria a velocidade do seu carro? '))
if vel > 80:
    multa = (vel - 80) * 7
    print(f'VOCÊ SERÁ MULTADO EM R${multa:.2f} POR ANDAR ACIMA DE 80Km POR HORA!')
else:
    print('Ótimo! siga a viagem em segurança!')

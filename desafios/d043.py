peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite a sua altura em Metros: '))
imc = peso / (altura ** 2)
if imc > 40:
    print(f'De acordo com o Índice de Massa Corporal (IMC), seu imc é de {imc:.1f} , você está com obesidade mórbida.')
elif imc > 30:
    print(f'De acordo com o Índice de Massa Corporal (IMC), seu imc é de {imc:.1f} , você está com obesidade.')
elif imc > 25:
    print(f'De acordo com o Índice de Massa Corporal (IMC), seu imc é de {imc:.1f} , você está com sobrepeso.')
elif imc >= 18.5:
    print(f'De acordo com o Índice de Massa Corporal (IMC), seu imc é de {imc:.1f} , você está com o peso ideal, parabéns!')
else:
    print(f'De acordo com o Índice de Massa Corporal (IMC), seu imc é de {imc:.1f} , você está abaixo do peso, necessita de mais proteína!')
    
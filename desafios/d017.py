from math import hypot
print('======CALCULADORA DA HIPOTENUSA======')
catOp = float(input('Digite o valor do cateto oposto: '))
catAd = float(input('Digite o valor do cateto adjacente: '))
hipot = hypot(catOp, catAd)
print(f'O comprimento da hipotenusa é aproximadamente igual á: {hipot:.2f}')

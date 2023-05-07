from math import isqrt
print('======CALCULADORA DA HIPOTENUSA======')
catOp = int(input('Digite o valor do cateto oposto: '))
catAd = int(input('Digite o valor do cateto adjacente: '))
hipot = (catOp**2) + (catAd**2)
raiz = isqrt(hipot)
print(f'O comprimento da hipotenusa é aproximadamente igual á: {raiz:.2f}')

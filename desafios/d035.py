n1 = float(input('Digite o primeiro ângulo: '))
n2 = float(input('Digite o segundo ângulo: '))
n3 = float(input('Digite o terceiro ângulo: '))
if n3 < n1 + n2 and n2 < n1 + n3 and n1 < n2 + n3:
    print('Com esses valores será possível formar um triângulo!')
else:
    print('Com estes valores não será possível formar um triângulo.')
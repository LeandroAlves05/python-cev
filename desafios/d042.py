l1 = float(input('Digite o primeiro ângulo: '))
l2 = float(input('Digite o segundo ângulo: '))
l3 = float(input('Digite o terceiro ângulo: '))
calculo = l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1
if calculo:
    print('Estes valores podem formar um triângulo!')
    if l1 == l2 == l3:
        print('Este triângulo se encaixaria no tipo Equilátero.')
    elif l1 != l2 != l3:
        print('Este triângulo se encaixaria no tipo Escaleno.')
    else:
        print('Este triângulo se encaixaria no tipo Isósceles.')
else:
    print('Estes valores não podem formar um triângulo.')
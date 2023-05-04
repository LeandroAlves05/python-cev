print('=====CALCULADORA DE ÁREA=====')
alt = float(input('Qual a altura da sua parede? : '))
lar = float(input('E qual sua largura? : '))
area = alt * lar
tinta = area / 2
print(f'A área da sua parede equivale a {area}m²\nSerá necessário {tinta:.3}L de tinta para pintar a sua parede por completo.')
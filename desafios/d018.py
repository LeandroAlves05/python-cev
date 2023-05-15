import math 
ang = float(input('Digite um algulo: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print(f'O seno, o cosseno, e a tangente deste número são aproximadamente: {seno:.2f}, {cosseno:.2f} e {tangente:.2f}')
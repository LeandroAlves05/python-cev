while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*20)
    if num < 0: 
        break
    for c in range(1, 10):
        print(f'{num} x {c} = {num*c}')
    print('-'*20)
print('Fim do programa!')
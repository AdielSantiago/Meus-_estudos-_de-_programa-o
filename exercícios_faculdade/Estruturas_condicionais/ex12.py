x:int = int(input('Digite um valor: '))
y:int = int(input('Digite um valor: '))
maior:int = 0 

if x > y:
    maior = x
    print(f'O maior número é o {maior} e a soma entre eles é {x + y}')
elif x < y:
    maior = y
    print(f'O maior número é o {maior} e a soma entre eles é {x + y}')
else:
    print(f'São iguais e a soma é {x + y}')



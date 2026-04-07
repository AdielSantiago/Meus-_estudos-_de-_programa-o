x:int = int(input('Digite um valor: '))

if x > 0:
    print(f'{x} é um número positivo.')
elif x < 0:
    print(F'{x} é um número negativo.')
else:
    print(F'{x} é neutro')
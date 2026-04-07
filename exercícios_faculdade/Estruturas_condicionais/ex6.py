x:int = int(input('Digite um valor: '))
y:int = int(input('Digite um valor: '))
maior:int = 0 

if x > y:
    maior = x
else:
    maior = y

print(f'O maior número é o {maior}')
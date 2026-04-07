num = int(input('Digite um número inteiro:'))

if num < 0 and num % 2 == 0:
    print('Seu número é negativo e é par')

elif num < 0 and not num % 2 == 0:
    print('Seu número é negativo e é impar')

elif num > 0 and num % 2 == 0:
    print('O seu número é positivo e é par')

elif num > 0 and not num % 2 == 0:
    print('O seu número é positivo e é impar')

else:
    print('Seu número é neutro e é par')
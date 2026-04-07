n = int(input("Digite um número: "))

if n == 0:
    print("Neutro")
else:
    resultado = ""
    resultado +=  "Par " if n % 2 == 0 else "Ímpar "
    resultado += "positivo" if n > 0 else "negativo"
    print(resultado)
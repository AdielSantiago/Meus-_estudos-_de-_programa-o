entrada = input("Digite algo: ")

if entrada.isnumeric():
    num = int(entrada)
    print(f"Tipo: {type(num)} - Quadrado: {num**2}")
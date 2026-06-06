while True:
    print("""      
  Escolha um algoritmo abaixo
          
[1] Ler 10 número inteiros       [2] par ou impar?           [3] está na lista?   
[4] remover números da lista     [5] positivos e negativos   [6] intersecção
[7] cadastro                     [8] ordenando números       [9] sair
    """)
    base = int(input('Qual sua opção?: '))
    
    if base == 1:
        numeros = list()
        for i in range(1,11):
            valor = int(input(f'Informe o {i}º número: '))
            numeros.append(valor)
        print(f'Os valores digitados são {numeros}. O maior número é {max(numeros)} e o menor é {min(numeros)}')
    
    elif base == 2:
        master, par, impar = list(), list(), list()
        for i in range(1, 16):
            num = int(input(f'Informe {i}º número: '))
            master.append(num)
        par = [n for n in master if n % 2 == 0]
        impar = [n for n in master if n % 2 != 0]
        print(f'dos números digitados os pares são {par} e os impares são {impar}')
    
    elif base == 3:
        numeros = list()
        for i in range(1, 8):
            x = int(input(f'Digite o {i}º valor: '))
            numeros.append(x)
        y = int(input('Digite o valor para verificação: '))
        status = "está" if y in numeros else "não está"
        print(f'{y} {status} na lista')
    
    elif base == 4:
        numeros = list()
        for i in range(1, 11):
            x = int(input(f'Digite o {i}º valor: '))
            numeros.append(x)
        remover = int(input('Qual numero quer remover?: '))
        numeros = [n for n in numeros if n != remover]
        print(numeros)
        
    elif base == 5:
        numeros, positivos, negativos = list(), list(), list()
        for i in range(1,21):
            num = int(input('Digite um valor: '))
            numeros.append(num)
        positivos = [n for n in numeros if n > 0]
        negativos = [n for n in numeros if n < 0]
        print(f'Existem {len(positivos)} números  positivos e {len(negativos)} números negativos dentre os valores digitados')
    
    elif base == 6:
        lista1, lista2, aparece, exclusivo = [4, 5, 6, 7, 8], [1, 2, 3, 4, 5], [], []      
        aparece = [n for n in lista1 if n in lista2]
        exclusivo = [n for n in lista1 + lista2 if (n in lista1) != (n in lista2)]
        print(f'Da lista {lista1} e {lista2} os numeros que estão nas duas são os {aparece} e os que não estão nas duas são os {sorted(exclusivo)} ')
    
    elif base == 7:
        produtos, pro_menor = [['notebook', 4000, 3], ['celular', 3200, 10], ['headset', 300, 20], ['churrasqueira', 600, 2], ['Placa de vídeo', 3500, 5]], list()
        pro_menor = [n for n in produtos if n[2] < 10]
        print(f'Os produtos com estoque menor que 10 são {pro_menor}. O produto mais caro é o {max(produtos, key = lambda x:x[1])}')
    
    elif base == 8:
        numeros, par, impar = list(), list(), list()
        for i in range(1,13):
            x = int(input(f'Digite {i}º número: '))
            numeros.append(x)
        par = [n for n in numeros if n % 2 == 0]
        impar = [n for n in numeros if n % 2 != 0]
        print(sorted(numeros), sorted(numeros, reverse=True), f'\nSão {len(par)} números pares e {len(impar)} números impares')

    if base == 9:
        print('Saindo...')
        break

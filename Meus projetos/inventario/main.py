import funcoes
from time import sleep
from rich import print

inventario = {}

while True:
    funcoes.interface(inventario)
    try:
        opcao = int(input('\nQual ação deseja fazer no inventário?: '))
    except ValueError:
        print('-' * 74)
        print('[red]As opções de ações com inventário so aceitam entradas de números inteiros.[/]')
        print('-' * 74)
        sleep(5)
    else:

        if opcao == 1:
            
            item_sem_espaco = str(input('Digite o item e a quantidade a ser adicionada seperados por ",": ')).strip().lower()
            itens = item_sem_espaco.split(',')

            if len(itens) > 1:
                item = itens[0]
                quantidade = itens[1]
            else:
                item = itens[0]
                quantidade = 1

            funcoes.adicionar(inventario, item, int(quantidade))
        
        
        elif opcao == 2:
            item_sem_espaco = str(input('Digite o item e a quantidade a ser usada seperados por ",": ')).strip().lower()
            itens= item_sem_espaco.split(',')

            if len(itens) > 1:
                item = itens[0]
                quantidade = itens[1]
            else:
                item = itens[0]
                quantidade = 1

            funcoes.reduzir(inventario, item, int(quantidade))
        
        elif opcao == 0:
            print('Saindo',end='')
            for i in range(4):
                print('.', end='', flush=True)
                sleep(0.5)
            
            break







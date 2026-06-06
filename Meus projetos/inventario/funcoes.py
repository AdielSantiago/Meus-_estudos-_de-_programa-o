from rich import print
from rich.panel import Panel
import os
from time import sleep


def interface(dicionario):
    
    limpar_tela()
    
    conteudo = '[medium_turquoise][1][/] -> [u]Adicionar item no inventário.[/]  '
    conteudo +='[medium_turquoise][2][/] -> [u]Usar item do inventário.[/]\n\n'
    texto_centralizado = " Itens ".center(69, "-")
    conteudo += f"[sky_blue3]{texto_centralizado}[/]\n"

    
    cont = 1
    for chave, valor  in sorted(dicionario.items(), key=lambda par: len(par[0])):
        conteudo += f'[khaki1]{chave}[/]: [bright_red]{valor}[/]    '
        conteudo += '\n\n' if cont % 4 == 0 else ''
        cont += 1
    
    interface = Panel(conteudo, border_style = 'medium_purple1', title='Inventário', expand=False)

    print(interface)

    if len(dicionario) == 0:
        print(f'[u]Seu inventário está vazio[/]')


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def adicionar(dicionario, item, quantidade):
    
    dicionario[item] = dicionario.get(item, 0) + quantidade

    
def reduzir(dicionario, item, quantidade):
    if item in dicionario:
        
        if dicionario.get(item) - quantidade > 0 :
            dicionario[item] = dicionario.get(item) - quantidade
        elif dicionario.get(item) - quantidade == 0:
            dicionario.pop(item)
        else:
            print(f'[u]Você não pussui a quantidade necessária de {item} para usar[/] [white]{quantidade}[/] [u]vezes[/]')
            sleep(3)
    
    else:
        print(f'[u]Você não possui o item: {item}[/]')
        sleep(3)
    
        
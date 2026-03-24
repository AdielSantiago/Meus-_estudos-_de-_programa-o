import os
import platform  # Usado para identificar o SO


def limpar_tela():
    """Limpa a tela do console/terminal."""

    # Verifica o sistema operacional
    sistema_operacional = platform.system()

    if sistema_operacional == "Windows":
        # Comando para limpar no Windows
        os.system('cls')
    else:
        # Comando para limpar em Linux e macOS (e muitos outros UNIX-like)
        os.system('clear')


equipamento = dict()
equipamentos = list()

while True:
    limpar_tela()
    equipamento ['nome'] = str(input('Digite o nome do equipamento: '))

    if equipamento['nome'] == '':
        break

    equipamento ['watt']  = float(input('Digite quantos watts o equipamento consome(0 para finalizar): '))
    
    if equipamento['watt'] == 0:
        break	
    
    equipamento ['tempo'] = float(input('Digite a quantidade de horas que o equipamento  fica ligado: '))

    watt_hora = equipamento['watt'] * equipamento ['tempo']
    kwh = watt_hora / 1000
    equipamento ['valor'] = kwh * 0.6 * 30
    equipamentos.append(equipamento.copy())

limpar_tela()

if len(equipamentos) > 0:
    print(F'{'-----Custo estimado mensal-----'}\n')

    total = 0
    for i in equipamentos:

        nome = i['nome']
        valor = i['valor']
        valor_formatado = f'R${valor:.2f}'
        total = total + valor

        print(F'{nome} -> {valor_formatado:^5}')

    print('-'* 30)
    print(F'total: R${total:.2f} ')
    input()
    print(equipamentos)

else:
    print('Você não adicionou nenhum equipamento')
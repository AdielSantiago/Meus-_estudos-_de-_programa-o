from rich import print
from rich.panel import Panel
import os


class Controleremoto:
    """
    Classe que simula o funcionamento de um controle remoto de TV.

    Atributos de Classe (Constantes):
        canal_min (int): O menor canal disponível (1).
        canal_max (int): O maior canal disponível (6).
        volume_min (int): O volume mínimo (1).
        volume_max (int): O volume máximo (16).
    """

    canal_min: int = 1
    canal_max: int = 6
    volume_min: int = 1
    volume_max: int = 16

    def __init__(self, canal: int = 1, volume: int = 2):
        """
        Inicializa o estado da TV.

        Args:
            canal (int): Canal inicial ao ligar (padrão 1).
            volume (int): Volume inicial ao ligar (padrão 2).
        """
        self.canal_atual: int = canal
        self.volume_atual: int = volume
        self.ligado: bool = False

    def liga_desliga(self):
        """Alterna o estado de energia da TV (Ligado/Desligado)."""
        self.ligado = not self.ligado

    def canal_mais(self):
        """
        Sobe um canal. Se chegar no canal_max, volta para o canal_min (ciclo).
        Apenas funciona se a TV estiver ligada.
        """
        if self.ligado:
            if self.canal_atual == Controleremoto.canal_max:
                self.canal_atual = Controleremoto.canal_min
            else:
                self.canal_atual += 1

    def canal_menos(self):
        """
        Desce um canal. Se chegar no canal_min, vai para o canal_max (ciclo).
        Apenas funciona se a TV estiver ligada.
        """
        if self.ligado:
            if self.canal_atual == Controleremoto.canal_min:
                self.canal_atual = Controleremoto.canal_max
            else:
                self.canal_atual -= 1

    def volume_mais(self):
        """Aumenta o volume em 1, respeitando o limite máximo."""
        if self.ligado:
            if self.volume_atual < Controleremoto.volume_max:
                self.volume_atual += 1

    def volume_menos(self):
        """Diminui o volume em 1, respeitando o limite mínimo."""
        if self.ligado:
            if self.volume_atual > Controleremoto.volume_min:
                self.volume_atual -= 1

    def mostrar_tv(self):
        """
        Renderiza visualmente o estado da TV usando a biblioteca Rich.
        Mostra o canal atual em destaque e o volume em uma barra de progresso verde.
        """
        if  not self.ligado:
            conteudo = '[red]A tv está desligada[/]'
        else:
            # Renderização dos Canais
            conteudo = 'CANAL = '
            for i in range(Controleremoto.canal_min, Controleremoto.canal_max + 1):
                if i == self.canal_atual:
                    conteudo += f'[yellow on yellow] {i} [/]'
                else:
                    conteudo += f' {i} '

            # Renderização da Barra de Volume
            conteudo += '\nVOLUME = '
            for i in range(Controleremoto.volume_min, Controleremoto.volume_max + 1):
                if i <= self.volume_atual:
                    conteudo += '[black on green] [/]'
                else:
                    conteudo += '[black on white] [/]'

        # Criação do painel visual
        tv = Panel(conteudo, title='[ TV ]', width=45)
        print(tv)

c1 = Controleremoto()
while True:
    # LIMPEZA DE TELA:
    # Isso garante que a TV seja desenhada sempre na mesma posição do terminal.
    os.system('cls' if os.name == 'nt' else 'clear')

    # Chama o método que utiliza a biblioteca 'rich' para desenhar a interface visual.
    c1.mostrar_tv()

    # .strip() remove espaços em branco acidentais antes ou depois do comando.
    # Exemplo: " @ " vira "@", evitando erros de reconhecimento no match.
    comando: str = input(f'< CH{c1.canal_atual} >   - vol{c1.volume_atual} + ').strip()

    # Substitui múltiplos if/elifs por uma sintaxe mais limpa e legível.
    match comando:
        case '0':
            # Encerra o loop e finaliza a execução do programa.
            break
        case '@':
            # Alterna o estado de ligado/desligado.
            c1.liga_desliga()
        case '>':
            # Sobe um canal
            c1.canal_mais()
        case '<':
            # Desce um canal
            c1.canal_menos()
        case '-':
            # Diminui o volume
            c1.volume_menos()
        case '+':
            # Aumenta o volume
            c1.volume_mais()

input()
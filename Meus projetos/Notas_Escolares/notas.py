from rich import print
from rich.panel import Panel

class Nota:
    def __init__(self, nome, *args):
        #Atributos
        self.nome = nome
        self.notas = args

    #métodos
    def media(self):
        #Verifica se o argumento args foi passado
        if not self.notas:
            return 0
        
        #Calcula a média das notas
        return sum(self.notas) / len(self.notas)


    def analisar(self):
        m = self.media()

        conteudo = f'[u]Nome do aluno: {self.nome}[/u]\n\n'

        for i, nota in enumerate(self.notas, 1):
            conteudo += f'[green]{i}ºNota[/]: [sky_blue3]{nota}\n[/]'

        if m < 7:
            conteudo += f'\n[u red]Média final: {m:.1f}[/u red]'
        else:
            conteudo += f'\n[u medium_purple1]Média final: {m:.1f}[/u medium_purple1]'

        painel = Panel(conteudo,
                       title='[blue]Notas do aluno[/]',
                       border_style='yellow',
                       expand=False
                 )

        print(painel)

a1 = Nota('Adiel de freitas santiago', 6, 9, 7)
a1.analisar()
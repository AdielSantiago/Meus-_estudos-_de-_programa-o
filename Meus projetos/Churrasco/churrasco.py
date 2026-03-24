from rich import print
from rich.panel import Panel


class Churrasco:
    preco_por_kg = 82.40
    def __init__(self, quant_pessoas, carne_por_pessoa = 400):
        #Atributos:

        self.pessoas = quant_pessoas
        self.carne_por_pessoa = carne_por_pessoa

    #Métodos:

    def total_de_carne(self):
        return (int(self.pessoas) * self.carne_por_pessoa) / 1000

    def valor_total(self):
        return Churrasco.preco_por_kg * self.total_de_carne()

    def valor_por_pessoa(self):
        return float(self.valor_total()) / self.pessoas

    def analisar(self):

        conteudo = f'[medium_purple1]->[/] Análise do churrasco com [blue]{self.pessoas} pessoas[/]'

        conteudo += f'\n[medium_purple1]->[/] Será necessário [red]{self.total_de_carne()}Kg de carne[/] [bold yellow]({self.carne_por_pessoa}g/pessoa)[/].'

        conteudo += f'\n[medium_purple1]->[/] O valor total do churras sai por [green]R${self.valor_total():.2f}[/] [bold green](R${self.valor_por_pessoa()}/pessoa)[/].'

        painel = Panel(conteudo, title='[medium_purple2]Churrasco com amigos[/]')
        print(painel)

        print()


c1 = Churrasco(15, 400)
c2 = Churrasco(200, 300)
c1.analisar()
c2.analisar()

input()

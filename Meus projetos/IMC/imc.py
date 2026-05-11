import os
from rich import print
from rich.panel import Panel

# Função para limpar o console de forma multiplataforma
def limpartela():
    # 'nt' refere-se ao Windows, caso contrário assume sistemas Unix (Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')


class Pessoa:
    # Constantes para definir o tamanho da régua visual do IMC
    imc_max = 40
    imc_min = 15
    
    def __init__(self, nome, peso, altura):
        """Inicializa os dados básicos da pessoa."""
        self.nome: str = nome
        self.peso: float = peso
        self.altura: float = altura
        self.imc: float = 0
    
    def calcula_imc(self):
        """Calcula o valor do IMC: Peso dividido pela altura ao quadrado."""
        self.imc = self.peso / self.altura ** 2

    def saudavel(self):
        """Analisa o IMC e define a categoria de saúde e a cor visual."""
        if self.imc < 18.5:
            return 'Abaixo do peso', '[blue]'
        elif self.imc < 25:
            return 'Saudável', '[green]'
        elif self.imc < 30:
            return 'Intermediário (Sobrepeso)', '[yellow]'
        else:
            return 'Atenção (Obesidade)', '[red]'
        
    def exibir(self):
        """Gera a interface visual com a régua de IMC e dados do usuário."""
        imc_arredondado = int(self.imc)
        
        conteudo = ''
        barra = ''
        
        # Obtém o status de saúde e a cor definida no método anterior
        status, cor = self.saudavel()

        # Montagem da barra colorida (Régua de IMC)
        for i in range(Pessoa.imc_min, Pessoa.imc_max + 1):
            # Define o estilo de fundo para cada faixa da régua
            if i < 19:
                estilo = 'black on blue'    # Abaixo do peso
            elif i < 25:
                estilo = 'black on green'   # Ideal
            elif i < 28:
                estilo = 'black on yellow'  # Sobrepeso
            else:
                estilo = 'black on red'     # Obesidade
            
            # Se o valor atual da régua coincidir com o IMC do usuário, coloca o ponteiro ▼
            if i == imc_arredondado:
                barra += f'[{estilo}] ▼ [/]'
            else:
                barra += f'[{estilo}]   [/]'
                
        # Adiciona a barra pronta ao conteúdo final
        conteudo += f'{barra}\n'
        
        # Adiciona a escala numérica abaixo da barra (15, 16, 17...)
        for i in range(Pessoa.imc_min, Pessoa.imc_max + 1):
            conteudo += f'{str(i)} '
        
        # Formatação dos textos informativos com estilos do Rich (sublinhado e cores)
        conteudo += f'\n\nO IMC de {self.nome} é [u]{cor}{self.imc:.2f}[/][/] e está na situação {cor}{status}[/] '
        conteudo += f'\nAltura -> [u purple]{self.altura:.2f}M[/]\nMassa -> [u purple]{self.peso}KG[/]'
        
        # Criação do painel visual (caixa envolvente)
        interface = Panel(conteudo, title='IMC', border_style='sky_blue3', expand=False)
        print(interface)
            

# Loop principal do programa
while True:
    # Cabeçalho decorativo centralizado em 80 espaços
    print('=' * 80)
    print(f"{'Verifique seu IMC'.center(80)}")
    print('=' * 80)
    
    # Coleta de informações do usuário
    nome: str = str(input('Digite seu nome: ')) 
    massa: float = float(input('Digite seu peso (KG): '))
    altura: float = float(input('Digite sua altura (M): '))
    
    # Limpa as perguntas para mostrar apenas o resultado
    limpartela()
    
    # Criação do objeto (Instância)
    p1 = Pessoa(nome, massa, altura)
    p1.calcula_imc()
    p1.exibir()

    # Controle de repetição do programa
    # .lower()[0] pega apenas a primeira letra em minúsculo (s ou n)
    continuar = input('Deseja alterar os dados? (Sim ou Não): ').lower().strip()[0]

    if continuar == 'n':
        print("Encerrando programa...")
        break
    elif continuar == 's':
        limpartela()
  Simulação de Controle Remoto de TV

Este projeto  desenvolvido em Python simula as funcionalidades de um controle remoto de televisão. O projeto foca em conceitos de Programação Orientada a Objetos (POO) e utiliza a biblioteca Rich para uma interface visual colorida terminal.
  
  Funcionalidades

    Ligar/Desligar: Alterna o estado de energia da TV.

    Troca de Canais: Navegação cíclica entre os canais (1 a 6).

    Controle de Volume: Ajuste de volume (1 a 16) com barra de progresso visual.

    Interface Dinâmica: Renderização de painéis e cores via terminal.

    Comandos Intuitivos: Mapeamento de teclas para facilitar o uso.

   Tecnologias Utilizadas

    Python 3.10+

    Rich: Biblioteca para renderização de texto e painéis no console.

    OS: Biblioteca nativa para manipulação de comandos do sistema (limpeza de tela).

   Pré-requisitos

Antes de rodar o projeto, você precisará ter o Python instalado e a biblioteca rich.
Bash

# Instalar a biblioteca Rich
pip install rich

  Como Usar

    Utilize os seguintes comandos no terminal:

        @ : Ligar ou Desligar a TV.

        > : Próximo canal.

        < : Canal anterior.

        + : Aumentar volume.

        - : Diminuir volume.

        0 : Sair do programa.

   Conceitos de Programação Aplicados

Este projeto foi desenvolvido como parte de estudos acadêmicos,cobrindo:

    Encapsulamento: A lógica de limites de volume e canais está protegida dentro dos métodos da classe.

    Atributos de Classe: Definição de constantes para limites operacionais.

    Clean Code: Código documentado com Docstrings e tipos definidos para facilitar a manutenção.
 Calculadora de IMC com Interface Rich

Este projeto é uma aplicação de linha de comando (CLI) desenvolvida em Python que calcula o Índice de Massa Corporal (IMC). O diferencial desta ferramenta é a sua interface visual, que utiliza uma "régua colorida" para indicar graficamente a situação de saúde do usuário diretamente no terminal.
 Funcionalidades

    Cálculo Preciso: Calcula o IMC com base no peso e altura informados.

    Interface Visual: Renderiza uma barra de status colorida (Azul, Verde, Amarelo e Vermelho) para representar as categorias de peso.

    Ponteiro Dinâmico: Um marcador (▼) indica exatamente onde o seu IMC se encontra na régua.

    Multiplataforma: Função integrada para limpar o console tanto no Windows quanto no Linux/macOS.

    Loop de Interação: Permite realizar múltiplos cálculos sem fechar o programa.

🛠️ Tecnologias Utilizadas

    Python 3.14

    Rich: Biblioteca para formatação de texto e renderização de componentes visuais (painéis e cores) no terminal.

    Instalar dependências

Este projeto exige a biblioteca rich. Você pode instalá-la via pip:
Bash

pip install rich


Tabela de Referência
O programa utiliza as faixas padrão de classificação:

IMC,Classificação,Cor na Régua
Abaixo de 18.5,Abaixo do peso,Azul 🔵
18.5 - 24.9,Saudável,Verde 🟢
25.0 - 29.9,Sobrepeso,Amarelo 🟡
Acima de 30.0,Obesidade,Vermelho 🔴

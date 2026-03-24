🥩 Calculadora de Churrasco (POO & Rich)

Um script Python inteligente para planejar o churrasco com os amigos. Ele calcula a quantidade de carne necessária e o rateio de custos por pessoa, exibindo tudo em um painel visual no terminal.

## 🚀 Funcionalidades

* **Cálculo de Insumos:** Define a quantidade total de carne (em kg) baseada no número de convidados.
* **Rateio de Custos:** Calcula o valor total do evento e quanto cada participante deve contribuir.
* **Customização por Pessoa:** Permite ajustar a gramatura de carne consumida por pessoa (padrão de 400g).
* **Interface Colorida:** Utiliza a biblioteca `rich` para gerar relatórios organizados e fáceis de ler.

## 🛠️ Instalação

Você precisará da biblioteca `rich` instalada:

```bash
pip install rich

💻 Exemplo de Código

# Exemplo: 15 pessoas consumindo 400g cada
churras_pequeno = Churrasco(15, 400)
churras_pequeno.analisar()

# Exemplo: Grande evento com 200 pessoas consumindo 300g cada
evento_grande = Churrasco(200, 300)
evento_grande.analisar()
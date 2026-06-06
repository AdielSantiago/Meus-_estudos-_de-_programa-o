Sistema de Gerenciamento de Inventário em Python

Um sistema interativo de inventário para jogos de RPG desenvolvido em Python 3. O projeto utiliza funções modulares, contando com uma interface colorida renderizada diretamente no terminal através da biblioteca **Rich**.

---

## Funcionalidades

* **Adição Inteligente:** Permite adicionar itens informando o nome e a quantidade separados por vírgula (ex: `espada, 2`). Caso a quantidade seja omitida, o sistema assume automaticamente o valor `1`.
* **Redução de Itens:** Consome ou remove quantidades específicas de itens do inventário, com tratamento visual para sublinhados e cores.
* **Validação de Entradas (Anti-Crash):** Sistema protegido por blocos `try/except` que impede o fechamento do programa caso o usuário digite letras nas opções numéricas.
* **Interface Dinâmica:** Renderização automática de painéis utilizando a biblioteca Rich, limpando o terminal a cada ciclo para manter a tela sempre organizada.
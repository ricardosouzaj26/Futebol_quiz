# Futebol Quiz – Adivinhe a Data

Um jogo simples em **Python** onde o jogador deve **adivinhar a data (DDMMAAAA)** de acontecimentos marcantes do futebol a partir de dicas.


## Como funciona o jogo

1. O programa escolhe aleatoriamente um evento do futebol.
2. Uma dica é exibida (ex: título, conquista ou evento histórico).
3. O jogador deve digitar a data no formato **DDMMAAAA**.
4. O jogo mostra:
   - ✅ para cada dígito correto
   - ⬆️ quando o número digitado é **menor** que o correto  
   - ⬇️ quando o número digitado é **maior** que o correto  
5. O jogador tem **5 tentativas** para acertar a data completa.

---

## Como executar

1. Certifique-se de ter o Python 3 instalado
2. Clone o repositório ou baixe os arquivos, certifique-se de que o arquivo.json esteja na mesma pasta do arquivo.py  
```
 git clone https://github.com/ricardosouzaj26/futebol_quiz.git
```
3. No terminal, entre na pasta do projeto:
```
cd futebol_quiz
```   
Execute o jogo:
```
python futebol_quiz.py

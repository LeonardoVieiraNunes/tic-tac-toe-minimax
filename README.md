# Tic-Tac-Toe Minimax

Neste projeto, comparamos o desempenho de diferentes heurísticas em um algoritmo minimax para criar uma inteligência artificial (IA) que joga o jogo da velha. O objetivo é identificar qual heurística tem melhor desempenho e, portanto, é mais adequada para ser usada na IA do jogo da velha.

Abaixo as heurísticas utilizadas no projeto:

- Heurística de Possibilidades de Vitória: Avalia o número de possibilidades de vitória para cada jogador. Uma possibilidade de vitória é uma linha, coluna ou diagonal que não contém a marca do oponente.
- Heurística de Pontuação de Posição: Atribui uma pontuação a cada posição no tabuleiro e calcula a pontuação total para cada jogador com base na soma das pontuações das posições ocupadas por suas marcas.
- Heurística de Pontuação Simples: Utiliza a função de pontuação do jogo, que retorna uma pontuação fixa se o jogo for ganho (100 pontos).

Para mais informações e resultados, consulte o [relatório](relatorio.pdf)

## Instalação

### Pré-requisitos

- Python 3.6 ou superior

### Passos

1. Clone este repositório ou baixe o código-fonte:
```
https://github.com/LeonardoVieiraNunes/tic-tac-toe-minimax.git
```
2. Navegue até o diretório do projeto:
```
cd tic-tac-toe-minimax
```
3. Instale as dependências do projeto:
```
pip install -r requirements.txt
```
## Uso

### Executar a comparação entre as heurísticas
```
python tic_tac_toe_minimax.py
```
ou
```
python3 tic_tac_toe_minimax.py
```
Isso executará a função `compare_heuristics()` e exibirá os resultados no terminal.

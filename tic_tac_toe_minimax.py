from easyAI import TwoPlayerGame, AI_Player, TranspositionTable, Negamax
from easyAI.AI import TranspositionTable
from easyAI import solve_with_iterative_deepening
from easyAI.Player import AI_Player

class TicTacToe(TwoPlayerGame):
    def __init__(self, players):
        self.players = players
        self.board = [0] * 9
        self.current_player = 1

    def possible_moves(self):
        return [str(i) for i, cell in enumerate(self.board) if cell == 0]

    def make_move(self, move):
        self.board[int(move)] = self.current_player

    def win(self, player):
        winning_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                             (0, 3, 6), (1, 4, 7), (2, 5, 8),
                             (0, 4, 8), (2, 4, 6)]
        return any(all(self.board[pos] == player for pos in line) for line in winning_positions)

    def is_over(self):
        return (any(self.win(player) for player in [1, 2]) or
                all(cell != 0 for cell in self.board))

    def show(self):
        print("\n" + "\n".join(" ".join(str(self.board[i * 3 + j]) for j in range(3)) for i in range(3)))

    def play(self, display=True):
        if display:
                self.show()
        move_counter = 0
        while not self.is_over():
            move = self.player.ask_move(self)
            self.make_move(move)
            move_counter += 1
            self.switch_player()
            if display:
                self.show()

        return move_counter

def heuristic_scoring(game: TicTacToe):
    if game.win(2):
        return 100
    elif game.win(1):
        return -100
    else:
        return 0

def winning_possibilities_heuristic(game: TicTacToe):
    winning_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                         (0, 3, 6), (1, 4, 7), (2, 5, 8),
                         (0, 4, 8), (2, 4, 6)]
    player1_possibilities = sum(1 for line in winning_positions if all(game.board[pos] != 2 for pos in line))
    player2_possibilities = sum(1 for line in winning_positions if all(game.board[pos] != 1 for pos in line))
    return player2_possibilities - player1_possibilities

def position_score_heuristic(game: TicTacToe):
    position_scores = [3, 2, 3,
                       2, 4, 2,
                       3, 2, 3]
    player1_score = sum(position_scores[i] for i, cell in enumerate(game.board) if cell == 1)
    player2_score = sum(position_scores[i] for i, cell in enumerate(game.board) if cell == 2)
    return player2_score - player1_score

def compare_heuristics(heuristics, rounds=100):
    results = {i: 0 for i in range(1, len(heuristics) + 1)}
    results["draw"] = 0

    for _ in range(rounds):
        for i, heuristic1 in enumerate(heuristics, start=1):
            for j, heuristic2 in enumerate(heuristics[i:], start=i + 1):
                ai1 = Negamax(9, scoring=heuristic1)
                ai2 = Negamax(9, scoring=heuristic2)

                game1 = TicTacToe([AI_Player(ai1), AI_Player(ai2)])
                game1.play(display=False)

                game2 = TicTacToe([AI_Player(ai2), AI_Player(ai1)])
                game2.play(display=False)

                if game1.is_over() and not game1.win(1) and not game1.win(2):
                    results["draw"] += 1
                else:
                    results[game1.current_player] += 1

                if game2.is_over() and not game2.win(1) and not game2.win(2):
                    results["draw"] += 1
                else:
                    results[3 - game2.current_player] += 1

    return results

# Comparando as heurísticas
heuristic1 = winning_possibilities_heuristic
heuristic2 = position_score_heuristic
heuristic3 = heuristic_scoring  # Utilizando a heurística de pontuação simples

results = compare_heuristics([heuristic1, heuristic2, heuristic3], rounds=10)
print("Heurística 1 venceu:", results[1], "vezes")
print("Heurística 2 venceu:", results[2], "vezes")
print("Heurística 3 venceu:", results[3], "vezes")
print("Empates:", results["draw"])
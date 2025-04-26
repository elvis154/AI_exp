import numpy as np
import time
import random

class TicTacToe:
    def __init__(self, difficulty="hard"):
        self.board = np.zeros((3, 3), dtype=int)
        self.player = 1  # Player 1 ('X') starts
        self.difficulty = difficulty  # "easy" or "hard"

    def available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == 0]

    def make_move(self, position, player=None):
        if player is None:
            player = self.player
        row, col = position
        if self.board[row, col] != 0:
            return False
        self.board[row, col] = player
        self.player = -player
        return True

    def undo_move(self, position):
        row, col = position
        self.player = -self.player
        self.board[row, col] = 0

    def check_winner(self):
        for i in range(3):
            if abs(np.sum(self.board[i, :])) == 3:
                return self.board[i, 0]
            if abs(np.sum(self.board[:, i])) == 3:
                return self.board[0, i]
        if abs(np.sum([self.board[i, i] for i in range(3)])) == 3:
            return self.board[0, 0]
        if abs(np.sum([self.board[i, 2 - i] for i in range(3)])) == 3:
            return self.board[0, 2]
        if len(self.available_moves()) == 0:
            return 0
        return None

    def is_terminal(self):
        return self.check_winner() is not None

    def display_board(self):
        symbols = {1: 'X', -1: 'O', 0: ' '}
        print("\n")
        for i in range(3):
            print(" " + " | ".join([symbols[self.board[i, j]] for j in range(3)]))
            if i < 2:
                print("-" * 9)
        print("\n")

    def minimax(self, depth, is_maximizing, alpha=float('-inf'), beta=float('inf')):
        winner = self.check_winner()
        if winner is not None:
            return winner

        if is_maximizing:
            best_score = float('-inf')
            for move in self.available_moves():
                self.make_move(move, 1)
                score = self.minimax(depth + 1, False, alpha, beta)
                self.undo_move(move)
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return best_score
        else:
            best_score = float('inf')
            for move in self.available_moves():
                self.make_move(move, -1)
                score = self.minimax(depth + 1, True, alpha, beta)
                self.undo_move(move)
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
            return best_score

    def best_move(self, player):
        if self.difficulty == "easy" and random.random() < 0.7:
            available = self.available_moves()
            return random.choice(available) if available else None

        best_score = float('-inf') if player == 1 else float('inf')
        best_move = None

        for move in self.available_moves():
            self.make_move(move, player)
            score = self.minimax(0, player != 1)
            self.undo_move(move)

            if (player == 1 and score > best_score) or (player == -1 and score < best_score):
                best_score = score
                best_move = move

        return best_move


def play_game():
    print("Select game mode:")
    print("1. Human vs Computer (Human goes first - Easy)")
    print("2. Human vs Computer (Human goes first - Hard)")
    print("3. Computer vs Human (Computer goes first)")
    print("4. Computer vs Computer")

    while True:
        try:
            mode = int(input("Enter mode (1-4): "))
            if mode in [1, 2, 3, 4]:
                break
            else:
                print("Please enter a valid mode (1-4).")
        except ValueError:
            print("Please enter a number (1-4).")

    difficulty = "easy" if mode == 1 else "hard"
    game = TicTacToe(difficulty)
    current_player = 1

    while not game.is_terminal():
        game.display_board()

        if (mode in [1, 2] and current_player == 1) or (mode == 3 and current_player == -1):
            print(f"Player {'X' if current_player == 1 else 'O'}'s turn")
            while True:
                try:
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter column (0-2): "))
                    if 0 <= row <= 2 and 0 <= col <= 2 and game.board[row, col] == 0:
                        break
                    else:
                        print("Invalid move. Please try again.")
                except ValueError:
                    print("Please enter valid numbers.")
            game.make_move((row, col), current_player)
        else:
            print(f"Computer ({'X' if current_player == 1 else 'O'}) is thinking... [{game.difficulty.capitalize()} mode]")
            time.sleep(1)
            move = game.best_move(current_player)
            print(f"Computer plays at position: {move}")
            game.make_move(move, current_player)

        current_player = -current_player

    game.display_board()
    winner = game.check_winner()
    if winner == 1:
        print("X wins!")
    elif winner == -1:
        print("O wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    play_game()

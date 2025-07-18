import math
import time

class TicTacToe:
    def __init__(self):
        self.human = 'X'
        self.ai = 'O'
        self.current_player = self.human
        self.reset_board()

    def reset_board(self):
        self.board = [[None]*3 for _ in range(3)]
        self.game_over = False

    def print_board(self):
        print("\n   0   1   2")
        for i in range(3):
            row = [self.board[i][j] if self.board[i][j] else ' ' for j in range(3)]
            print(f"{i}  {row[0]} | {row[1]} | {row[2]}")
            if i < 2:
                print("  ---+---+---")

    def get_available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if not self.board[i][j]]

    def is_valid_move(self, r, c):
        return 0 <= r < 3 and 0 <= c < 3 and self.board[r][c] is None

    def make_move(self, r, c, player):
        self.board[r][c] = player

    def undo_move(self, r, c):
        self.board[r][c] = None

    def check_winner(self):
        lines = self.board + list(zip(*self.board))
        lines.append([self.board[i][i] for i in range(3)])
        lines.append([self.board[i][2 - i] for i in range(3)])
        for line in lines:
            if line[0] and line.count(line[0]) == 3:
                return line[0]
        if not self.get_available_moves():
            return 'Draw'
        return None

    def evaluate(self):
        winner = self.check_winner()
        if winner == self.ai:
            return 10
        elif winner == self.human:
            return -10
        return 0

    def minimax(self, depth, is_max, alpha, beta):
        score = self.evaluate()
        if score != 0 or not self.get_available_moves():
            return score

        if is_max:
            max_eval = -math.inf
            for r, c in self.get_available_moves():
                self.make_move(r, c, self.ai)
                eval = self.minimax(depth + 1, False, alpha, beta)
                self.undo_move(r, c)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for r, c in self.get_available_moves():
                self.make_move(r, c, self.human)
                eval = self.minimax(depth + 1, True, alpha, beta)
                self.undo_move(r, c)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def best_move(self):
        print("🤖 AI is thinking...")
        start = time.time()
        best_score, move = -math.inf, None
        for r, c in self.get_available_moves():
            self.make_move(r, c, self.ai)
            score = self.minimax(0, False, -math.inf, math.inf)
            self.undo_move(r, c)
            if score > best_score:
                best_score, move = score, (r, c)
        print(f"⏱️ Done in {time.time() - start:.2f}s")
        return move

    def user_setup(self):
        choice = input("Do you want to be 'X' or 'O'? ").upper()
        if choice == 'O':
            self.human, self.ai = 'O', 'X'
        turn = input("Do you want to go first? (y/n): ").lower()
        if turn.startswith('n'):
            self.current_player = self.ai
        else:
            self.current_player = self.human

    def play(self):
        print("🎮 Welcome to Tic-Tac-Toe with AI!")
        self.user_setup()
        while True:
            self.reset_board()
            self.print_board()

            while not self.game_over:
                if self.current_player == self.human:
                    while True:
                        try:
                            move = input("Your move (row col): ")
                            r, c = map(int, move.split())
                            if self.is_valid_move(r, c):
                                self.make_move(r, c, self.human)
                                break
                            print("❌ Invalid move. Try again.")
                        except:
                            print("⚠️ Enter in format: row col (e.g. 0 2)")
                else:
                    r, c = self.best_move()
                    self.make_move(r, c, self.ai)
                    print(f"🤖 AI moved to {r}, {c}")

                self.print_board()
                winner = self.check_winner()
                if winner:
                    self.game_over = True
                    if winner == 'Draw':
                        print("🤝 It's a draw!")
                    else:
                        print(f"🎉 {winner} wins!")
                    break

                self.current_player = self.human if self.current_player == self.ai else self.ai

            again = input("\n🔁 Do you want to play again? (y/n): ").lower()
            if again.startswith('n'):
                print("👋 Thanks for playing!")
                break
            else:
                self.user_setup()

if __name__ == "__main__":
    TicTacToe().play()

class TicTacToe:
    def __init__(self, name, x, o):
        self.name = name  # Name of the game
        self.players = {'X': x, 'O': o}  # Players assigned to X and O
        self.board = [" " for _ in range(9)]  # Create an empty board

    def display_board(self):
        print("-------------")
        print("|", self.board[0], "|", self.board[1], "|", self.board[2], "|")
        print("-------------")
        print("|", self.board[3], "|", self.board[4], "|", self.board[5], "|")
        print("-------------")
        print("|", self.board[6], "|", self.board[7], "|", self.board[8], "|")
        print("-------------")

    def play_game(self):
        print(f"Welcome to {self.name}!")
        print(f"Player 1 ({self.players['X']}): X")
        print(f"Player 2 ({self.players['O']}): O")
        print("Let's begin!")

        current_player = 'X'  # Assume 'X' starts the game

        while True:
            self.display_board()
            position = int(input(f"{self.players[current_player]}, enter a position (1-9): ")) - 1

            if self.board[position] != ' ':
                print("Invalid move! Position already taken. Try again.")
                continue

            self.board[position] = current_player

            # Check for a winner or a tie

            # Switch to the other player
            current_player = 'O' if current_player == 'X' else 'X'

# Example usage
game = TicTacToe("Tic-Tac-Toe Game", "Player 1", "Player 2")
game.play_game()

"""
Tic-Tac-Toe Game with Minimax AI
An implementation of adversarial search for game playing
"""

import math
import copy

# Constants
X = "X"
O = "O"
EMPTY = None


class TicTacToe:
    """Tic-Tac-Toe game with Minimax AI"""
    
    def __init__(self):
        """Initialize the game board"""
        self.board = [[EMPTY, EMPTY, EMPTY],
                      [EMPTY, EMPTY, EMPTY],
                      [EMPTY, EMPTY, EMPTY]]
    
    def get_player(self):
        """Return which player's turn it is (X or O)"""
        x_count = sum(row.count(X) for row in self.board)
        o_count = sum(row.count(O) for row in self.board)
        return X if x_count == o_count else O
    
    def get_actions(self):
        """Return set of all possible actions (i, j) available"""
        actions = set()
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == EMPTY:
                    actions.add((i, j))
        return actions
    
    def result(self, action):
        """Return the board that results from making move (i, j)"""
        if action not in self.get_actions():
            raise ValueError("Invalid action")
        
        i, j = action
        new_board = copy.deepcopy(self.board)
        new_board[i][j] = self.get_player()
        
        new_game = TicTacToe()
        new_game.board = new_board
        return new_game
    
    def winner(self):
        """Return the winner if there is one, else None"""
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] is not EMPTY:
                return row[0]
        
        # Check columns
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] and self.board[0][j] is not EMPTY:
                return self.board[0][j]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not EMPTY:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not EMPTY:
            return self.board[0][2]
        
        return None
    
    def terminal(self):
        """Return True if game is over, False otherwise"""
        if self.winner() is not None:
            return True
        
        # Check if board is full
        for row in self.board:
            if EMPTY in row:
                return False
        return True
    
    def utility(self):
        """Return 1 if X wins, -1 if O wins, 0 for tie"""
        winner = self.winner()
        if winner == X:
            return 1
        elif winner == O:
            return -1
        else:
            return 0
    
    def minimax(self):
        """Return the optimal action for the current player"""
        if self.terminal():
            return None
        
        player = self.get_player()
        
        if player == X:
            # X wants to maximize score
            value = -math.inf
            best_action = None
            
            for action in self.get_actions():
                new_game = self.result(action)
                action_value = self._min_value(new_game)
                
                if action_value > value:
                    value = action_value
                    best_action = action
            
            return best_action
        
        else:
            # O wants to minimize score
            value = math.inf
            best_action = None
            
            for action in self.get_actions():
                new_game = self.result(action)
                action_value = self._max_value(new_game)
                
                if action_value < value:
                    value = action_value
                    best_action = action
            
            return best_action
    
    def _max_value(self, game):
        """Helper function for minimax - maximize"""
        if game.terminal():
            return game.utility()
        
        v = -math.inf
        for action in game.get_actions():
            v = max(v, self._min_value(game.result(action)))
        return v
    
    def _min_value(self, game):
        """Helper function for minimax - minimize"""
        if game.terminal():
            return game.utility()
        
        v = math.inf
        for action in game.get_actions():
            v = min(v, self._max_value(game.result(action)))
        return v
    
    def print_board(self):
        """Print the board"""
        for i, row in enumerate(self.board):
            row_str = " | ".join([cell if cell else " " for cell in row])
            print(f" {row_str} ")
            if i < 2:
                print("-----------")
    
    def make_move(self, action):
        """Make a move on the current board"""
        if action not in self.get_actions():
            raise ValueError("Invalid action")
        
        i, j = action
        self.board[i][j] = self.get_player()


def play_game():
    """Play a game of Tic-Tac-Toe"""
    game = TicTacToe()
    
    print("=== Tic-Tac-Toe with Minimax AI ===\n")
    print("You are O, AI is X")
    print("Positions: (0,0) is top-left, (2,2) is bottom-right\n")
    
    while not game.terminal():
        game.print_board()
        print()
        
        player = game.get_player()
        
        if player == X:
            print("AI is thinking...")
            action = game.minimax()
            print(f"AI plays: {action}")
        else:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
                action = (row, col)
            except (ValueError, IndexError):
                print("Invalid input. Try again.")
                continue
        
        try:
            game.make_move(action)
        except ValueError:
            print("Invalid move. Try again.")
            continue
        
        print()
    
    # Game over
    game.print_board()
    print()
    
    winner = game.winner()
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a tie!")


def demo_ai_vs_ai():
    """Demo game where AI plays against itself"""
    print("\n=== AI vs AI Demo ===\n")
    
    game = TicTacToe()
    move_count = 0
    
    while not game.terminal():
        print(f"Move {move_count + 1}:")
        game.print_board()
        print()
        
        action = game.minimax()
        print(f"{game.get_player()} plays: {action}\n")
        game.make_move(action)
        move_count += 1
    
    game.print_board()
    print()
    
    winner = game.winner()
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a tie! (As expected with perfect play)")


if __name__ == "__main__":
    # Uncomment to play against AI
    # play_game()
    
    # Demo: AI vs AI
    demo_ai_vs_ai()

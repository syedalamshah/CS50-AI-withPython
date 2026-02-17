# Tic-Tac-Toe with Minimax AI

An implementation of the Minimax algorithm for playing Tic-Tac-Toe optimally.

## Concepts Demonstrated

- **Adversarial Search**: Finding optimal moves in competitive games
- **Minimax Algorithm**: Maximizing player's score while minimizing opponent's
- **Game Trees**: Exploring all possible game states
- **Zero-Sum Games**: One player's gain is another's loss

## How It Works

The Minimax algorithm:
1. Explores all possible future game states
2. Assumes both players play optimally
3. X (maximizing player) tries to get score of 1
4. O (minimizing player) tries to get score of -1
5. Returns the best move for current player

## Running the Game

```bash
python tictactoe.py
```

By default, runs an AI vs AI demo showing perfect play.

To play against the AI, edit `tictactoe.py` and uncomment:
```python
play_game()
```

## Game Rules

- Board positions: (row, col) from (0,0) to (2,2)
- X always goes first
- Win by getting 3 in a row (horizontal, vertical, or diagonal)
- With perfect play, the game always ends in a tie

## Algorithm Details

**Max-Value**: Returns the best score X can achieve
- If terminal: return utility
- Maximize over all possible actions

**Min-Value**: Returns the best score O can achieve  
- If terminal: return utility
- Minimize over all possible actions

**Complexity**: O(b^m) where b is branching factor, m is max depth
- Tic-Tac-Toe: manageable since board is small (3x3)

## Enhancements

Possible improvements:
- Alpha-Beta Pruning for efficiency
- Depth-limited search for larger games
- Evaluation functions for non-terminal states
- Opening book for faster early moves

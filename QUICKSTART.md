# Quick Start Guide

Get started with AI fundamentals in minutes!

## Installation

```bash
# Clone the repository
git clone https://github.com/syedalamshah/CS50-AI-withPython.git
cd CS50-AI-withPython

# (Optional) Install dependencies for advanced features
pip install -r requirements.txt
```

## Try the Examples

### 1. Search Algorithms (5 minutes)

See how different search algorithms solve mazes:

```bash
python3 search/maze_solver.py
```

You'll see:
- DFS finding a solution (not optimal)
- BFS finding the shortest path
- Greedy Best-First using heuristics
- A* combining cost and heuristics

### 2. Logic and Knowledge (3 minutes)

Solve logic puzzles with propositional logic:

```bash
python3 knowledge/logic_examples.py
```

Solves:
- Knights and Knaves puzzles
- Weather inference problems

### 3. Optimization (5 minutes)

Watch AI solve the N-Queens problem:

```bash
python3 optimization/nqueens_example.py
```

Compares:
- Hill Climbing (can get stuck)
- Simulated Annealing (escapes local maxima)

### 4. Machine Learning (3 minutes)

See basic ML algorithms in action:

```bash
python3 learning/ml_examples.py
```

Demonstrates:
- K-Nearest Neighbors classification
- Linear Regression prediction

### 5. Neural Networks (2 minutes)

Train a perceptron to learn logic gates:

```bash
python3 neural_networks/perceptron_example.py
```

Learns:
- AND gate
- OR gate
- Why XOR needs multiple layers

### 6. Game Playing (3 minutes)

Watch AI play perfect Tic-Tac-Toe:

```bash
python3 projects/tictactoe/tictactoe.py
```

Uses Minimax algorithm for optimal play.

## Learning Path

### Beginner
1. Start with **Search** - understand how AI explores problems
2. Try **Optimization** - see how AI finds good solutions
3. Experiment with **Machine Learning** - learn from data

### Intermediate
4. Study **Knowledge** - represent and reason with logic
5. Explore **Neural Networks** - building blocks of deep learning
6. Build **Projects** - combine concepts

## Next Steps

- Modify the examples to understand how they work
- Change parameters and see what happens
- Read the module READMEs for detailed explanations
- Build your own AI projects using these as templates

## Getting Help

- Check individual module READMEs for detailed docs
- Review the main README for comprehensive overview
- Explore the CS50 AI course materials
- Experiment and learn by doing!

## Common Issues

**Import errors?**
- Make sure you're running from the repository root
- Python 3.8+ required

**Missing dependencies?**
- Most examples work without external dependencies
- For advanced features: `pip install -r requirements.txt`

Happy Learning! 🚀

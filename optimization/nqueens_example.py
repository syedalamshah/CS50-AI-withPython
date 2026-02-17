"""
Example: Solving optimization problems
N-Queens problem using hill climbing and simulated annealing
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random
from optimization import hill_climbing, simulated_annealing


class NQueens:
    """
    N-Queens problem: Place N queens on NxN board with no conflicts.
    """
    
    def __init__(self, n):
        self.n = n
    
    def random_state(self):
        """Generate random state (one queen per column)"""
        return [random.randint(0, self.n - 1) for _ in range(self.n)]
    
    def conflicts(self, state):
        """Count number of queen conflicts"""
        conflicts = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                # Same row
                if state[i] == state[j]:
                    conflicts += 1
                # Same diagonal
                if abs(state[i] - state[j]) == abs(i - j):
                    conflicts += 1
        return conflicts
    
    def value(self, state):
        """Evaluate state (fewer conflicts is better)"""
        # Return negative conflicts so higher is better
        return -self.conflicts(state)
    
    def neighbors(self, state):
        """Generate all neighbor states (move one queen in its column)"""
        neighbors = []
        for col in range(self.n):
            for row in range(self.n):
                if row != state[col]:
                    neighbor = state.copy()
                    neighbor[col] = row
                    neighbors.append(neighbor)
        return neighbors
    
    def print_board(self, state):
        """Print the board"""
        for row in range(self.n):
            line = ""
            for col in range(self.n):
                if state[col] == row:
                    line += "Q "
                else:
                    line += ". "
            print(line)


def solve_nqueens_hill_climbing(n=8):
    """Solve N-Queens using hill climbing"""
    print(f"=== Solving {n}-Queens with Hill Climbing ===\n")
    
    problem = NQueens(n)
    initial = problem.random_state()
    
    print("Initial state:")
    problem.print_board(initial)
    print(f"Conflicts: {problem.conflicts(initial)}\n")
    
    solution = hill_climbing(
        initial,
        problem.neighbors,
        problem.value,
        max_iterations=1000
    )
    
    print("Final state:")
    problem.print_board(solution)
    print(f"Conflicts: {problem.conflicts(solution)}")
    
    if problem.conflicts(solution) == 0:
        print("✓ Solution found!")
    else:
        print("✗ Stuck at local maximum")
    
    return solution


def solve_nqueens_simulated_annealing(n=8):
    """Solve N-Queens using simulated annealing"""
    print(f"\n\n=== Solving {n}-Queens with Simulated Annealing ===\n")
    
    problem = NQueens(n)
    initial = problem.random_state()
    
    print("Initial state:")
    problem.print_board(initial)
    print(f"Conflicts: {problem.conflicts(initial)}\n")
    
    solution = simulated_annealing(
        initial,
        problem.neighbors,
        problem.value,
        temperature=100,
        cooling_rate=0.99
    )
    
    print("Final state:")
    problem.print_board(solution)
    print(f"Conflicts: {problem.conflicts(solution)}")
    
    if problem.conflicts(solution) == 0:
        print("✓ Solution found!")
    else:
        print("✗ Did not find perfect solution")
    
    return solution


def main():
    """Run optimization examples"""
    solve_nqueens_hill_climbing(8)
    solve_nqueens_simulated_annealing(8)


if __name__ == "__main__":
    main()

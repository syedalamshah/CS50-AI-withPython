"""
Example usage of search algorithms to solve a maze
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from search import Maze, dfs, bfs, greedy_best_first, a_star


def main():
    """
    Demonstrate different search algorithms on a maze.
    """
    # Create a simple maze
    print("Creating maze...")
    maze = Maze()
    
    print("\nOriginal Maze:")
    maze.print_maze()
    
    # Test DFS
    print("\n\n=== Depth-First Search ===")
    solution = dfs(maze)
    if solution:
        print(f"Solution found with {len(solution)} steps")
        maze.print_maze(solution)
    else:
        print("No solution found")
    
    # Test BFS
    print("\n\n=== Breadth-First Search ===")
    solution = bfs(maze)
    if solution:
        print(f"Solution found with {len(solution)} steps")
        maze.print_maze(solution)
    else:
        print("No solution found")
    
    # Test Greedy Best-First
    print("\n\n=== Greedy Best-First Search ===")
    solution = greedy_best_first(maze)
    if solution:
        print(f"Solution found with {len(solution)} steps")
        maze.print_maze(solution)
    else:
        print("No solution found")
    
    # Test A*
    print("\n\n=== A* Search ===")
    solution = a_star(maze)
    if solution:
        print(f"Solution found with {len(solution)} steps")
        maze.print_maze(solution)
    else:
        print("No solution found")


if __name__ == "__main__":
    main()

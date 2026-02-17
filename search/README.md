# Search Algorithms

This module implements fundamental search algorithms used in AI for problem-solving and pathfinding.

## Algorithms Implemented

### 1. Depth-First Search (DFS)
- Uses a stack (LIFO) structure
- Explores as deep as possible before backtracking
- Not guaranteed to find shortest path
- Memory efficient

### 2. Breadth-First Search (BFS)
- Uses a queue (FIFO) structure
- Explores all neighbors before going deeper
- Guarantees shortest path (unweighted graphs)
- More memory intensive than DFS

### 3. Greedy Best-First Search
- Uses a priority queue with heuristic function
- Always expands the node closest to goal
- Fast but not optimal
- Uses Manhattan distance as heuristic

### 4. A* Search
- Uses f(n) = g(n) + h(n) where:
  - g(n) = cost from start to n
  - h(n) = estimated cost from n to goal
- Guarantees optimal solution
- Efficient with good heuristic

## Usage

```python
from search import Maze, dfs, bfs, greedy_best_first, a_star

# Create a maze
maze = Maze()

# Solve using different algorithms
solution_dfs = dfs(maze)
solution_bfs = bfs(maze)
solution_gbf = greedy_best_first(maze)
solution_astar = a_star(maze)

# Display solution
maze.print_maze(solution_astar)
```

## Running the Example

```bash
python maze_solver.py
```

## Maze Format

Mazes are defined using text files:
- `A` = Start position
- `B` = Goal position  
- `#` = Wall
- ` ` = Empty space

Example:
```
###############
#A            #
#   #####  #  #
#   #      #  #
#   #  #####  #
#      #      #
########      B
###############
```

## Key Concepts

- **State Space**: All possible configurations
- **Actions**: Moves that change state (up, down, left, right)
- **Goal Test**: Check if current state is goal
- **Path Cost**: Number of steps taken
- **Heuristic**: Estimated cost to reach goal (Manhattan distance)

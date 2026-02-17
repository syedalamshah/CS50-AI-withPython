"""
Maze class for representing and solving maze problems
"""

class Maze:
    """
    A maze environment for pathfinding algorithms.
    """
    
    def __init__(self, filename=None):
        """
        Initialize a maze from a file.
        
        File format:
        - 'A' marks the start
        - 'B' marks the goal
        - '#' marks walls
        - ' ' marks empty spaces
        """
        if filename:
            with open(filename, 'r') as f:
                contents = f.read()
        else:
            # Default simple maze
            contents = """###############
#A            #
#   #####  #  #
#   #      #  #
#   #  #####  #
#      #      #
########      B
###############"""
        
        # Validate and parse maze
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)
        
        # Keep track of walls, start, and goal
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == 'A':
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == 'B':
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == ' ':
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)
        
        self.solution = None
    
    def neighbors(self, state):
        """
        Returns possible actions and resulting states from current state.
        
        Args:
            state: Current position (row, col)
            
        Returns:
            List of (action, new_state) tuples
        """
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]
        
        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result
    
    def print_maze(self, solution=None):
        """
        Print the maze with optional solution path.
        """
        solution_coords = set()
        if solution:
            for action, state in solution:
                solution_coords.add(state)
        
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif (i, j) in solution_coords:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

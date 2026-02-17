"""
Search Algorithms Implementation
Includes DFS, BFS, Greedy Best-First Search, and A* Search
"""

from collections import deque
import heapq
from .node import Node


def dfs(maze):
    """
    Depth-First Search algorithm.
    Uses a stack (LIFO) to explore states.
    
    Args:
        maze: Maze object with start, goal, and neighbors method
        
    Returns:
        List of (action, state) tuples representing the solution path
        or None if no solution exists
    """
    start = Node(state=maze.start, parent=None, action=None)
    frontier = [start]  # Stack
    explored = set()
    
    while frontier:
        node = frontier.pop()
        
        if node.state == maze.goal:
            # Reconstruct path
            actions = []
            states = []
            while node.parent is not None:
                actions.append(node.action)
                states.append(node.state)
                node = node.parent
            actions.reverse()
            states.reverse()
            return list(zip(actions, states))
        
        explored.add(node.state)
        
        for action, state in maze.neighbors(node.state):
            if state not in explored and not any(n.state == state for n in frontier):
                child = Node(state=state, parent=node, action=action)
                frontier.append(child)
    
    return None


def bfs(maze):
    """
    Breadth-First Search algorithm.
    Uses a queue (FIFO) to explore states.
    
    Args:
        maze: Maze object with start, goal, and neighbors method
        
    Returns:
        List of (action, state) tuples representing the solution path
        or None if no solution exists
    """
    start = Node(state=maze.start, parent=None, action=None)
    frontier = deque([start])  # Queue
    explored = set()
    
    while frontier:
        node = frontier.popleft()
        
        if node.state == maze.goal:
            # Reconstruct path
            actions = []
            states = []
            while node.parent is not None:
                actions.append(node.action)
                states.append(node.state)
                node = node.parent
            actions.reverse()
            states.reverse()
            return list(zip(actions, states))
        
        explored.add(node.state)
        
        for action, state in maze.neighbors(node.state):
            if state not in explored and not any(n.state == state for n in frontier):
                child = Node(state=state, parent=node, action=action)
                frontier.append(child)
    
    return None


def manhattan_distance(state1, state2):
    """
    Calculate Manhattan distance heuristic between two states.
    
    Args:
        state1: (row, col) tuple
        state2: (row, col) tuple
        
    Returns:
        Manhattan distance as integer
    """
    return abs(state1[0] - state2[0]) + abs(state1[1] - state2[1])


def greedy_best_first(maze):
    """
    Greedy Best-First Search algorithm.
    Uses a priority queue ordered by heuristic value.
    
    Args:
        maze: Maze object with start, goal, and neighbors method
        
    Returns:
        List of (action, state) tuples representing the solution path
        or None if no solution exists
    """
    start = Node(state=maze.start, parent=None, action=None, cost=0)
    frontier = []
    heapq.heappush(frontier, (manhattan_distance(maze.start, maze.goal), start))
    explored = set()
    
    while frontier:
        _, node = heapq.heappop(frontier)
        
        if node.state == maze.goal:
            # Reconstruct path
            actions = []
            states = []
            while node.parent is not None:
                actions.append(node.action)
                states.append(node.state)
                node = node.parent
            actions.reverse()
            states.reverse()
            return list(zip(actions, states))
        
        explored.add(node.state)
        
        for action, state in maze.neighbors(node.state):
            if state not in explored:
                child = Node(state=state, parent=node, action=action)
                h = manhattan_distance(state, maze.goal)
                heapq.heappush(frontier, (h, child))
    
    return None


def a_star(maze):
    """
    A* Search algorithm.
    Uses a priority queue ordered by f(n) = g(n) + h(n).
    
    Args:
        maze: Maze object with start, goal, and neighbors method
        
    Returns:
        List of (action, state) tuples representing the solution path
        or None if no solution exists
    """
    start = Node(state=maze.start, parent=None, action=None, cost=0)
    h_start = manhattan_distance(maze.start, maze.goal)
    frontier = []
    heapq.heappush(frontier, (h_start, start))
    explored = set()
    
    # Keep track of best cost to reach each state
    best_cost = {maze.start: 0}
    
    while frontier:
        _, node = heapq.heappop(frontier)
        
        if node.state == maze.goal:
            # Reconstruct path
            actions = []
            states = []
            while node.parent is not None:
                actions.append(node.action)
                states.append(node.state)
                node = node.parent
            actions.reverse()
            states.reverse()
            return list(zip(actions, states))
        
        explored.add(node.state)
        
        for action, state in maze.neighbors(node.state):
            new_cost = node.cost + 1
            
            if state not in explored and (state not in best_cost or new_cost < best_cost[state]):
                best_cost[state] = new_cost
                child = Node(state=state, parent=node, action=action, cost=new_cost)
                h = manhattan_distance(state, maze.goal)
                f = new_cost + h
                heapq.heappush(frontier, (f, child))
    
    return None

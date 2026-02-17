"""
Hill Climbing Algorithm
Local search optimization technique
"""

import random


def hill_climbing(initial_state, neighbors_func, value_func, max_iterations=10000):
    """
    Hill climbing optimization algorithm.
    
    Args:
        initial_state: Starting state
        neighbors_func: Function that returns neighbor states
        value_func: Function that evaluates state quality (higher is better)
        max_iterations: Maximum number of iterations
        
    Returns:
        Best state found
    """
    current = initial_state
    current_value = value_func(current)
    
    for i in range(max_iterations):
        neighbors = neighbors_func(current)
        
        if not neighbors:
            break
        
        # Find best neighbor
        best_neighbor = max(neighbors, key=value_func)
        best_value = value_func(best_neighbor)
        
        # If no neighbor is better, we've reached a local maximum
        if best_value <= current_value:
            break
        
        current = best_neighbor
        current_value = best_value
    
    return current


def random_restart_hill_climbing(initial_state_func, neighbors_func, value_func, 
                                 num_restarts=10, max_iterations=1000):
    """
    Hill climbing with random restarts to escape local maxima.
    
    Args:
        initial_state_func: Function that generates random initial state
        neighbors_func: Function that returns neighbor states
        value_func: Function that evaluates state quality
        num_restarts: Number of random restarts
        max_iterations: Maximum iterations per restart
        
    Returns:
        Best state found across all restarts
    """
    best_state = None
    best_value = float('-inf')
    
    for _ in range(num_restarts):
        initial = initial_state_func()
        result = hill_climbing(initial, neighbors_func, value_func, max_iterations)
        result_value = value_func(result)
        
        if result_value > best_value:
            best_state = result
            best_value = result_value
    
    return best_state

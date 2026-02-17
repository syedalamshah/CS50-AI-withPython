"""
Simulated Annealing Algorithm
Probabilistic optimization technique
"""

import random
import math


def simulated_annealing(initial_state, neighbors_func, value_func, 
                       temperature=10000, cooling_rate=0.95, min_temperature=1):
    """
    Simulated annealing optimization algorithm.
    
    Accepts worse solutions with probability that decreases over time,
    allowing escape from local maxima.
    
    Args:
        initial_state: Starting state
        neighbors_func: Function that returns neighbor states
        value_func: Function that evaluates state quality (higher is better)
        temperature: Initial temperature
        cooling_rate: Rate at which temperature decreases (0 < rate < 1)
        min_temperature: Minimum temperature (stopping condition)
        
    Returns:
        Best state found
    """
    current = initial_state
    current_value = value_func(current)
    best = current
    best_value = current_value
    
    while temperature > min_temperature:
        neighbors = neighbors_func(current)
        
        if not neighbors:
            break
        
        # Pick random neighbor
        neighbor = random.choice(neighbors)
        neighbor_value = value_func(neighbor)
        
        # Calculate change in value
        delta = neighbor_value - current_value
        
        # Accept better solutions always, worse solutions with probability
        if delta > 0:
            current = neighbor
            current_value = neighbor_value
            
            # Update best if this is better
            if current_value > best_value:
                best = current
                best_value = current_value
        else:
            # Accept worse solution with probability e^(delta/temperature)
            probability = math.exp(delta / temperature)
            if random.random() < probability:
                current = neighbor
                current_value = neighbor_value
        
        # Cool down
        temperature *= cooling_rate
    
    return best


def acceptance_probability(current_value, neighbor_value, temperature):
    """
    Calculate probability of accepting a worse solution.
    
    Args:
        current_value: Value of current state
        neighbor_value: Value of neighbor state
        temperature: Current temperature
        
    Returns:
        Probability of acceptance (0 to 1)
    """
    if neighbor_value > current_value:
        return 1.0
    
    delta = neighbor_value - current_value
    return math.exp(delta / temperature)

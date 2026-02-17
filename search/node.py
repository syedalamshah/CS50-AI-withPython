"""
Node class for representing states in search problems
"""

class Node:
    """
    A node in a search tree. Contains a state, parent node, and action taken.
    """
    
    def __init__(self, state, parent=None, action=None, cost=0):
        """
        Initialize a node with a state, parent, action, and cost.
        
        Args:
            state: The state represented by this node
            parent: The parent node that led to this node
            action: The action taken to reach this node
            cost: The path cost from the initial state to this node
        """
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
    
    def __repr__(self):
        return f"Node(state={self.state}, cost={self.cost})"
    
    def __lt__(self, other):
        """Comparison for priority queue"""
        return self.cost < other.cost

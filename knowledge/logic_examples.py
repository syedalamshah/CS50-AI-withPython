"""
Example: Using propositional logic to solve logic puzzles
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from knowledge import Symbol, And, Or, Not, Implication, KnowledgeBase


def knights_and_knaves():
    """
    Knights and Knaves puzzle:
    - Knights always tell the truth
    - Knaves always lie
    
    Puzzle: A says "I am a knight" or "B is a knave"
    """
    print("=== Knights and Knaves Puzzle ===\n")
    
    # Create symbols
    A_knight = Symbol("A is a knight")
    B_knight = Symbol("B is a knight")
    
    # Create knowledge base
    kb = KnowledgeBase()
    
    # A says: "I am a knight or B is a knave"
    statement = Or(A_knight, Not(B_knight))
    
    # If A is a knight, the statement is true
    # If A is a knave, the statement is false
    kb.tell(Implication(A_knight, statement))
    kb.tell(Implication(Not(A_knight), Not(statement)))
    
    # Query: Is A a knight?
    print(f"Statement by A: {statement.formula()}")
    print(f"\nIs A a knight? {kb.ask(A_knight)}")
    print(f"Is B a knight? {kb.ask(B_knight)}")


def weather_inference():
    """
    Weather inference example:
    - If it's raining, then the ground is wet
    - If the ground is wet, then the grass is slippery
    - It is raining
    """
    print("\n\n=== Weather Inference ===\n")
    
    # Create symbols
    raining = Symbol("raining")
    ground_wet = Symbol("ground_wet")
    grass_slippery = Symbol("grass_slippery")
    
    # Create knowledge base
    kb = KnowledgeBase()
    
    # Add rules
    kb.tell(Implication(raining, ground_wet))
    kb.tell(Implication(ground_wet, grass_slippery))
    kb.tell(raining)  # Fact: it is raining
    
    # Queries
    print("Knowledge:")
    print("- If it's raining, then the ground is wet")
    print("- If the ground is wet, then the grass is slippery")
    print("- It is raining")
    
    print("\nQueries:")
    print(f"Is the ground wet? {kb.ask(ground_wet)}")
    print(f"Is the grass slippery? {kb.ask(grass_slippery)}")


def main():
    """Run logic examples"""
    knights_and_knaves()
    weather_inference()


if __name__ == "__main__":
    main()

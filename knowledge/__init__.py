"""
Knowledge Representation Module
Implements propositional logic and inference
"""

from .logic import Symbol, Not, And, Or, Implication, Biconditional
from .knowledge_base import KnowledgeBase

__all__ = ['Symbol', 'Not', 'And', 'Or', 'Implication', 'Biconditional', 'KnowledgeBase']

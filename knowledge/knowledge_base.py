"""
Knowledge Base for storing and reasoning with logical sentences
"""

import itertools


class KnowledgeBase:
    """
    A knowledge base for propositional logic.
    Stores sentences and can perform inference.
    """
    
    def __init__(self):
        self.sentences = []
    
    def tell(self, sentence):
        """Add a sentence to the knowledge base"""
        self.sentences.append(sentence)
    
    def ask(self, query):
        """
        Check if query can be inferred from knowledge base.
        Uses model checking (exhaustive enumeration).
        """
        symbols = set()
        for sentence in self.sentences:
            symbols = symbols.union(sentence.symbols())
        symbols = symbols.union(query.symbols())
        
        return self._check_all(query, symbols, {})
    
    def _check_all(self, query, symbols, model):
        """
        Check if KB entails query using all possible models.
        """
        # If no more symbols, check if model satisfies KB and query
        if not symbols:
            # If KB is true in model, then query must also be true
            if self._kb_true(model):
                return query.evaluate(model)
            return True
        
        # Choose one symbol
        symbol = symbols.pop()
        
        # Try with symbol = True
        model_true = model.copy()
        model_true[symbol] = True
        
        # Try with symbol = False
        model_false = model.copy()
        model_false[symbol] = False
        
        # Recursively check both possibilities
        return (self._check_all(query, symbols.copy(), model_true) and
                self._check_all(query, symbols.copy(), model_false))
    
    def _kb_true(self, model):
        """Check if all sentences in KB are true in given model"""
        return all(sentence.evaluate(model) for sentence in self.sentences)
    
    def __repr__(self):
        return f"KB with {len(self.sentences)} sentences"

"""
Propositional Logic Implementation
"""


class Sentence:
    """Base class for logical sentences"""
    
    def evaluate(self, model):
        """Evaluate the sentence given a model (dict of symbol: bool)"""
        raise NotImplementedError
    
    def formula(self):
        """Return string formula"""
        raise NotImplementedError
    
    def symbols(self):
        """Return set of symbols in sentence"""
        raise NotImplementedError


class Symbol(Sentence):
    """A propositional symbol"""
    
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, other):
        return isinstance(other, Symbol) and self.name == other.name
    
    def __hash__(self):
        return hash(("symbol", self.name))
    
    def __repr__(self):
        return self.name
    
    def evaluate(self, model):
        return model.get(self.name, False)
    
    def formula(self):
        return self.name
    
    def symbols(self):
        return {self.name}


class Not(Sentence):
    """Logical NOT"""
    
    def __init__(self, operand):
        self.operand = operand
    
    def __eq__(self, other):
        return isinstance(other, Not) and self.operand == other.operand
    
    def __hash__(self):
        return hash(("not", hash(self.operand)))
    
    def __repr__(self):
        return f"Not({self.operand})"
    
    def evaluate(self, model):
        return not self.operand.evaluate(model)
    
    def formula(self):
        return f"¬{self.operand.formula()}"
    
    def symbols(self):
        return self.operand.symbols()


class And(Sentence):
    """Logical AND"""
    
    def __init__(self, *conjuncts):
        self.conjuncts = list(conjuncts)
    
    def __eq__(self, other):
        return isinstance(other, And) and self.conjuncts == other.conjuncts
    
    def __hash__(self):
        return hash(("and", tuple(hash(c) for c in self.conjuncts)))
    
    def __repr__(self):
        return f"And({', '.join(str(c) for c in self.conjuncts)})"
    
    def evaluate(self, model):
        return all(conjunct.evaluate(model) for conjunct in self.conjuncts)
    
    def formula(self):
        if len(self.conjuncts) == 1:
            return self.conjuncts[0].formula()
        return "(" + " ∧ ".join(c.formula() for c in self.conjuncts) + ")"
    
    def symbols(self):
        return set().union(*[c.symbols() for c in self.conjuncts])


class Or(Sentence):
    """Logical OR"""
    
    def __init__(self, *disjuncts):
        self.disjuncts = list(disjuncts)
    
    def __eq__(self, other):
        return isinstance(other, Or) and self.disjuncts == other.disjuncts
    
    def __hash__(self):
        return hash(("or", tuple(hash(d) for d in self.disjuncts)))
    
    def __repr__(self):
        return f"Or({', '.join(str(d) for d in self.disjuncts)})"
    
    def evaluate(self, model):
        return any(disjunct.evaluate(model) for disjunct in self.disjuncts)
    
    def formula(self):
        if len(self.disjuncts) == 1:
            return self.disjuncts[0].formula()
        return "(" + " ∨ ".join(d.formula() for d in self.disjuncts) + ")"
    
    def symbols(self):
        return set().union(*[d.symbols() for d in self.disjuncts])


class Implication(Sentence):
    """Logical implication (if-then)"""
    
    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent
    
    def __eq__(self, other):
        return (isinstance(other, Implication) and 
                self.antecedent == other.antecedent and 
                self.consequent == other.consequent)
    
    def __hash__(self):
        return hash(("implies", hash(self.antecedent), hash(self.consequent)))
    
    def __repr__(self):
        return f"Implication({self.antecedent}, {self.consequent})"
    
    def evaluate(self, model):
        # P => Q is equivalent to (not P) or Q
        return not self.antecedent.evaluate(model) or self.consequent.evaluate(model)
    
    def formula(self):
        return f"{self.antecedent.formula()} ⇒ {self.consequent.formula()}"
    
    def symbols(self):
        return self.antecedent.symbols().union(self.consequent.symbols())


class Biconditional(Sentence):
    """Logical biconditional (if and only if)"""
    
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __eq__(self, other):
        return (isinstance(other, Biconditional) and 
                self.left == other.left and 
                self.right == other.right)
    
    def __hash__(self):
        return hash(("biconditional", hash(self.left), hash(self.right)))
    
    def __repr__(self):
        return f"Biconditional({self.left}, {self.right})"
    
    def evaluate(self, model):
        # P <=> Q is true when both have same truth value
        return self.left.evaluate(model) == self.right.evaluate(model)
    
    def formula(self):
        return f"{self.left.formula()} ⇔ {self.right.formula()}"
    
    def symbols(self):
        return self.left.symbols().union(self.right.symbols())

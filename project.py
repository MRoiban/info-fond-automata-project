from utils import *
from tests import *

from automata.fa.fa import FA
from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

from pysat.solvers import Minisat22, Minicard
from pysat.formula import CNF, CNFPlus, IDPool

# Q2
def gen_aut(alphabet: str, pos: list[str], neg: list[str], k: int) -> DFA:
    xpool = IDPool(start_from=1)
    tpool = IDPool(start_from=1)
    apool = IDPool(start_from=1)
    cfn = CNF()
    
    for i in range(1, k):
        clause = []
        for j in range(1, k):
            for sigma in pos:
                clause.append(xpool.id((i,j,sigma)))
                clause.append(apool.id(j))
        cfn.append(clause)
    
    for i in range(1, k):
        clause = []
        for j in range(1, k):
            for sigma in neg:
                clause.append(xpool.id((i,j,sigma)))
                clause.append(-apool.id(j))
        cfn.append(clause)
    
    for i in range(1, k):
        clause = []
        for j in range(1, k):
            for sigma in alphabet:
                clause.append(tpool.id((i,j,sigma)))
        cfn.append(clause)
    
    solver = Minisat22(use_timer=True)
    solver.append_formula(cfn.clauses, no_return=False)
    print(cfn.clauses)
    solver.solve()
    model = solver.get_model()
    
    for i in range(1, k):
        for j in range(1, k):
            for sigma in pos:
                if xpool.id((i,j,sigma)) in model:
                    print("i: ",i," | j: ",j," | sigma: ", sigma)
        cfn.append(clause)
    
    
    return None
    

# Q3
def gen_minaut(alphabet: str, pos: list[str], neg: list[str]) -> DFA:
    # À COMPLÉTER
    pass

# Q4
def gen_autc(alphabet: str, pos: list[str], neg: list[str], k: int) -> DFA:
    # À COMPLÉTER
    pass

# Q5
def gen_autr(alphabet: str, pos: list[str], neg: list[str], k: int) -> DFA:
    # À COMPLÉTER
    pass

# Q6
def gen_autcard(alphabet: str, pos: list[str], neg: list[str], k: int, ell: int) -> DFA:
    # À COMPLÉTER
    pass

# Q7
def gen_autn(alphabet: str, pos: list[str], neg: list[str], k: int) -> NFA:
    # À COMPLÉTER
    pass

# def main():
#     test_aut()
#     test_minaut()
#     test_autc()
#     test_autr()
#     test_autcard()
#     test_autn()

# if __name__ == '__main__':
#     main()

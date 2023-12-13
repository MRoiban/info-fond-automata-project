from utils import *
from tests import *

from automata.fa.fa import FA
from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

from pysat.solvers import Minisat22, Minicard
from pysat.formula import CNF, CNFPlus, IDPool

vpool = IDPool(start_from=1)
cfn = CNF()

A_ID = 1
X_ID = 2
T_ID = 3

# Q2
def gen_aut(alphabet: str, pos: list[str], neg: list[str], k: int) -> DFA:
    vpool = IDPool(start_from=1)
    cnf = CNF()
    for sigma in pos:
        for j in range(1, k):
            cnf.append([-vpool.id((X_ID,j,sigma)),vpool.id((A_ID,j))])
                
    
    for sigma in pos:
        for j in range(1, k):
            cnf.append([vpool.id((X_ID,j,sigma)),-vpool.id((A_ID,j))])
                
    
    for i in range(1, k):
        for j in range(1, k):
            for j_1 in range(1,k):
                if j != j_1:
                    for alpha in alphabet:
                        cnf.append([-vpool.id((T_ID,i,j,alpha)),-vpool.id((T_ID,i,j_1,alpha))])
       
    
    solver = Minisat22(use_timer=True)
    solver.append_formula(cfn.clauses, no_return=False)
    print(cnf.clauses)
    solver.solve()
    model = solver.get_model()
   
    for sigma in pos: 
        for j in range(k):
            if vpool.id((X_ID,j,sigma)) in model:
                print(j)
    
    
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

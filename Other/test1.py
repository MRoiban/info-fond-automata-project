from pysat.solvers import Glucose3

def encode_formula(k, P):
    # Create a SAT solver instance
    solver = Glucose3()

    # Define variables
    variables = [[[[solver.new_var() for _ in range(len(P))] for _ in range(k)] for _ in range(k)] for _ in range(2)]

    # Encode the formula
    for i in range(k):
        for j in range(k):
            clause = [variables[0][i][j][sigma] for sigma in range(len(P))]
            solver.add_clause(clause)

    for i in range(k):
        for sigma in P:
            clause = [variables[0][i][j][sigma] for j in range(k)] + [variables[1][i][sigma]]
            solver.add_clause(clause)

    # Ensure at least one variable is true for each i, j
    for i in range(k):
        for j in range(k):
            clause = [variables[0][i][j][sigma] for sigma in range(len(P))] + [variables[1][i][sigma] for sigma in P]
            solver.add_clause(clause)
    
    
    
    return solver

# Example usage with k=3 and P=[1, 2, 3]
k_value = 3
P_values = [1, 2, 3]
solver_instance = encode_formula(k_value, P_values)

# Solve the formula
if solver_instance.solve():
    print("Formula is satisfiable")
    model = solver_instance.get_model()
    print("Model:", model)
else:
    print("Formula is unsatisfiable")

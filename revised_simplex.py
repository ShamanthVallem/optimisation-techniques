# import numpy as np

# def revisedSimplexMethod(functionCoeffecientMatrix, inequalityMatrix, constantMatrix, minOrMax):
#     pass

import numpy as np

def revisedSimplexMethod(c, A, b, minOrMax):
    m, n = A.shape
    toBeReturned = []
    interation_list = []
    optimal_val_list = []
    basic_indices_list = []
    basic_feasible_solutions_list = []
    tableau = np.zeros((m + 1, n + m + 1))
    #   filling tableau with values of A
    for i in range(m):
        for j in range(n):
            tableau[i][j] = A[i][j]
#   filling tableau with values of b
    for i in range(m):
        tableau[i][-1] = b[i]
#   fill tableau with values of c
    if(minOrMax == "minimization"):
        for i in range(len(c)):
            tableau[-1][i] = c[i]
    else:
        for i in range(len(c)):
            tableau[-1][i] = (-1)*c[i]

    v, d = tableau.shape

    # Adding slack variables
    for i in range(m):
        for j in range(n, d-2):
            tableau[i][j+i] = 1
            break

    initial_tableau = tableau.copy()


    c_mat = c.copy()
    m, n = A.shape
    M = np.concatenate((A, np.eye(m)), axis=1)
    c = np.concatenate((c, np.zeros(m)))
    c = -1*c
    basis = np.arange(n, n + m)  # Initial basis indices
    non_basis = np.arange(n)  # Initial non-basis indices
    
    iteration = 0  # Counter for iterations
    
    while True:
        iteration += 1
        # print("Iteration:", iteration)
        interation_list.append(iteration)
        B = M[:, basis]
        N = M[:, non_basis]
        c_B = c[basis]
#         print(c_B)
        c_N = c[non_basis]
        B_inv = np.linalg.inv(B)
#         print(B_inv)
        x_B = B_inv @ b
        c_B_T = c_B.T @ B_inv
#         print(c_B_T)
        reduced_costs = c_N - c_B_T @ N
#         print(reduced_costs)
        
        
        opt_val = 0
        for i in range(len(basis)):
            if(basis[i] < len(c_mat)):
                opt_val = opt_val + (c_mat[basis[i]]*x_B[i])
#             print(x_B[i])
#             print(basis[i])
#             print(c_mat[i])
        print(f"optimal value of BFS:{opt_val}")

        optimal_val_list.append(opt_val)
        
        
        # print("Basis indices:", basis)
        
        basis_copy = basis.copy()
        basic_indices_list.append(basis_copy)
        # print("Basic feasible solution:", x_B)
        
        x_B_copy = x_B.copy()
        basic_feasible_solutions_list.append(x_B_copy)
        # print("-"*50)
        
        if np.all(reduced_costs >= 0):
            break  # Optimal solution reached

        entering_idx = np.argmin(reduced_costs)
        entering_var = non_basis[entering_idx]

        d_B = B_inv @ A[:, entering_var]
        if np.all(d_B <= 0):
            raise Exception("Unbounded solution")  # Unbounded problem

        ratios = np.divide(x_B, d_B, out=np.inf * np.ones(m), where=d_B > 0)
        leaving_idx = np.argmin(ratios)
        leaving_var = basis[leaving_idx]

        basis[leaving_idx] = entering_var
        non_basis[entering_idx] = leaving_var

    toBeReturned.append(initial_tableau)
    toBeReturned.append(interation_list)
    toBeReturned.append(optimal_val_list)
    toBeReturned.append(basic_indices_list)
    toBeReturned.append(basic_feasible_solutions_list)
    # return x_B, basis
    return toBeReturned


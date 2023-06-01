import numpy as np

def revisedSimplexMethod(functionCoeffecientMatrix, inequalityMatrix, constantMatrix, minOrMax):
    # pass
    m, n = inequalityMatrix.shape
    tobeReturned = []
    bfs_list = []
    pivotValues_list = []
    np.set_printoptions(suppress=True)
    tableau = np.zeros((m + 1, n + m + 1))

#   filling tableau with values of A
    for i in range(m):
        for j in range(n):
            tableau[i][j] = inequalityMatrix[i][j]
#   filling tableau with values of b
    for i in range(m):
        tableau[i][-1] = constantMatrix[i]
#   fill tableau with values of c
    if(minOrMax == "minimization"):
        for i in range(len(functionCoeffecientMatrix)):
            tableau[-1][i] = functionCoeffecientMatrix[i]
    else:
        for i in range(len(functionCoeffecientMatrix)):
            tableau[-1][i] = (-1)*functionCoeffecientMatrix[i]

#     print(tableau)
    v, d = tableau.shape

    # Adding slack variables
    for i in range(m):
        for j in range(n, d-2):
            tableau[i][j+i] = 1
            break
    initial_tableau = tableau.copy()
    tobeReturned.append(initial_tableau)
            
    # print(tableau)b
#     i = 0
    while np.any(tableau[-1, :-1] < 0):
        pivot_column = np.argmin(tableau[-1, :-1])
        ratios = tableau[:-1, -1] / tableau[:-1, pivot_column]
        pivot_row = np.argmin(ratios[ratios >= 0])
        pivot_value = tableau[pivot_row, pivot_column]

        pivotValues_list.append([pivot_value, pivot_row, pivot_column])
        bfs_list.append(tableau.copy())
#         Pivot operation
        tableau[pivot_row, :] /= pivot_value
        for i in range(m + 1):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_column] * tableau[pivot_row, :]
    # final_bfs.append(tableau)
    final_bfs = tableau.copy()
    tobeReturned.append(bfs_list)
    tobeReturned.append(pivotValues_list)
    tobeReturned.append(final_bfs)
    return tobeReturned
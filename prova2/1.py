import numpy as np
import pandas as pd

def gauss_elimination_partial_pivot(A, b):
    n = len(b)
    A = A.astype(float)
    b = b.astype(float)
    iter_table = []

    # Iteração 0 - Matriz inicial aumentada
    augmented_matrix = np.hstack((A, b.reshape(-1, 1)))
    iter_table.append(pd.DataFrame(augmented_matrix, columns=[f'x{i+1}' for i in range(n)] + ['b']).round(10))

    for k in range(n - 1):
        max_row = np.argmax(np.abs(A[k:, k])) + k
        if A[max_row, k] == 0:
            raise ValueError("A matriz é singular e não possui solução.")
        
        if max_row != k:
            A[[k, max_row]] = A[[max_row, k]]
            b[[k, max_row]] = b[[max_row, k]]
        
        for i in range(k + 1, n):
            m = A[i, k] / A[k, k]
            A[i, k:] -= m * A[k, k:]
            b[i] -= m * b[k]
        
        augmented_matrix = np.hstack((A, b.reshape(-1, 1)))
        iter_table.append(pd.DataFrame(augmented_matrix, columns=[f'x{i+1}' for i in range(n)] + ['b']).round(10))
    
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
    
    return x, iter_table

def gauss_elimination_total_pivot(A, b):
    n = len(b)
    A = A.astype(float)
    b = b.astype(float)
    iter_table = []
    index_order = np.arange(n)

    # Iteração 0 - Matriz inicial aumentada
    augmented_matrix = np.hstack((A, b.reshape(-1, 1)))
    iter_table.append(pd.DataFrame(augmented_matrix, columns=[f'x{i+1}' for i in range(n)] + ['b']).round(10))

    for k in range(n - 1):
        sub_matrix = np.abs(A[k:, k:])
        max_row, max_col = np.unravel_index(np.argmax(sub_matrix), sub_matrix.shape)
        max_row += k
        max_col += k

        if A[max_row, max_col] == 0:
            raise ValueError("A matriz é singular e não possui solução.")

        if max_row != k:
            A[[k, max_row]] = A[[max_row, k]]
            b[[k, max_row]] = b[[max_row, k]]
        
        if max_col != k:
            A[:, [k, max_col]] = A[:, [max_col, k]]
            index_order[[k, max_col]] = index_order[[max_col, k]]

        for i in range(k + 1, n):
            m = A[i, k] / A[k, k]
            A[i, k:] -= m * A[k, k:]
            b[i] -= m * b[k]
        
        augmented_matrix = np.hstack((A, b.reshape(-1, 1)))
        iter_table.append(pd.DataFrame(augmented_matrix, columns=[f'x{i+1}' for i in range(n)] + ['b']).round(10))

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
    
    x_final = np.zeros(n)
    for i, ix in enumerate(index_order):
        x_final[ix] = x[i]
    
    return x_final, iter_table

# Dados da matriz A e vetor b
A = np.array([
    [20.00000000, -28.00000000, 30.00000000, 88.00000000, 47.00000000, -2.00000000, 87.00000000],
    [21.00000000, 46.00000000, 51.00000000, 52.00000000, -15.00000000, 42.00000000, 68.00000000],
    [27.00000000, -37.00000000, -93.00000000, -40.00000000, -43.00000000, -13.00000000, -75.00000000],
    [49.00000000, 14.00000000, -62.00000000, 36.00000000, -28.00000000, -16.00000000, 1.00000000],
    [78.00000000, 32.00000000, -50.00000000, -51.00000000, -34.00000000, -19.00000000, -5.00000000],
    [70.00000000, -47.00000000, 31.00000000, -82.00000000, 7.00000000, 60.00000000, 33.00000000],
    [-31.00000000, -62.00000000, 6.00000000, -30.00000000, -79.00000000, -12.00000000, 11.00000000]
])
b = np.array([96.00000000, 81.00000000, 17.00000000, -9.00000000, 75.00000000, -96.00000000, 33.00000000])

# Executa os métodos
x_partial, iter_table_partial = gauss_elimination_partial_pivot(A.copy(), b.copy())
x_total, iter_table_total = gauss_elimination_total_pivot(A.copy(), b.copy())

# Resultados do Pivotamento Parcial
for idx, table in enumerate(iter_table_partial):
    print(f"\nA{idx} - Pivotamento Parcial:")
    print(table.to_string(index=False, float_format="   {:.10e}".format))

#print("\nSolução com Pivotamento Parcial:\n", end="")
#print("    ".join([f"x{i + 1} = {val:.10e}" for i, val in enumerate(x_partial)]))

solucao_ordenada_partial = [f"x{i + 1} = {x_partial[i]:.10e}" for i in range(len(x_partial)-1, -1, -1)]
print("\nSolução com Pivotamento Parcial:\n", "    ".join(solucao_ordenada_partial))

print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Resultados do Pivotamento Total
for idx, table in enumerate(iter_table_total):
    print(f"\nA{idx} - Pivotamento Total:")
    print(table.to_string(index=False, float_format="   {:.10e}".format))

#print("\nSolução com Pivotamento Total:\n", end="")
#print("    ".join([f"x{i + 1} = {val:.10e}" for i, val in enumerate(x_total)]))

solucao_ordenada_total = [f"x{i + 1} = {x_total[i]:.10e}" for i in range(len(x_total)-1, -1, -1)]
print("\nSolução com Pivotamento Total:\n", "    ".join(solucao_ordenada_total))
print("\n")

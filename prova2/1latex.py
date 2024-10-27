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

def matriz_to_latex(matrix):
    latex = "\\begin{bmatrix}\n"
    for row in matrix:
        latex += " & ".join(f"{val:.10e}" for val in row) + " \\\\\n"
    latex += "\\end{bmatrix}"
    return latex

def salvar_iteracoes_em_latex(iteracoes, filename, metodo):
    with open(filename, "w") as f:
        f.write(r"\documentclass{article}\usepackage{amsmath}\begin{document}\n")
        f.write(f"\\section*{{Eliminação de Gauss com {metodo}}}\n")
        
        for idx, tabela in enumerate(iteracoes):
            f.write(f"\\subsection*{{Iteração {idx}}}\n")
            f.write(f"{matriz_to_latex(tabela.values)}\n\n")
        
        f.write("\\end{document}")

# Configurar e executar
A = np.array([
    [20, -28, 30, 88, 47, -2, 87],
    [21, 46, 51, 52, -15, 42, 68],
    [27, -37, -93, -40, -43, -13, -75],
    [49, 14, -62, 36, -28, -16, 1],
    [78, 32, -50, -51, -34, -19, -5],
    [70, -47, 31, -82, 7, 60, 33],
    [-31, -62, 6, -30, -79, -12, 11]
])
b = np.array([96, 81, 17, -9, 75, -96, 33])

# Executar os métodos
x_partial, iter_table_partial = gauss_elimination_partial_pivot(A.copy(), b.copy())
x_total, iter_table_total = gauss_elimination_total_pivot(A.copy(), b.copy())

# Salvar tabelas e soluções em LaTeX
salvar_iteracoes_em_latex(iter_table_partial, "gauss_partial_pivot.tex", "Pivotamento Parcial")
salvar_iteracoes_em_latex(iter_table_total, "gauss_total_pivot.tex", "Pivotamento Total")

# Exibir a solução em LaTeX
def salvar_solucoes_em_latex(solucao, filename, metodo):
    with open(filename, "a") as f:
        f.write("\\subsection*{Solução}\n")
        for i, val in enumerate(solucao):
            f.write(f"x_{{{i+1}}} = {val:.10e}\\\\\n")
        f.write("\\end{document}")

salvar_solucoes_em_latex(x_partial, "gauss_partial_pivot.tex", "Pivotamento Parcial")
salvar_solucoes_em_latex(x_total, "gauss_total_pivot.tex", "Pivotamento Total")

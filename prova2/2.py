import numpy as np

# Matriz C e vetor d definidos
#C = np.array([
#    [-822, -84, -17, 26, 8, 64, 213],
#    [-51, 542, 94, 11, 7, -236, 31],
#    [-15, 180, 436, 5, 34, 63, -108],
#    [-6, 64, 10, -494, -225, -22, 108],
#    [-11, -42, 33, 179, -479, -144, -9],
#    [197, -52, -134, -2, 29, -637, 19],
#    [-10, -17, 263, 131, -61, 40, 939]
#], dtype=float)

#d = np.array([2, 96, -4, -39, -27, 45, 15], dtype=float)

# Nova matriz C e vetor d fornecidos
C = np.array([
    [583, 25, 2, -80, -148, -17, 282],
    [-17, -718, 2, -39, 93, -44, 174],
    [-17, 55, -795, 204, -35, 89, 10],
    [-32, 44, 9, -633, -280, -149, 15],
    [18, -276, -67, 4, 934, -152, -22],
    [-38, 14, -144, 0, 56, -847, 267],
    [-39, -5, -78, -276, 136, 13, 593]
], dtype=float)

d = np.array([73, -10, -9, 34, -73, -67, 10], dtype=float)

# Configurações de precisão
precision = 1e-5
max_iter = 100

# Função para calcular o método de Jacobi
def jacobi_method(C, d):
    n = len(d)
    x = np.zeros(n)
    x_new = np.zeros(n)
    results = [x.copy()]  # Adicionando iteração 0 com valores iniciais
    errors = [np.full(n, None)]  # Erros na iteração 0 são nulos

    for k in range(1, max_iter):
        for i in range(n):
            sigma = sum(C[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (d[i] - sigma) / C[i][i]

        # Armazenar resultados e erros relativos
        results.append(x_new.copy())
        err = np.abs((x_new - x) / (x_new + 1e-10))  # Adicionado valor pequeno para evitar divisão por zero
        errors.append(err)

        # Parada se todos erros estiverem dentro da precisão
        if all(e < precision for e in err):
            break

        x = x_new.copy()

    return results, errors

# Função para calcular o método de Gauss-Seidel
def gauss_seidel_method(C, d):
    n = len(d)
    x = np.zeros(n)
    results = [x.copy()]  # Adicionando iteração 0 com valores iniciais
    errors = [np.full(n, None)]  # Erros na iteração 0 são nulos

    for k in range(1, max_iter):
        x_old = x.copy()
        
        for i in range(n):
            sigma = sum(C[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (d[i] - sigma) / C[i][i]

        # Armazenar resultados e erros relativos
        results.append(x.copy())
        err = np.abs((x - x_old) / (x + 1e-10))  # Adicionado valor pequeno para evitar divisão por zero
        errors.append(err)

        # Parada se todos erros estiverem dentro da precisão
        if all(e < precision for e in err):
            break

    return results, errors

# Executa os métodos e armazena os resultados
jacobi_results, jacobi_errors = jacobi_method(C, d)
gauss_seidel_results, gauss_seidel_errors = gauss_seidel_method(C, d)

# Exibir resultados formatados em tabelas para cada método
def format_results(results, errors, method_name):
    print(f"{method_name}\n{'  k                 ':>3} " + "                  ".join([f"x{i+1},k" for i in range(len(results[0]))]))
    for k, res in enumerate(results):
        print(f"{k:>3}     " + " ".join([f"{x: .10e}    " for x in res]))
    print("\n--------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(f"\n{'  k                ':>3} " + "                 ".join([f"ER{i+1},k" for i in range(len(errors[0]))]))
    
    for k, err in enumerate(errors):
        if k == 0:
            print(f"{k:>3}     " + " ".join(["                -    " for _ in err]))
        else:
            print(f"{k:>3}     " + " ".join([f"{e: .10e}    " for e in err]))

    print("\n--------------------------------------------------------------------------------------------------------------------------------------------------------------")


# Exibindo tabelas
format_results(jacobi_results, jacobi_errors, "MÉTODO DE JACOBI")
print("\n")
format_results(gauss_seidel_results, gauss_seidel_errors, "MÉTODO DE GAUSS-SEIDEL")

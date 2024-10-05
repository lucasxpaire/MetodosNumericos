def f(x):
    return 3880.73 + 4044.8 * x + 1614.77 * x**2 + 308.576 * x**3 + 28.3001 * x**4 + x**5

def metodo_secante(x0, x1, tol, max_iter):
    print("MÉTODO DA SECANTE É DETERMINAÇÃO DA RAÍZ z3")
    print(f"{'k':<4} {'xk':<15} {'f(x_k)':<22} {'ER_k':<15}")

    k = 0
    erro_relativo = float('inf')  # Inicializa o erro relativo com um valor alto

    while erro_relativo > tol and k < max_iter:
        f_x0 = f(x0)
        f_x1 = f(x1)

        if f_x1 - f_x0 == 0:
            print("Divisão por zero detectada, abortando...")
            break

        # Fórmula da secante
        xk = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        # Cálculo do erro relativo
        if k > 0:
            erro_relativo = abs((xk - x1) / xk)

        # Impressão da linha com os valores de xk, f(xk) e erro relativo
        if k == 0:
            print(f"{k:<4} {x0:<15.10e} {f_x0:<22.10e} {'-':<15}")
            print(f"{k + 1:<4} {x1:<15.10e} {f_x1:<22.10e} {'-':<15}")
        else:
            print(f"{k + 1:<4} {xk:<15.10e} {f(xk):<22.10e} {erro_relativo:<15.10e}")

        # Atualiza os valores de x0 e x1 para a próxima iteração
        x0 = x1
        x1 = xk
        k += 1

    # Exibe a raiz encontrada
    print(f"\nRaíz z3 = {xk:.10e}")

# Parâmetros de entrada
x0 = -5.5  # Chute inicial
x1 = -5.0  # Segundo chute
tolerancia = 1e-6  # Tolerância para erro relativo
max_iteracoes = 100  # Número máximo de iterações

# Chama o método da secante
metodo_secante(x0, x1, tolerancia, max_iteracoes)

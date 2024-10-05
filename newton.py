def f(x):
    # Função fornecida
    return 3880.73 + 4044.8 * x + 1614.77 * x**2 + 308.576 * x**3 + 28.3001 * x**4 + x**5

def df(x):
    # Derivada da função
    return 4044.8 + 2 * 1614.77 * x + 3 * 308.576 * x**2 + 4 * 28.3001 * x**3 + 5 * x**4

def metodo_newton(x0, tol, max_iter):
    print("MÉTODO DE NEWTON É DETERMINAÇÃO DA RAÍZ z1")
    
    # Títulos das colunas com espaçamento ajustado
    print(f"{'k':<4} {'xk':<20} {'f(x_k)':<20} {'f\'(x_k)':<20} {'ER_k':<20}")
    
    k = 0
    erro_relativo = float('inf')  # Inicializa com um valor grande para começar o loop

    while erro_relativo > tol and k < max_iter:
        f_x0 = f(x0)
        f_prime_x0 = df(x0)

        # Cálculo do erro relativo
        if k > 0:
            erro_relativo = abs((xk - x_prev) / xk)
        else:
            erro_relativo = float('inf')  # Primeira iteração não calcula erro

        # Atualiza xk usando o método de Newton
        xk = x0 - f_x0 / f_prime_x0

        # Impressão da linha com espaçamento fixo
        if k > 0:
            print(f"{k:<4} {xk:<20.10e} {f(xk):<20.10e} {f_prime_x0:<20.10e} {erro_relativo:<20.10e}")
        else:
            print(f"{k:<4} {x0:<20.10e} {f_x0:<20.10e} {f_prime_x0:<20.10e} {'-':<15}")

        # Atualiza x0 para a próxima iteração
        x_prev = x0  # Armazena o valor anterior de x0
        x0 = xk  # Atualiza x0
        k += 1  # Incrementa o contador de iterações

    # Exibe a raiz encontrada
    print(f"\nRaíz z1 = {xk:.10e}")

# Parâmetros de entrada
x0 = -7.5  # Aproximação inicial
tolerancia = 1e-6  # Tolerância para erro relativo
max_iteracoes = 100  # Número máximo de iterações

# Chama a função do método de Newton
metodo_newton(x0, tolerancia, max_iteracoes)

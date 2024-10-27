def f(x):
    # Função fornecida
    #x^5 + 35.3346x^4 + 495.069x^3 + 3436.98x^2 + 11819.8x + 16104.6
    return 16104.6 + 11819.8 * x + 3436.98 * x**2 + 495.069 * x**3 + 35.3346 * x**4 + x**5

def metodo_bisseccao(a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        print("A função deve ter sinais opostos nos extremos.")
        return None

    print("MÉTODO DA BISSECÇÃO É DETERMINAÇÃO DA RAÍZ z1")
    
    # Títulos das colunas com espaçamento ajustado
    print(f"{'k':<4} {'ak':<20} {'xk':<20} {'bk':<20} {'f(ak)':<20} {'f(xk)':<20} {'f(bk)':<20} {'ERk':<20}")

    x_prev = None  # Inicializa x_prev como None para a primeira iteração
    k = 0
    erro_relativo = float('inf')  # Inicializa com um valor grande para começar o loop

    while erro_relativo > tol and k < max_iter:
        xk = (a + b) / 2
        f_a = f(a)
        f_x = f(xk)
        f_b = f(b)

        # Cálculo do erro relativo
        if x_prev is not None:
            erro_relativo = abs((xk - x_prev) / xk)
        else:
            erro_relativo = float('inf')  # Primeira iteração não calcula erro

        # Impressão da linha com espaçamento fixo
        if k == 0:
            print(f"{k:<4} {a:<20.10e} {xk:<20.10e} {b:<20.10e} {f_a:<20.10e} {f_x:<20.10e} {f_b:<20.10e} {'-':<20}")
        else:
            print(f"{k:<4} {a:<20.10e} {xk:<20.10e} {b:<20.10e} {f_a:<20.10e} {f_x:<20.10e} {f_b:<20.10e} {erro_relativo:<20.10e}")

        # Atualiza os limites com base no sinal de f(a) * f(xk)
        if f_a * f_x < 0:
            b = xk
        else:
            a = xk

        x_prev = xk  # Armazena o valor anterior de xk
        k += 1  # Incrementa o contador de iterações

    # Exibe a raiz encontrada
    print(f"\nRaíz z1 = {xk:.10e}")

# Parâmetros de entrada
a = -9.0  # Limite inferior
b = -5.0  # Limite superior
tolerancia = 1e-6  # Tolerância para erro relativo
max_iteracoes = 100  # Número máximo de iterações

# Chama a função do método da bissecção
metodo_bisseccao(a, b, tolerancia, max_iteracoes)

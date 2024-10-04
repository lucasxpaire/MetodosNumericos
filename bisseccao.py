def f(x):
    # Função fornecida
    return 3880.73 + 4044.8 * x + 1614.77 * x**2 + 308.576 * x**3 + 28.3001 * x**4 + x**5

def metodo_bisseccao(a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        print("A função deve ter sinais opostos nos extremos.")
        return None

    print("MÉTODO DA BISSECÇÃO É DETERMINAÇÃO DA RAÍZ z1")
    print("k\t ak\t\t xk\t\t bk\t\t f(a_k)\t\t f(x_k)\t\t f(b_k)\t\t ER_k")

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

        # Impressão da linha
        if k == 0:
            print(f"{k}\t {a:.10f}\t {xk:.10f}\t {b:.10f}\t {f_a:.10f}\t {f_x:.10f}\t {f_b:.10f}\t {'-'}")
        else:
            print(f"{k}\t {a:.10f}\t {xk:.10f}\t {b:.10f}\t {f_a:.10f}\t {f_x:.10f}\t {f_b:.10f}\t {erro_relativo:.10f}")

        # Atualiza os limites com base no sinal de f(a) * f(xk)
        if f_a * f_x < 0:
            b = xk
        else:
            a = xk

        x_prev = xk  # Armazena o valor anterior de xk
        k += 1  # Incrementa o contador de iterações

    # Exibe a raiz encontrada
    print(f"Raíz z1 = {xk:.9f}")

# Parâmetros de entrada
a = -9.0  # Limite inferior
b = -8.0  # Limite superior
tolerancia = 1e-6  # Tolerância para erro relativo
max_iteracoes = 100  # Número máximo de iterações

# Chama a função do método da bissecção
metodo_bisseccao(a, b, tolerancia, max_iteracoes)

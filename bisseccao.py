def f(x):
    # Função ajustada conforme sua descrição
    return 3880.73 + 4044.8 * x + 1614.77 * x**2 + 308.576 * x**3 + 28.3001 * x**4 + x**5
    #minha função
    #return = x5 + 35.3346x4 + 495.069x3 + 3436.98x2 + 11819.8x + 16104.6
    #return 16104.6 + 11819.8*x + 3436.98*x**2 + 495.069*x**3 + 35.3346*x**4 + x**5

def metodo_bisseccao(a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        print("A função deve ter sinais opostos nos extremos.")
        return None

    print("MÉTODO DA BISSECÇÃO É DETERMINAÇÃO DA RAÍZ z1")
    print("k\t ak\t\t xk\t\t bk\t\t f(a_k)\t\t f(x_k)\t\t f(b_k)\t\t ER_k")

    for k in range(max_iter):
        xk = (a + b) / 2
        f_a = f(a)
        f_x = f(xk)
        f_b = f(b)

        # Cálculo do erro relativo
        if k > 0:
            ER_k = abs((xk - x_prev) / xk)
        else:
            ER_k = '-'

        # Impressão da linha
        print(f"{k}\t {a:.10f}\t {xk:.10f}\t {b:.10f}\t {f_a:.10f}\t {f_x:.10f}\t {f_b:.10f}\t {ER_k}")

        # Atualiza os limites
        if f_a * f_x < 0:
            b = xk
        else:
            a = xk

        x_prev = xk  # Armazena o valor anterior de xk

        # Verifica a convergência
        if abs(f_x) < tol:
            break

    print(f"Raíz z1 = {xk:.10f}")

# Parâmetros de entrada
a = -9.0  # Limite inferior
b = -8.0  # Limite superior
tolerancia = 1e-6  # Tolerância
max_iteracoes = 17  # Número máximo de iterações

# Chama a função do método da bissecção
metodo_bisseccao(a, b, tolerancia, max_iteracoes)

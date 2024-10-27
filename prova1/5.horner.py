def horner(coeficientes, x):
    n = len(coeficientes) - 1  # Grau do polinômio
    p = coeficientes[0]  # Primeiro coeficiente (a_N)
    p_linha = 0  # Derivada começa com zero

    coeficientes_P = [p]  # Coeficientes do polinômio
    coeficientes_P_linha = []  # Coeficientes da derivada

    # Aplicando o método de Horner para P(x) e P'(x)
    for i in range(1, n+1):
        p_linha = p_linha * x + p  # Derivada de Horner
        p = p * x + coeficientes[i]  # Polinômio de Horner
        coeficientes_P_linha.append(p_linha)  
        coeficientes_P.append(p)  # Coeficiente do polinômio

    return p, p_linha, coeficientes_P, coeficientes_P_linha

def pedir_numero_float(mensagem):
    return float(input(mensagem))

def f(x):
    # Exemplo de polinômio P(x) = x^5 - 20.0253x^4 + 156.407x^3 - 595.207x^2 + 1103.49x - 797.472
    return 16104.6 + 11819.8 * x + 3436.98 * x**2 + 495.069 * x**3 + 35.3346 * x**4 + x**5

def f_linha(x):
    # Derivada do polinômio P'(x) = 5x^4 - 80.1012x^3 + 469.221x^2 - 1190.414x + 1103.49
    return 11819.8 + 2*3436.98*x + 3*495.069 * x**2 + 4*35.3346 * x**3 + 5*x**4

def tolerancia(x_novo, x_anterior):
    return abs((x_novo - x_anterior) / x_novo)

def e():
    return 1e-6  # Tolerância para o erro relativo

def metodo_de_horner():
    # Coeficientes do polinômio P(x) = x^5 - 20.0253x^4 + 156.407x^3 - 595.207x^2 + 1103.49x - 797.472
    coeficientes = [1, 35.3346, 495.069, 3436.98, 11819.8, 16104.6]
    
    x_anterior = pedir_numero_float("Chute inicial: ")

    coeficientes_P = []
    coeficientes_P_linha = []
    estimativas = []  # Lista para armazenar as interações
    estimativas.append((x_anterior, f(x_anterior), f_linha(x_anterior), "-"))

    while True:
        p_xn, pn_linha_xn, coeficientes_P_atual, coeficientes_P_linha_atual = horner(coeficientes, x_anterior)

        # Adiciona os coeficientes da iteração atual às listas
        if pn_linha_xn == 0:
            print("Derivada igual a zero, método não pode continuar.")
            return None, []

        x = x_anterior - p_xn / pn_linha_xn
        erro = tolerancia(x, x_anterior)  # Calcula a tolerância

        coeficientes_P.append(coeficientes_P_atual)
        coeficientes_P_linha.append(coeficientes_P_linha_atual)
        estimativas.append((x, f(x), f_linha(x), erro))
        
        # Verifica se o erro está dentro da tolerância
        if erro < e():
            return x, estimativas, coeficientes_P, coeficientes_P_linha

        # Limite de 100 iterações para evitar loops infinitos
        if len(estimativas) > 100:
            print("Método de Horner não convergiu.")
            return None, []

        x_anterior = x

# Função para imprimir os resultados formatados em notação científica
def imprimir_resultados(estimativas, coeficientes_P, coeficientes_P_linha):
    print("\nCoeficientes bi do Polinômio f(x)")
    # Alteração: invertendo apenas os nomes das colunas b(i,k), mas mantendo a impressão inalterada
    print("k   ", "  ".join([f"b{i}k".ljust(20) for i in range(len(coeficientes_P[0]) - 1, -1, -1)]))

    for k, b_vals in enumerate(coeficientes_P):
        # Notação científica para coeficientes de f(x)
        print(f"{k:<4}", "  ".join([f"{b_vals[i]:<20.10e}" for i in range(len(b_vals))]))

    print("\nCoeficientes ci do Polinômio f'(x)")
    # Alteração: invertendo apenas os nomes das colunas c(i,k), mas mantendo a impressão inalterada
    print("k   ", "  ".join([f"c{i+1}k".ljust(20) for i in range(len(coeficientes_P_linha[0]) - 1, -1, -1)]))

    for k, c_vals in enumerate(coeficientes_P_linha):
        # Notação científica para coeficientes de f'(x)
        print(f"{k:<4}", "  ".join([f"{c_vals[i - 1]:<20.10e}" for i in range(1, len(c_vals) + 1)]))

    print("\nEstimativas")
    # Alteração para notação científica nas estimativas
    print(f"{'k':<5}{'xk':<20}{'f(xk)':<20}{'f\'(xk)':<20}{'ERk':<20}")
    for k, (x, fx, fpx, erro) in enumerate(estimativas):
        # Checando se 'erro' é uma string ou um número
        if isinstance(erro, str):
            print(f"{k:<5}{x:<20.10e}{fx:<20.10e}{fpx:<20.10e}{erro:<20}")
        else:
            print(f"{k:<5}{x:<20.10e}{fx:<20.10e}{fpx:<20.10e}{erro:<20.10e}")

# Chamando o método de Horner
raiz, estimativas, coeficientes_P, coeficientes_P_linha = metodo_de_horner()

if raiz is not None:
    imprimir_resultados(estimativas, coeficientes_P, coeficientes_P_linha)
    print(f"\nRaiz z5 = {raiz:.10e}")

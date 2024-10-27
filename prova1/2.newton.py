def f_string():
    return "x**5 - 12.0953*x**4 + 33.6161*x**3 + 55.4476*x**2 - 260.915*x + 119.827"

def f(x):
    return 16104.6 + 11819.8 * x + 3436.98 * x**2 + 495.069 * x**3 + 35.3346 * x**4 + x**5

def f_linha(x):
    return 11819.8 + 2*3436.98*x + 3*495.069 * x**2 + 4*35.3346 * x**3 + 5*x**4

def e():
    return 0.000001  # Define a tolerância

def tolerancia(x, x_anterior):
    return abs((x - x_anterior) / x)

def pedir_numero_float(mensagem):
    while True:
        try:
            x = float(input(mensagem))
            return x
        except ValueError:
            print("Entrada inválida, tente novamente!")

def metodo_de_newton():
    x_anterior = pedir_numero_float("Chute inicial: ")

    interacoes = []  # Lista para armazenar as interações
    interacoes.append((x_anterior, f(x_anterior), f_linha(x_anterior), "-"))

    while True:
        if f_linha(x_anterior) == 0:
            print("Derivada igual a zero, método não pode continuar.")
            return None, []

        x = x_anterior - f(x_anterior) / f_linha(x_anterior)
        erro = tolerancia(x, x_anterior)  # Calcula a tolerância
        interacoes.append((x, f(x), f_linha(x), erro))

        if erro < e():
            return x, interacoes

        if len(interacoes) > 100:
            print("Método de Newton não convergiu.")
            return None, []

        x_anterior = x

# Chamar o método de Newton
raiz, interacoes = metodo_de_newton()

# Verifica se a raiz foi encontrada e exibe as interações
if raiz is not None:
    print("\nMÉTODO DE NEWTON | DETERMINAÇÃO DA RAIZ z2")
    # Cabeçalho da tabela
    print(f"{'k':<4} {'xk':<20} {'f(xk)':<20} {'f\'(xk)':<20} {'ERk':<20}")

    # Exibir as iterações
    for i, (x, fx, f_linha, er) in enumerate(interacoes):
        if isinstance(er, str):
            print(f"{i:<4} {x:<20.10e} {fx:<20.10e} {f_linha:<20.10e} {er:<20}")
        else:
            print(f"{i:<4} {x:<20.10e} {fx:<20.10e} {f_linha:<20.10e} {er:<20.10e}")

    # Exibe o valor final da raiz
    print(f"\nRaiz z2 = {raiz:.9e}")
else:
    print("Método de Newton não encontrou uma raiz.")

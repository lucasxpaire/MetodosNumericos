def f_string():
    return "x**5 - 12.0953*x**4 + 33.6161*x**3 + 55.4476*x**2 - 260.915*x + 119.827"

def f(x):
    return 16104.6 + 11819.8 * x + 3436.98 * x**2 + 495.069 * x**3 + 35.3346 * x**4 + x**5

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

def metodo_falsa_posicao():
    a = pedir_numero_float("Digite a1: ")
    b = pedir_numero_float("Digite b1: ")
    print()

    if f(a) * f(b) > 0:
        print("Não existe raiz nesse intervalo ou o intervalo possui mais de uma raiz. Tente outro.")
        return None, []

    x_anterior = None
    interacoes = []  # Lista para armazenar as interações

    for _ in range(100):
        x = a - (b - a) / (f(b) - f(a)) * f(a)
        interacoes.append((a, x, b, f(x), tolerancia(x, x_anterior) if x_anterior is not None else "-"))

        if x_anterior is not None and tolerancia(x, x_anterior) <= e():
            return x, interacoes

        if f(a) * f(x) < 0:
            b = x
        else:
            a = x

        x_anterior = x

    print("O método não convergiu dentro do número máximo de iterações.")
    return None, []

# Chamar o método da Falsa Posição
raiz, interacoes = metodo_falsa_posicao()

# Verifica se a raiz foi encontrada e exibe as interações
if raiz is not None:
    print("\nMÉTODO DA FALSA POSIÇÃO | DETERMINAÇÃO DA RAIZ z4")
    # Cabeçalho da tabela
    print(f"{'k':<4} {'ak':<20} {'xk':<20} {'bk':<20} {'f(xk)':<20} {'ERk':<20}")

    # Exibir as iterações
    for i, (a, x, b, fx, er) in enumerate(interacoes):
        if isinstance(er, str):
            print(f"{i:<4} {a:<20.9e} {x:<20.9e} {b:<20.9e} {fx:<20.9e} {er:<20}")
        else:
            print(f"{i:<4} {a:<20.9e} {x:<20.9e} {b:<20.9e} {fx:<20.9e} {er:<20.9e}")

    # Exibe o valor final da raiz
    print(f"\nRaiz z4 = {raiz:.9e}")
else:
    print("Método da Falsa Posição não encontrou uma raiz.")

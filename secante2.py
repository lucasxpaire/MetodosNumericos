import math

# Definir a função f(x) fornecida
def f(x):
    return 3880.73 + 4044.8 * x + 1614.77 * x**2 + 308.576 * x**3 + 28.3001 * x**4 + x**5

# Método da secante
def secante(x0, x1, tol=1e-6, max_iter=100):
    print(f"{'k':^5}{'x_k':^25}{'f(x_k)':^25}{'ER_k':^25}")
    
    k = 0
    f_x0 = f(x0)
    print(f"{k:^5}{x0:^25.10e}{f_x0:^25.10e}{'-':^25}")
    
    k += 1
    f_x1 = f(x1)
    er = abs((x1 - x0) / x1)  # Corrigido cálculo do erro relativo
    print(f"{k:^5}{x1:^25.10e}{f_x1:^25.10e}{er:^25.10e}")
    
    while er > tol and k < max_iter:
        try:
            # Aplicando a fórmula da secante
            x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        except ZeroDivisionError:
            print("Divisão por zero encontrada durante a execução do método da secante.")
            break
        
        # Atualizar valores para próxima iteração
        x0, x1 = x1, x2
        f_x0, f_x1 = f_x1, f(x2)
        er = abs((x1 - x0) / x1)  # Cálculo do erro relativo ajustado
        
        k += 1
        print(f"{k:^5}{x1:^25.10e}{f_x1:^25.10e}{er:^25.10e}")

    return x1

# Chamar a função com os valores iniciais fornecidos
x0 = -5.5
x1 = -5.0
raiz = secante(x0, x1)

print(f"\nRaiz z3 = {raiz:.10e}")

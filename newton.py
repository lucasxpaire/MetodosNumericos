# Função fornecida
def f(x):
    return 3880.73 + 4044.8*x + 1614.77*x**2 + 308.576*x**3 + 28.3001*x**4 + x**5

# Derivada da função fornecida
def df(x):
    return 4044.8 + 2*1614.77*x + 3*308.576*x**2 + 4*28.3001*x**3 + 5*x**4

# Implementação do método de Newton
def newton(x0, tol=1e-6, max_iter=5):
    iteracoes = []
    for k in range(max_iter):
        fxk = f(x0)
        dfxk = df(x0)
        
        # Verifica se a derivada é zero para evitar divisão por zero
        if dfxk == 0:
            print("Derivada é zero, método não pode continuar.")
            break

        # Calcula a nova aproximação
        xk_new = x0 - fxk / dfxk
        
        # Erro relativo entre a nova aproximação e a anterior
        erro_relativo = abs((xk_new - x0) / xk_new)
        
        # Salva os resultados da iteração
        iteracoes.append([k, x0, fxk, dfxk, erro_relativo])
        
        # Critério de parada
        if erro_relativo < tol:
            break
        
        # Atualiza o valor de x0 para a próxima iteração
        x0 = xk_new

    return x0, iteracoes

# Função para exibir os resultados formatados
def exibir_resultados_newton(resultados):
    print("MÉTODO DE NEWTON É DETERMINAÇÃO DA RAÍZ z2")
    print(f"{'k':<3} {'xk':<15} {'f(xk)':<20} {'df(xk)':<20} {'ERk':<20}")
    
    for k, xk, fxk, dfxk, er in resultados:
        print(f"{k+1:<3} {xk:<15.10f} {fxk:<20.15e} {dfxk:<20.10e} {er:<20.9e}")

    print(f"Raíz z2 = {resultados[-1][1]:.9f}")

# Valor inicial e execução do método de Newton
raiz_newton, resultados_newton = newton(-7.5)

# Exibindo o resultado formatado
exibir_resultados_newton(resultados_newton)

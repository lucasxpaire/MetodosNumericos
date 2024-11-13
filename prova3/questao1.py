import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Dados fornecidos
x = np.array([1.07118, 0.87691, 0.740587, 1.3449, 1.40753, 1.49681, 0.54692, 1.67324, 0.338935, 0.199134])
y = np.array([0.197905, 0.265178, 0.055113, 2.35749, 2.92806, 4.66274, -0.0632531, 4.30248, 1.17692, 2.21001])
z = 1.03  # Ponto em que estimar

# Função para calcular a tabela de diferenças divididas
def divided_differences(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y  # A primeira coluna são os valores de y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

    return coef

# Função para calcular o valor do polinômio de Newton no ponto z
def newton_interpolating_polynomial(x, coef, z):
    n = len(coef)  # Quantidade de coeficientes
    p = coef[0, 0]  # O primeiro termo é o valor de y_0

    for k in range(1, n):
        term = coef[0, k]
        for j in range(k):
            term *= (z - x[j])
        p += term
    return p

# Calcula a tabela de diferenças divididas
coef = divided_differences(x, y)

# Exibe a tabela de diferenças divididas
print("\nTABELA DE DIFERENÇAS DIVIDIDAS | z =", z)
print("-" * 175)
headers = ["x", "y"] + [f"DD{i}" for i in range(1, len(x))]  # Cabeçalhos das diferenças divididas
table = np.hstack((x.reshape(-1, 1), y.reshape(-1, 1), coef[:, 1:]))  # Tabela de coeficientes
df_table = pd.DataFrame(table, columns=headers)

# Formata e centraliza os valores para exibição
def format_value(val, threshold=1e-10):
    return "-" if abs(val) < threshold else f"{val:.6f}"

formatted_table = df_table.apply(lambda col: col.map(format_value) if col.name != "x" else col)
formatted_table_str = formatted_table.to_string(index=False, col_space=15, justify="center")
print(formatted_table_str)
print("-" * 175 + "\n")

# Calcula as estimativas no ponto z para ordens de 0 a 10
print("ESTIMATIVAS | f(z)")
print("-" * 70)
print(f"{'k':^5} {'Pk(z)':^15} {'Erro relativo':^20}")
print("-" * 70)
estimativas = []
erro_relativo_anterior = None  # Variável para armazenar o erro relativo da iteração anterior

# Armazenando os erros relativos para posterior análise
erros_relativos = []

for k in range(0, 10):
    valor = newton_interpolating_polynomial(x[:k+1], coef[:k+1, :], z)  # Usando coef até k+1
    
    # Cálculo do erro relativo, se k >= 1
    if k == 0:
        erro_relativo = "-"  # Para k=0, não há erro relativo
    else:
        erro_relativo = abs(valor - estimativas[k-1][1]) / abs(valor)  # Erro relativo em relação ao valor anterior
    
    # Armazenando erro relativo
    erros_relativos.append(erro_relativo)
    estimativas.append((k, valor, erro_relativo))
    print(f"{k:^5} {format_value(valor):^15} {format_value(erro_relativo) if erro_relativo != '-' else '-':^20}")

print("-" * 70)

# Analisando o erro relativo e encontrando a aproximação mais confiável
melhor_aproximacao = None
menor_erro_relativo = float('inf')  # Inicializa com um valor grande

for k in range(2, len(erros_relativos)):
    if erros_relativos[k] < menor_erro_relativo:
        menor_erro_relativo = erros_relativos[k]
        melhor_aproximacao = estimativas[k]

if melhor_aproximacao:
    print(f"APROXIMAÇÃO MAIS CONFIÁVEL: k = {melhor_aproximacao[0]}, Pk(z) = {format_value(melhor_aproximacao[1])}")
else:
    print("Não foi encontrada uma estimativa confiável.")

print("-" * 70)
print("\n")

# Gráficos dos polinômios P2, P4, P6, P8
polinomios = [2, 4, 6, 8]  # Ordens dos polinômios a serem plotados
x_vals = np.linspace(min(x)-0.2, max(x)+0.2, 200)  # Ampliando o intervalo de avaliação

plt.figure(figsize=(12, 10))  # Tamanho da figura

for i, k in enumerate(polinomios):
    # Calcula os valores do polinômio
    y_vals = [newton_interpolating_polynomial(x[:k+1], coef[:k+1, :], xv) for xv in x_vals]
    
    plt.subplot(2, 2, i+1)  # Subgráficos organizados em 2 linhas e 2 colunas
    plt.plot(x_vals, y_vals, label=f'$P_{k}(x)$')
    plt.scatter(x, y, color='black', zorder=5)  # Adiciona os pontos originais
    plt.title(f'$P_{k}(x)$')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.legend(loc="best")
    
    # Definindo os limites fixos dos eixos:
    plt.xlim(0, 2)        # Limita o eixo x de 0 a 2
    plt.ylim(-1, 6)       # Limita o eixo y de -1 a 6

plt.subplots_adjust(wspace=0.3, hspace=0.3)  # Ajuste o layout para evitar sobreposição
plt.show()

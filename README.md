# Métodos Numéricos

Este repositório contém implementações em **Python** de diversos algoritmos fundamentais de cálculo numérico. Os scripts foram desenvolvidos para resolver problemas de zeros de funções, sistemas lineares e interpolação polinomial, gerando tabelas detalhadas de iterações e erros relativos.

## 🗂️ Estrutura do Projeto

Os códigos estão organizados por pastas correspondentes às avaliações/tópicos da disciplina:

### 1\. Zeros de Funções (Prova 1)

Algoritmos para encontrar raízes de equações não lineares (f(x) = 0).

  * **Bissecção (`1.bisseccao.py`):** Método intervalar que divide o intervalo repetidamente.
  * **Newton (`2.newton.py`):** Método aberto que utiliza a derivada f'(x) para convergência rápida (quadrática).
  * **Secante (`3.secante.py`):** Similar ao método de Newton, mas substitui a derivada por uma aproximação de diferenças finitas, exigindo dois chutes iniciais.
  * **Falsa Posição (`4.falsaposicao.py`):** Método intervalar similar à bissecção, mas usa a interseção da reta secante com o eixo x.
  * **Horner (`5.horner.py`):** Implementação eficiente para avaliação de polinômios e suas derivadas, utilizada em conjunto com o método de Newton.

### 2\. Sistemas Lineares (Prova 2)

Métodos diretos e iterativos para resolução de sistemas da forma Ax = b.

  * **Métodos Diretos (`1.py`):**
      * Eliminação de Gauss com Pivotamento Parcial.
      * Eliminação de Gauss com Pivotamento Total.
      * Gera tabelas passo a passo usando `pandas` para visualizar a matriz aumentada.
  * **Métodos Iterativos (`2.py`):**
      * Método de Jacobi.
      * Método de Gauss-Seidel.
      * Verifica critérios de convergência e precisão.

### 3\. Interpolação (Prova 3)

  * **Polinômio Interpolador de Newton (`questao1.py`):**
      * Cálculo da tabela de Diferenças Divididas.
      * Estimativa de valores em pontos específicos (f(z)).
      * Análise de erro relativo entre ordens do polinômio.
      * **Visualização Gráfica:** Plota os polinômios de diferentes graus (P2, P4, P6, P8) comparando com os pontos originais usando `matplotlib`.

-----

## 🛠️ Tecnologias e Dependências

Os scripts foram desenvolvidos em **Python 3**. Para executá-los, é necessário instalar as seguintes bibliotecas para manipulação de vetores, tabelas e gráficos:

  * **NumPy:** Computação numérica e operações matriciais.
  * **Pandas:** Formatação e exibição tabular dos dados.
  * **Matplotlib:** Geração de gráficos (usado na interpolação).

### Instalação

Você pode instalar todas as dependências com o comando:

```bash
pip install numpy pandas matplotlib
```

-----

## 🚀 Como Executar

Cada arquivo funciona de maneira independente. A maioria dos scripts já possui dados de entrada (funções, matrizes ou pontos) definidos diretamente no código ou solicita entrada do usuário via terminal.

1.  Navegue até a pasta desejada (ex: `prova1`):
    ```bash
    cd prova1
    ```
2.  Execute o script desejado:
    ```bash
    python 2.newton.py
    ```

### ⚠️ Personalização dos Dados

Como os scripts foram feitos para provas específicas, as funções matemáticas (`f(x)`), matrizes (`A`, `C`) e vetores (`b`, `d`) estão, em sua maioria, **"hardcoded"** (fixos no código).

  * **Para testar com outros problemas:** Abra o arquivo `.py` em um editor de texto e altere as funções `def f(x):`, ou as variáveis de matrizes (`A = np.array([...])`) no início ou final do arquivo antes de executar.

-----

## 📊 Exemplo de Saída

Os algoritmos geram tabelas formatadas no terminal para facilitar a análise de convergência:

```text
MÉTODO DE NEWTON | DETERMINAÇÃO DA RAIZ z2
k    xk                   f(xk)                f'(xk)               ERk                 
0    1.5000000000e+00     2.3450000000e+01     1.2000000000e+01     -                   
1    1.4500000000e+00     ...                  ...                  3.4482758621e-02    
...
Raiz z2 = 1.452345...
```

-----

## ✒️ Autor

  * **Lucas**

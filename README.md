# Avaliação

## Questão 1

Você recebe uma lista de nomes, e uma lista de alturas que consiste de números inteiros positivos distintos.
Ambas as listas são de comprimento `n`.

Para cada índice `i`, `nomes[i]` e `alturas[i]` denotam o nome e a altura da i-ésima pessoa.

Retorne os nomes ordenados em ordem decrescente pelas alturas das pessoas.

### Exemplo 1

```
Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
```

### Exemplo 2

```
Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
```

## Questão 2

Você está subindo uma escada. São necessários `n` degraus para chegar ao topo.

Você pode subir 1 ou 2 degraus de cada vez. De quantas formas distintas você pode escalar até o topo?

### Exemplo 1

```
Input: n = 2
Output: 2
Explicação: Existem duas maneiras de chegar ao topo.
1. 1 degrau + 1 degrau
2. 2 degraus
```

### Exemplo 2

```
Input: n = 3
Output: 3
Explanation: Existem três maneiras de chegar ao topo.
1. 1 degrau + 1 degrau + 1 degrau
2. 1 degrau + 2 degraus
3. 2 degraus + 1 degrau
```

## Questão 3

Você recebe uma lista de preços onde o `preço[i]` é o preço de uma determinada ação no i-ésimo dia.

Você quer maximizar seu lucro escolhendo um único dia para comprar uma ação e escolhendo um dia diferente no futuro para
vender essa ação.

Retorne o lucro máximo que você pode obter com esta transação. Se você não puder obter nenhum lucro, devolva 0.

### Exemplo 1

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explicação: Compre no segundo dia (preço = 1) e venda no dia 5 (preço = 6), lucro = 6-1 = 5.
```

### Exemplo 2

```
Input: prices = [7,6,4,3,1]
Output: 0
Explicação: Não é possível obter lucro, pois o preço de venda deve ser maior que o preço de compra.
```

## Questão 4

Os numerais romanos são representados por sete símbolos diferentes: I, V, X, L, C, D e M.

| Símbolo | Valor |
|---------|-------|
| I       | 1     |
| V       | 5     |
| X       | 10    |
| L       | 50    |
| C       | 100   |
| D       | 500   |
| M       | 1000  |

Por exemplo, 2 é escrito como II em algarismo romano, apenas dois juntos. 12 está escrito como XII,
que é simplesmente X + II. O número 27 está escrito como XXVII, que é XX + V + II.

Os numerais romanos são geralmente escritos da esquerda para a direita, do maior para a menor. Entretanto, o numeral
para quatro não é IIII. Ao invés disso, o número quatro é escrito como IV. Porque o um está antes dos cinco,
subtraindo-o, fazendo quatro. O mesmo princípio se aplica ao número nove, que é escrito como IX. Há seis casos em que a
subtração é utilizada:

* I pode ser colocado antes de V (5) e X (10) para fazer 4 e 9.
* X pode ser colocado antes de L (50) e C (100) para fazer 40 e 90.
* C pode ser colocado antes de D (500) e M (1000) para fazer 400 e 900.

Dado um numeral romano, converta-o para um número inteiro.

## Questão 5

Você recebe uma lista de caminhos, onde `caminhos[i] = [cidadeAi, cidadeBi]` significa que existe um caminho direto que
vai de `cidadeAi` para `cidadeBi`. Retorne a cidade de destino, ou seja, a cidade sem nenhum caminho que saia dela.

### Exemplo 1

```
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explicação: Através de "London" -> "New York" -> "Lima" -> "Sao Paulo", você chega ao destino.
```

### Exemplo 2

```
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explicação: Todos os caminhos possíveis são:
"D" -> "B" -> "C" -> "A".
"B" -> "C" -> "A".
"C" -> "A".
"A".
Portanto, "A" é a cidade de destino.
```

## Desafio

Dada uma lista de números inteiros não-negativos, organize-os de modo que formem o maior número e devolva-o.

Como o resultado pode ser muito grande, é preciso devolver uma string em vez de um número inteiro.

### Exemplo 1

```
Input: nums = [10,2]
Output: "210"
```

### Exemplo 2

```
Input: nums = [3,30,34,5,9]
Output: "9534330"
```
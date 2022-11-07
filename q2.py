# Você está subindo uma escada. São necessários `n` degraus para chegar ao topo.
#
# Você pode subir 1 ou 2 degraus de cada vez. De quantas formas distintas você pode escalar até o topo?
#
# ### Exemplo 1
#
# ```
# Input: n = 2
# Output: 2
# Explicação: Existem duas maneiras de chegar ao topo.
# 1. 1 degrau + 1 degrau
# 2. 2 degraus
# ```
#
# ### Exemplo 2
#
# ```
# Input: n = 3
# Output: 3
# Explanation: Existem três maneiras de chegar ao topo.
# 1. 1 degrau + 1 degrau + 1 degrau
# 2. 1 degrau + 2 degraus
# 3. 2 degraus + 1 degrau
# ```


def q2(n):
    R = [1, 2, 3]
    n -= 3
    x = 1
    n1=1
    n2=2
    while x <= n:
        Rn = R[n1] + R[n2]
        R.append(Rn)
        x += 1
        n1 += 1
        n2 += 1
    R.sort(reverse=True)
    return R[0]


if __name__ == '__main__':
    print(q2(2))

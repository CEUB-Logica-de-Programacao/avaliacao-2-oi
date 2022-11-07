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


def q4(numeral):

    mapa = {
       "I": 1, 
       "V": 5, 
       "X": 10, 
       "L": 50, 
       "C": 100, 
       "D": 500, 
       "M": 1000
       }
    valor = 0
    ult_digito = 0
    
    for digito_rom in numeral[::-1]:             
       valor_digito = mapa[digito_rom]
       if valor_digito >= ult_digito:
           valor += valor_digito
           ult_digito = valor_digito
       else:
           valor -= valor_digito
    return valor



if __name__ == '__main__':
    print(q2(2))

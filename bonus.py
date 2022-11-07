# Dada uma lista de números inteiros não-negativos, organize-os de modo que formem o maior número e devolva-o.
#
# Como o resultado pode ser muito grande, é preciso devolver uma string em vez de um número inteiro.
#
# ### Exemplo 1
#
# ```
# Input: nums = [10,2]
# Output: "210"
# ```
#
# ### Exemplo 2
#
# ```
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
# ```


def bonus(nums):
    lista_len = []

    contador = 9
    while contador != -1:
        lista_provisoria = []
        for num in nums:
            if str(num)[0] == str(contador):
                lista_provisoria.append(str(num))

        if lista_provisoria:
            lista_provisoria.sort(reverse=True)
            lista_len.append(lista_provisoria)
        contador -= 1

    for lista_num in lista_len:
        for num in lista_num:
            if str(num)[len(str(num)) - 1] == '0':
                lista_num.remove(num)
                lista_num.append(num)

    lista_len_str = []
    total = ""
    for lista_num in lista_len:
        for num in lista_num:
            lista_len_str.append(str(num))

    for termo in lista_len_str:
        total += termo
    lista_len_int = []
    for n in total:
        lista_len_int.append(int(n))
    if sum(lista_len_int) == 0:
        return '0'
    print(total)
    return total

if __name__ == '__main__':
    print(bonus([3, 30, 34, 5, 9]))

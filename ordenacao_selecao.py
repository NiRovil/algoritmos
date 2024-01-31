# primeiro criamos uma funcao que identifica o index que possui o menor valor da lista
def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        # se o item atual do loop for menor que o primeiro item da lista
        # substitui o atual menor valor e o indice correspondente
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i

    # retorna o indice que contem o menor valor da lista
    return menor_indice

def ordenarSelecao(arr):
    # criamos um novo array onde iremos anexar os valores ordenados
    novoArr = []

    # para cada item do array base
    for i in range(len(arr)):
        # identificamos o indice que contem o menor valor
        menor = buscaMenor(arr)
        # adicionamos ao novo array e removemos o valor da lista base
        # para que seja usado no loop de busca novamente
        novoArr.append(arr.pop(menor))

    # logo apos retornamos o array ordenado de forma crescente
    return novoArr

print(ordenarSelecao([2,3,1,4,5]))
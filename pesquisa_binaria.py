# Pesquisa binaria consiste na eliminacao da metade dos numeros 
# de uma lista ordenada a cada tentativa de pesquisa, 
# sendo uma das mais rápidas na notacao BigO
# tendo seu tempo estimado em O(log n).

def pesquisa_binaria(lista, item):

    # pode-se ordenar a lista antes de fazer a devida pesquisa, porém por motivos de estudo
    # todas as listas serao pre ordenadas
    
    # primeiro define-se o inicio e o fim da lista
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:

        # a cada tentativa, testa o elemento central do corte
        meio = (inicio + fim) // 2
        chute = lista[meio]

        # se o elemento situado no meio do corte for o item procurado retorna o index do item
        if chute == item:
            return meio
        
        # se o elemento situado no meio do corte for maior que o item procurado, o fim da lista
        # se torna o meio da lista antiga menos 1 index
        if chute > item:
            fim = meio - 1
        
        # se o elemento situado no meio do corte for menor que o item procurado, o inicio da lista
        # se torna o meio da lista antiga mais 1 index
        else:
            inicio = meio + 1

    # caso o item não exista retorna um valor nulo
    return None

minha_lista = [1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 3))
print(pesquisa_binaria(minha_lista, 7))
print(pesquisa_binaria(minha_lista, -2))
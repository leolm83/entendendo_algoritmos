def busca_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1 
    while baixo <= alto:
        meio = (baixo + alto) // 2 # // arredonda o resultado para baixo
        chute = lista[meio]
        if (chute == item):
            return meio
        if chute > item :
            alto = meio - 1
        else:
            baixo = meio + 1
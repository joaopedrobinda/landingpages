def pesquisa_binaria (lista, item):
    baixo = 0
    alto = len(lista) - 1 # o - 1 é apenas para não estourar o array que começa em zero
    while baixo <= alto: #pois o baixo e alto vão variar conforme o chute
        meio = (baixo + alto) //2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio -1
        else:
            baixo = meio +1
    return None
minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
item = 12
resultado = pesquisa_binaria(minha_lista, item)
print (resultado)
        
    
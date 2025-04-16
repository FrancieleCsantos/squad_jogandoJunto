#Em lista, imprimimos os indices assim:
idades = [10, 15, 21, 18, 20]
print (idades[0])

#TODO: Imprima em For os indices


# o len retorna o tamanho da lista enquanto o range gera os números de acordo com o tamanho da lista
for i in range(len(idades)):
    if idades[i] >= 18:
        print(f"Índice {i}: Indivíduo possui idade mínima para dirigir")



# o enumerate é uma função do python que recebe uma lista e retorna um objeto iterável com índice e valor, exemplo: (0, 10)
for indice, idade in enumerate(idades):
    if idade >= 18:
        print (f"Índice {indice}: Indivíduo possui idade mínima para dirigir")
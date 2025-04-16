def par(x):
    return x % 2 == 0

def multiplicar_por_2(x):
    return x * 2

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# TODO 1.1: Filtrar apenas os números pares
# no filter eu passo primeiro a função que vai retornar true ou false nesse caso, o que for true vai ser mantido na lista
pares = filter(par, numeros)

# TODO 1.2: Multiplicar cada número por 2
# no map eu passo primeiro a função que será aplicada a todos os elementos da lista
multiplicados = map(multiplicar_por_2, pares)

# TODO 1.3: Ordenar a lista em ordem decrescente
resultado = sorted(multiplicados, reverse=True)

print(resultado)


#isinstance é para verificar se é uma string
def string(x):
    return isinstance(x, str)

#upper é para transformar em maiusculas
def para_maiusculas(x):
    return x.upper()

# é uma tupla contendo diferentes tipos de dados, como string e inteiros
dados = ("maçã", 10, "banana", 5, "laranja", "uva", 20)

# TODO 2.1: Filtrar apenas os elementos que são strings
somente_strings = filter(string, dados)

# TODO 2.2: Converter as strings para letras maiúsculas
maiusculas = map(para_maiusculas, somente_strings)

# TODO 2.3: Ordenar as strings em ordem alfabética
resultado = tuple(sorted(maiusculas))

print(resultado)


#startswith verifica se a palavra começa com a
def comeca_com_a(palavra):
    return palavra.lower().startswith("a")

def para_maiusculas(palavra):
    return palavra.upper()

# Um set é uma coleção não ordenada de elementos únicos.
palavras = {"banana", "Abacate", "pera", "Amora", "uva", "aveia"}

# TODO 3.1: Filtrar palavras que começam com a letra 'a' (maiúscula ou minúscula)
comeca_com_a_palavras = filter(comeca_com_a, palavras)

# TODO 3.2: Converter para letras maiúsculas
maiusculas = map(para_maiusculas, comeca_com_a_palavras)

# TODO 3.3: Ordenar e converter em conjunto
ordenadas = sorted(maiusculas)

resultado = set(ordenadas)

print(resultado)



def string_com_mais_de_3(x):
    return isinstance(x, str) and len(x) > 3

def para_minusculas(x):
    return x.lower()

# um dicionário é uma estrutura de dados que armazena pares de chave e valor.
dicionario = {
    "a": 10,
    "b": "banana",
    "c": "abacaxi",
    "d": 5,
    "e": "uva",
    "f": "melancia"
}

# TODO 4.1: Obter valores do dicionário
valores = dicionario.values()

# TODO 4.2: Filtrar strings com mais de 3 letras
filtradas = filter(string_com_mais_de_3, valores)

# TODO 4.3: Converter para letras minúsculas
minusculas = map(para_minusculas, filtradas)

# TODO 4.4: Ordenar em ordem alfabética
resultado = sorted(minusculas)

print(resultado)
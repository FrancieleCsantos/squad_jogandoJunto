def par(x):
    return x % 2 == 0

def multiplicar_por_2(x):
    return x * 2

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = filter(par, numeros)

multiplicados = map(multiplicar_por_2, pares)

resultado = sorted(multiplicados, reverse=True)

print(resultado)



def string(x):
    return isinstance(x, str)

def para_maiusculas(x):
    return x.upper()

dados = ("maçã", 10, "banana", 5, "laranja", "uva", 20)

somente_strings = filter(string, dados)

maiusculas = map(para_maiusculas, somente_strings)

resultado = tuple(sorted(maiusculas))

print(resultado)



def comeca_com_a(palavra):
    return palavra.lower().startswith("a")

def para_maiusculas(palavra):
    return palavra.upper()

palavras = {"banana", "Abacate", "pera", "Amora", "uva", "aveia"}

comeca_com_a_palavras = filter(comeca_com_a, palavras)

maiusculas = map(para_maiusculas, comeca_com_a_palavras)

ordenadas = sorted(maiusculas)
resultado = set(ordenadas)

print(resultado)



def string_com_mais_de_3(x):
    return isinstance(x, str) and len(x) > 3

def para_minusculas(x):
    return x.lower()

dicionario = {
    "a": 10,
    "b": "banana",
    "c": "abacaxi",
    "d": 5,
    "e": "uva",
    "f": "melancia"
}

valores = dicionario.values()
filtradas = filter(string_com_mais_de_3, valores)

minusculas = map(para_minusculas, filtradas)

resultado = sorted(minusculas)

print(resultado)
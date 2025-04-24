def processar_numeros(lista):
    resultado = []
    for numero in lista:
        if numero % 2 == 0:
            resultado.append(numero * 2)
    return sorted(resultado, reverse=True)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(processar_numeros(numeros))




def processar_dados(dados):
    resultado = []
    for item in dados:
        if isinstance(item, str):
            resultado.append(item.upper())
    return tuple(sorted(resultado))

dados = ("maçã", 10, "banana", 5, "laranja", "uva", 20)
print(processar_dados(dados))




def palavras_com_a(palavras):
    resultado = []
    for palavra in palavras:
        if palavra.lower().startswith("a"):
            resultado.append(palavra.upper())
    return set(sorted(resultado))

palavras = {"banana", "Abacate", "pera", "Amora", "uva", "aveia"}
print(palavras_com_a(palavras))




def filtrar_strings(dicionario):
    resultado = []
    for valor in dicionario.values():
        if isinstance(valor, str) and len(valor) > 3:
            resultado.append(valor.lower())
    return sorted(resultado)

dicionario = {
    "a": 10,
    "b": "banana",
    "c": "abacaxi",
    "d": 5,
    "e": "uva",
    "f": "melancia"
}
print(filtrar_strings(dicionario))
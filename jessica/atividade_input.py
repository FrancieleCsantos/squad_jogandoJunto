#Faça um programa que capture o nome do usuário, altura em metros, idade e imprima esses dados na tela.

nome = input("Seja bem-vindo! Qual é o seu nome? ")
altura = input(f"Olá, {nome}! Qual é sua altura (em metros) ? ")
idade = input(f"Quantos anos você tem? ")

print(f"\n{nome}, você tem {idade} anos e mede {altura} metros. Legal, né?")
print("-------------------------------------------------------------------")


# Nova feature 
# Insira duas variáveis com espaço para o input e uma terceira com o valor somado da operação.
# Deve informar o tipo do dado

primeiro_numero = float(input(f"Olá, {nome}! Agora chegamos a segunda parte, por favor, digite um número: "))
segundo_numero = float(input("Digite outro número: "))
soma = primeiro_numero + segundo_numero
print(f"{nome}, o resultado da soma de {primeiro_numero} + {segundo_numero} é {soma}.")

tipo_primeiro_numero = type(primeiro_numero)
tipo_segundo_numero= type(segundo_numero)
tipo_soma= type(soma) 

print("-------------------------------------------------------------------")
print("Tipo de dado de 'primeiro número': ",tipo_primeiro_numero)
print("Tipo de dado de 'segundo número': ", tipo_segundo_numero)
print("Tipo de dado de 'soma': ", tipo_soma) 




nome_tutor = input("Qual o nome do responsável pelo cachorro? ")
nome_cachorro = input("Qual o nome do cachorro? ")
idade_humana = int(input(f"Quantos anos {nome_cachorro} tem? "))
calculo_idade = idade_humana * 7 
print(f"Legal! {nome_cachorro} tem {calculo_idade} anos de cachorro.")

print(f"Qual é o porte do {nome_cachorro}?")
print("1 - Porte pequeno")
print("2 - Porte médio")
print("3 - Porte grande")
porte_cachorro = input("Digite a opção: ")

valor_banho = 0
custo_banho = 0

if porte_cachorro == "1":
    valor_banho = 50
    custo_banho = 5
elif porte_cachorro == "2":   
    valor_banho = 60
    custo_banho = 15
elif porte_cachorro == "3":   
    valor_banho = 75
    custo_banho = 20
else:
    print("Opção de porte selecionada desconhecida.")


lucro = valor_banho - custo_banho
calculo_lucro_meses = lucro * 12
print(f"Olá, {nome_cachorro} tem {calculo_idade} anos e nos últimos 12 meses o lucro com este animal foi de R${calculo_lucro_meses:.2f}.")





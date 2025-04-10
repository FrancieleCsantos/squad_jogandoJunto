# case Idade do Pet e Lucro do PETSHOP
nome_pet = input("Qual o nome do pet?")

idade_humana = int(input("Qual é a idade do seu cachorro? "))

idade_cachorro = idade_humana * 7


print(f"Legal!{nome_pet} tem {idade_cachorro} anos humanos. ")

print("Escolha o porte do seu animal:")
print("1 - Pequeno")
print("2 - Médio")
print("3 - Grande")

opcao = input("Digite o número correspondente ao porte (1, 2 ou 3): ")

if opcao == "1":
    banho = 50
    custo = 5
    lucro = banho - custo
    lucro_anual = lucro * 12
    print(f"Olá, {nome_pet} tem {idade_cachorro} anos e nos últimos 12 meses o lucro com este animal foi R$:{lucro_anual:.2f})")
elif opcao == "2":
   banho = 60
   custo = 15
   lucro = banho - custo
   lucro_anual = lucro * 12
   print(f"Olá, {nome_pet} tem {idade_cachorro} anos e nos últimos 12 meses o lucro com este animal foi R$:{lucro_anual:.2f})")
elif opcao == "3":
   banho = 75
   custo = 20
   lucro = banho - custo
   lucro_anual = lucro * 12
   print(f"Olá, {nome_pet} tem {idade_cachorro} anos e nos últimos 12 meses o lucro com este animal foi R${lucro_anual:.2f})")
else:
    print("Não foi possível calcular o lucro com o porte informado")


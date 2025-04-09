nome = input("Olá, aluno! Digite o seu nome: ")
primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))
terceira_nota = float(input("Digite sua terceira nota: "))
quarta_nota = float(input("Digite sua quarta nota: "))

media = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4

print(f"Olá, {nome}! Sua média é {media:.0f} pontos")


""""
nome = input("Olá, aluno! Digite o seu nome: ")
primeira_nota = float(input("Digite sua primeira nota: ").replace(",", "."))
segunda_nota = float(input("Digite sua segunda nota: ").replace(",", "."))
terceira_nota = float(input("Digite sua terceira nota: ").replace(",", "."))
quarta_nota = float(input("Digite sua quarta nota: ").replace(",", "."))

media = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4

print(f"Olá, {nome}! Sua média é {media:.0f} pontos")

"""
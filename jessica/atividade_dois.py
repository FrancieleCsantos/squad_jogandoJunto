clientes = [
    {"nome": "PAULA MARTINS", "mes": "JANEIRO", "valor": 500.00, "cupom": "PAULAÉ10"},
    {"nome": "JOÃO SILVA", "mes": "FEVEREIRO", "valor": 350.00, "cupom": "JOÃOÉ10"},
    {"nome": "MARIA OLIVEIRA", "mes": "MARÇO", "valor": 720.00, "cupom": "MARIAÉ10"},
    {"nome": "CARLOS SANTOS", "mes": "ABRIL", "valor": 430.00, "cupom": "CARLOSÉ10"},
    {"nome": "ANA COSTA", "mes": "MAIO", "valor": 600.00, "cupom": "ANAÉ10"},
    {"nome": "PEDRO ALVES", "mes": "JUNHO", "valor": 250.00, "cupom": "PEDROÉ10"},
    {"nome": "FERNANDA LIMA", "mes": "JULHO", "valor": 800.00, "cupom": "FERNANDAÉ10"},
    {"nome": "LUIS MELO", "mes": "AGOSTO", "valor": 400.00, "cupom": "LUISÉ10"},
    {"nome": "BEATRIZ SOUZA", "mes": "SETEMBRO", "valor": 550.00, "cupom": "BEATRIZÉ10"},
    {"nome": "ROBERTO NUNES", "mes": "OUTUBRO", "valor": 320.00, "cupom": "ROBERTOÉ10"},
]

for cliente in clientes:
    print(f"Olá, {cliente['nome']}. Em {cliente['mes']} você realizou uma compra no valor de R${cliente['valor']:.2f} e ganhou um desconto de 10% em sua próxima compra. Use o cupom {cliente['cupom']}.")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
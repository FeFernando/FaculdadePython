

produtos = [
    {"Nome" : "Cebola", "Preco": 2.75, "Quantidade": 20},
    {"Nome" : "Cebola", "Preco": 2.75, "Quantidade": 20},
    {"Nome" : "Cebola", "Preco": 2.75, "Quantidade": 20}
]

while True:
    opcao = int( input("1 - Exibir lista de produtos \n2 - Sair do menu \n" ))

    if opcao == 1:
        print(produtos)
    if opcao == 2:
        break
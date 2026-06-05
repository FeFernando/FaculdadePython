estoque = {
    "Sabao": {"quantidade": 3, "preco": 2.50},
    "Detergente": {"quantidade": 5, "preco": 5.50}
}

while True:
    opcao = int( input("1 - Visualizar Estoque Atual \n "
                       "2 - Registrar Entrada de Produto \n "
                       "3 - Registrar Saída de Produto \n "
                       "4 - Sair do Sistema\n" ))

    if opcao == 1:
        for produto, dados in estoque.items():
            print(f"{produto} - Quantidade: {dados['quantidade']} - Preço: R${dados['preco']:2f}")

    if opcao == 2:
        nome_produto = input("Digite o nome do produto")
        nova_quantidade = int(input("Digite a quantidade"))

        if nome_produto in estoque:
            estoque[nome_produto]['quantidade'] += nova_quantidade
            print("Quantidade Atualizada!")
        else:
            print("Produto não encontrado")
    # Opção 3 - saída de produto
    if opcao == 3:
        nome_produto = input("Digite o nome do produto: ")
        quantidade_saida = int(input("Digite a quantidade: "))

        if nome_produto in estoque:

            if estoque[nome_produto]['quantidade'] >= quantidade_saida:
                estoque[nome_produto]['quantidade'] -= quantidade_saida
                print("Saída registrada com sucesso!")

            else:
                print("Estoque insuficiente")

        else:
            print("Produto não encontrado")
    elif opcao == 4:
        break
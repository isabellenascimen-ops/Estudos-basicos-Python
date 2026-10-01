produtos = []

while True:
    print("\n=== CONTROLE DE ESTOQUE ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Vender produto")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))

        produto = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }

        produtos.append(produto)

        print("Produto cadastrado!")

    elif opcao == "2":
        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            for produto in produtos:
                print("\nProduto:", produto["nome"])
                print("Preço: R$", produto["preco"])
                print("Quantidade:", produto["quantidade"])

                if produto["quantidade"] <= 5:
                    print("ATENÇÃO: Estoque baixo!")

    elif opcao == "3":
        nome = input("Qual produto deseja vender? ")
        encontrado = False

        for produto in produtos:
            if produto["nome"].lower() == nome.lower():
                encontrado = True

                quantidade = int(input("Quantidade vendida: "))

                if quantidade <= produto["quantidade"]:
                    produto["quantidade"] -= quantidade
                    print("Venda registrada!")
                else:
                    print("Quantidade insuficiente em estoque.")

        if not encontrado:
            print("Produto não encontrado.")

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
clientes = []

while True:
    print("\n=== CADASTRO DE CLIENTES ===")
    print("1 - Adicionar cliente")
    print("2 - Listar clientes")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        email = input("E-mail: ")
        telefone = input("Telefone: ")

        cliente = {
            "nome": nome,
            "email": email,
            "telefone": telefone
        }

        clientes.append(cliente)

        print("Cliente cadastrado!")

    elif opcao == "2":
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in clientes:
                print("\nNome:", cliente["nome"])
                print("E-mail:", cliente["email"])
                print("Telefone:", cliente["telefone"])

    elif opcao == "3":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
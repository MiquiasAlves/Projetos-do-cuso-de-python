# Definindo a lista de compras vazia
lista_compras = []
# Loop infinito para que o usuário possa adicionar itens à lista de compras
while True:
    # Exibindo as opções para o usuário
    print("O que você deseja fazer?")
    print("1. Adicionar item à lista de compras")
    print("2. Exibir lista de compras")
    print("3. Exibir total da compra")
    print("4. Sair")
    # Capturando a opção escolhida pelo usuário
    opcao = input("Opção escolhida: ")
    # Verificando a opção escolhida pelo usuário
    if opcao == "1":
        # Capturando o item e o valor a ser adicionado à lista de compras
        item = input("Digite o item a ser adicionado à lista de compras: ")
        valor = float(input("Digite o valor do item: "))
        # Adicionando o item e o valor à lista de compras como uma tupla
        lista_compras.append((item, valor))
        # Exibindo mensagem de confirmação
        print(f"{item} adicionado à lista de compras")
    elif opcao == "2":
        # Exibindo a lista de compras
        print("Lista de compras:")
        for item, valor in lista_compras:
            print(f"- {item}: R${valor:.2f}")
    elif opcao == "3":
        # Calculando o total da compra
        total = sum([valor for item, valor in lista_compras])
        # Exibindo o total da compra
        print(f"Total da compra: R${total:.2f}")
    elif opcao == "4":
        # Encerrando o programa
        print("Encerrando o programa")
        break
    else:
        # Exibindo mensagem de erro para opções inválidas
        print("Opção inválida. Tente novamente.")
# Exibindo a lista completa de compras
print("Lista completa de compras:")
for item, valor in lista_compras:
    print(f"- {item}: R${valor:.2f}")
# Calculando e exibindo o total da compra
total = sum([valor for item, valor in lista_compras])
print(f"Total da compra: R${total:.2f}")

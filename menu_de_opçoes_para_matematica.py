while True:
    try:
        n1 = int(input('Primeiro valor: ')) # Solicita o primeiro valor inteiro
        n2 = int(input('Segundo valor: ')) # Solicita o segundo valor inteiro
        break # Se não houver erro, sai do loop e continua a execução
    except ValueError: # Trata a exceção de um valor não inteiro
        print('Ops! Apenas números inteiros são permitidos. Tente novamente.')
opcao = 0
while opcao != 5:
    print('''    [1] Somar 
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    try:
        opcao = int(input('>> Qual é a sua opção: ')) # Solicita a opção escolhida
        if opcao == 1:
            soma = n1 + n2
            print(f'A soma entre {n1} + {n2} é {soma}')
        elif opcao == 2:
            mult = n1 * n2
            print(f'O resultado entre {n1} x {n2} é {mult}')
        elif opcao == 3:
            maior = max(n1, n2)
            print(f'O maior entre {n1} e {n2} é {maior}')
        elif opcao == 4:
            while True:
                try:
                    n1 = int(input('Primeiro valor: ')) # Solicita o primeiro valor inteiro novamente
                    n2 = int(input('Segundo valor: ')) # Solicita o segundo valor inteiro novamente
                    break # Se não houver erro, sai do loop e continua a execução
                except ValueError: # Trata a exceção de um valor não inteiro
                    print('Ops! Apenas números inteiros são permitidos. Tente novamente.')
        elif opcao == 5:
            print('Finalizando o programa...')
        else:
            print('Opção inválida. Tente novamente.')
    except ValueError: # Trata a exceção de um valor não inteiro
        print('Ops! Apenas números inteiros são permitidos. Tente novamente.')
print('Programa finalizado!') # Exibe a mensagem de finalização do programa

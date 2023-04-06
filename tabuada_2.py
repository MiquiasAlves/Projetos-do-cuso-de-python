while True:  # Inicia um loop infinito
    print('------' * 10) 
    opcao = int(input('Digite um número para ver a sua tabuada: '))  # Solicita ao usuário um número para ver a sua tabuada
    print('------' * 10) 
    for num in range(1,11):  # Inicia um loop para tabuada do número digitado pelo usuário
        print(f'{opcao} x {num} = {opcao * num}')  # fórmula da tabuada
    if opcao < 0:  # Se o número digitado pelo usuário for negativo, o programa encerra o loop
        print('----' * 10) 
        print(f'{opcao }, Número inválido para calculadora')  # mensagem informando que o número é inválido para a calculadora
        print('----' * 10)  
        break  # Encerra o loop principal
print('----' * 5)  
print('Programa encerrado')  # mensagem indicando que o programa foi encerrado
print('----' * 5) 

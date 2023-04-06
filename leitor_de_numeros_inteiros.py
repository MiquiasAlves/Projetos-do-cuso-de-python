print('---' * 10) 
print('LEITOR DE NÚMEROS INTEIROS')  # título do programa
print('---' * 10)
cont = resp = soma = 0 
while True:  # Inicia um loop infinito
    resp = int(input('Digite um número inteiro: '))  # Solicita ao usuário um número inteiro
    print('[999] Para fechar o programa')  # Indica ao usuário que 999 encerra o programa
    if resp == 999:  # Se o usuário digitar 999, o programa encerra o loop
        break
    soma += resp  # Soma o número digitado à variável de soma
    cont += 1 
print('Programa encerrado')  # mensagem indicando que o programa foi encerrado
print(f'A quantidade números digitados foram {cont}, todos estes números somados é {soma}')  # Imprime a quantidade de números digitados e a soma total de todos os números digitados

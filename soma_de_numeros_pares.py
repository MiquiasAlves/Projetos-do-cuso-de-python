soma = 0
numeros_pares = [] # lista vazia para armazenar os números pares
for i in range(6): # Loop que pede para o usuário digitar 6 números inteiros
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0: # Verifica se o número é par
        soma += num # Adiciona o número à variável soma se for par
        numeros_pares.append(num) # Adiciona o número à lista numeros_pares se for par
# soma dos números pares e a lista de números pares
print('A soma dos números pares é:', soma)
print(numeros_pares)
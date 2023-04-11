# Cria uma lista vazia para armazenar os números
numbers = []
# Loop que lê os números digitados pelo usuário e os adiciona à lista
while True:
    number_str = input("Digite um número (ou 'fim' para terminar): ")
    if number_str == "fim":
        break
    try:
        number = float(number_str) # Converte a entrada do usuário em um número real
        numbers.append(number) # Adiciona o número à lista de números
    except ValueError: # Trata erros de entrada inválida
        print("Entrada inválida.")
# Verifica se a lista de números não está vazia
if len(numbers) == 0:
    print("Não há números para ordenar.")
else:
    numbers.sort() # Ordena a lista em ordem crescente
    print("A lista ordenada é:")
    print(numbers) # Exibe a lista ordenada



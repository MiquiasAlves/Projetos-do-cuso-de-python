print('=====' * 7) 
print('CARRINHO DE COMPRAS')
print('=====' * 7)

total = acima = menor = cont = 0  # Inicializa as variáveis que serão utilizadas para armazenar as informações do carrinho
barato = ''

# Inicia um loop para adicionar produtos ao carrinho
while True:
    produto = str(input('Digite qual é o nome do produto: '))
    preço = float(input('Digite o valor do produto em R$: '))
    cont += 1  # Contador de produtos adicionados ao carrinho
    total += preço  # Soma o preço do produto ao valor total da compra

    if preço > 1000:
        acima += 1  # Contador de produtos acima de R$ 1000.00

    if cont == 1 or preço < menor:
        menor = preço
        barato = produto  # Armazena o nome e valor do produto mais barato

    resp = ' '
    while resp not in 'SN':    
        resp = str(input('Deseja continuar a compra [S/N]: ' )).upper().strip()[0]  # Pergunta se o usuário quer adicionar mais produtos

    if resp == 'N': 
        break  # Sai do loop se o usuário não quiser adicionar mais produtos
print('=====' * 7)
print(f'O seu carrinho de compra soma o valor de R$ {total:.2f}')
print(f'A quantidade de produtos acima de R$ 1000.00 é: {acima}')
print(f'O produto com valor mais baixo foi ({barato}), que custa: R$ {menor:.2f}')
print('FIM DO PROGRAMA')
print('=====' * 7) 


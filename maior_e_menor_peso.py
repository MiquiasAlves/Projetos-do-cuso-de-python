print('========' * 4)
print('Pesquisa de peso')
print('========' * 4)
# variáveis de maior e menor peso com valores iniciais
maior_peso = 0
menor_peso = float('inf')
# Loop para ler os pesos das 5 pessoas
for i in range(5):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i+1)))
    # Atualiza as variáveis de maior e menor peso, se necessário
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
# Exibe os resultados
print('Maior peso lido: {:.1f}'.format(maior_peso))
print('Menor peso lido: {:.1f}'.format(menor_peso))
print ('=======' * 4)
print('Números ímpares entre 1 até 500')
print ('=======' * 4)
soma = 0
cont = 0
for c in range(1, 501, 2):  # percorre apenas os números ímpares de 1 a 500
    if c % 3 == 0:  # verifica se o número é múltiplo de três
        cont = cont + 1
        soma += c  # adiciona o número à soma
print(f'A soma dos números {cont} ímpares múltiplos de três entre 1 e 500 é {soma}.')
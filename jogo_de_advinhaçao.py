from random import randint
# Gera um número aleatório entre 0 e 10 e atribui a variável "computador"
computador = randint(0,10)
palpites = 0
# Exibe uma mensagem para o usuário
print('-=-=-' * 10)
print('Acabei de pensar em número, entre 0 e 10')
print('-=-=-' * 10)
print('Tente adivinhar que número é este')
print('-=-=-' * 10)

# Inicializa a variável "acertou" como False
acertou = False
# Enquanto o jogador não acertar o número, solicita um palpite e conta os palpites
while not acertou:
    jogador = int(input('Qual é seu palpite: '))
    palpites += 1
    # Verifica se o palpite é igual ao número gerado pelo computador
    if jogador == computador:
        acertou = True
    # Verifica se o palpite é maior que 10
    elif jogador > 10:
        print('Digite um número válido')
    # Se o palpite não for igual ao número gerado pelo computador, exibe uma dica para o jogador
    else:
        if jogador < computador:
            print('Mais... tente novamente')
        elif jogador > computador:
            print('Menos... tente mais uma vez')
# Exibe uma mensagem de sucesso para o jogador e informa quantos palpites foram necessários para acertar o número
print('Você acertou o número que escolhi! Boa!')
print(f'Acertou com {palpites} tentativas.')

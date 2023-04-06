# cabeçalho para o menu de banco
print('====' * 8)
print('MENU DE BANCO PARA SAQUE')
print('====' * 8)
# Solicita o valor de saque ao usuário e armazena na variável 'valor'
valor = int(input('Que valor você quer sacar? R$ '))
# Inicializa as variáveis para contagem de cédulas
total = valor
ced = 50
totced = 0
# Loop para calcular as cédulas necessárias para o saque
while True:
    # Se o valor restante for maior ou igual à cédula atual, diminui o valor total e aumenta o contador de cédulas daquela denominação
    if total >= ced:
        total -= ced
        totced += 1
    else:
        # Se o contador de cédulas daquela denominação for maior que zero, imprime a quantidade de cédulas daquela denominação
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        # Muda a denominação da cédula para a próxima menor
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        # Se o valor total for zero, interrompe o loop
        if total == 0:
            break
# mensagem indicando que o programa foi finalizado
print('Programa fechado')

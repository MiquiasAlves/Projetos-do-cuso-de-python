from random import randint 
print('=========' * 6) 
print('JOGO DE PAR OU ÍMPAR')  # título do jogo
print('=========' * 6)

v = 0
while True:  # Inicia o loop principal do jogo
    opçao = int(input('Digite um número: '))  # Solicita ao usuário que digite um número
    computador = randint(0,10)  # O computador escolhe um número aleatório entre 0 e 10
    resultado = opçao + computador  # Calcula a soma dos números escolhidos pelo usuário e pelo computador
    escolha = ' '
    while escolha not in 'PI':  # Enquanto a escolha não for 'P' ou 'I', o programa continuará solicitando que o usuário digite uma escolha válida
        escolha = str(input('Par ou ímpar [P/I]: ')).upper().strip()[0]  # Solicita que o usuário escolha par ou ímpar e converte a escolha para maiúsculas
        
    print(f'Você jogou {opçao} e o computador {computador}. Total é {resultado}')
    if escolha == 'P':  # Se o usuário escolheu par
        if resultado % 2 == 0:  # E o resultado é par
            print('Você ganhou')  # O usuário ganha
            v += 1  # Adiciona uma vitória ao placar do usuário
        else:  # Caso contrário
            print('Você perdeu')  # O usuário perde
            break  # O loop principal é encerrado
    elif escolha == 'I':  # Se o usuário escolheu ímpar
        if resultado % 2 == 1:  # E o resultado é ímpar
            print('Você ganhou')  # O usuário ganha
            v += 1  # Adiciona uma vitória ao placar do usuário
        else:  # Caso contrário
            print('Você perdeu')  # O usuário perde
            break  # O loop principal é encerrado

    print('Vamos jogar novamente')  # O programa solicita que o usuário jogue novamente

print(f'GAME OVER! Você venceu {v} vezes.')

from random import choice # Importa a função "choice" do módulo "random"
from time import sleep # Importa a função "sleep" do módulo "time"
print('----'*10)
print('Vamos brincar de Jokenpô!') # Exibe uma mensagem de boas-vindas
print('----'*10)
escolhas = ['pedra', 'papel', 'tesoura'] # Opções disponíveis para o jogo em uma lista
computador = choice(escolhas) # Escolhendo aleatoriamente a jogada do computador usando a função "choice"
while True: # Entra em um loop while que solicita ao usuário para escolher uma jogada até que o usuário faça uma escolha válida
    usuario = (input('Escolha entre Pedra, Papel e Tesoura? ')).lower()
    if usuario in escolhas:
        break
    else:
        print("Opção inválida. Por favor, digite pedra, papel ou tesoura.")
print('----'*10)
if usuario == computador: # Verifica quem ganhou o jogo com base nas regras do "Pedra, Papel e Tesoura"
    print(f'Empate, escolhemos {computador}. Hahaha')
elif usuario == 'pedra' and computador == 'tesoura':
    print('Processando...')
    sleep(1)  # Pausa a execução por antes de exibir o resultado
    print('Você ganhou')
    print('----'*10)
elif usuario == 'papel' and computador == 'pedra':
    print('Processando...')
    sleep(1)
    print('Você ganhou')
    print('----'*10)
elif usuario == 'tesoura' and computador == 'papel':
    print('Processando...')
    sleep(1)
    print('Você ganhou')
    print('----'*10)
else:
    print('Processando...')
    sleep(1)
    print(f'Eu ganhei! Haha, eu escolhi {computador}.')
    print('----'*10)
from time import sleep # Importa a função sleep do módulo time
segundos = int(input('Digite quantos segundos para iniciar os fogos: ')) # usuário digite quantos segundos para iniciar os fogos
for c in range(segundos, 0, -1,): # Loop que percorre todos os segundos de 'segundos' até 0
    print(c)
    (sleep(1.5)) # Pausa a execução do programa por 1,5 segundos
print('Inicou as explosão dos fogos!') # mensagem indicando que os fogos foram iniciados
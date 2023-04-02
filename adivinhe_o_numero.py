import random # importada para gerar um número aleatório entre 0 e 5.
from time import sleep # importada para introduzir um atraso de 3 segundos antes de exibir o resultado.
numero = random.randint(0,5) # Gera um número aleatório entre 0 e 5
# solicita que o usuário faça um palpite
print('-=-' * 20)
palpite = int(input('Adivinhe um número entre 0 e 5: ')) 
print('-=-' * 20)
print('Processando...') # Mostra uma mensagem de processamento
sleep(3)
# Verifica se o palpite está dentro do intervalo válido
if palpite < 0 or palpite > 5:
    print("Desculpe, o número deve estar entre 0 e 5.")
if palpite == numero:
    print('Parabéns, você acertou!')
else:
    print(f'Infelizmente você errou. O número escolhido foi {numero}.')
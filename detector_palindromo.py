frase = input('Digite uma frase para descobrir se é um palíndromo: ')
frase_sem_espacos = frase.replace(' ', '').lower() # Remove os espaços da frase e converte tudo para minúsculas
frase_invertida = frase_sem_espacos[::-1] # Inverte a frase sem espaços
# Verifica se a frase original sem espaços é igual à frase invertida
if frase_sem_espacos == frase_invertida:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')

# Exemplos:
# Apos a sopa
# A sacada da casa
# A torre da derrota 
# O lobo ama o bolo 
# A base do teto desaba
# A mala nada na lama
# Solicita que o usuário digite um número inteiro
num = int(input('Digite um número inteiro: '))
for i in range(1, 11): # Loop que dos números de 1 a 10
    resultado = num * i # Calcula o resultado da multiplicação
    print(f'{num} x {i} = {resultado}') # mostra a linha da tabuada com o já com formato 
# mensagem de introdução
print('------' * 13)
print('Vamos decobrir quais números pares tem de 0 até o número da sua escolha!')
print('------' * 13)
num2 = int(input('Digite um número: ')) # Solicita que o usuário digite o número de finalização
for c in range(0, num2+2, 2): # Loop que percorre todos os números pares de 0 até num2
    print(c)
print (f'Estes são os números pares entre 0 e {num2}!') # mensagem indicando que a contagem foi finalizada
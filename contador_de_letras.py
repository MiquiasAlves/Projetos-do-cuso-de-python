name = str(input('Digite seu nome completo: ')) # Solicita que o usuário digite seu nome completo e armazena em uma variável 'name'
print('Analisando seu nome...') # mensagem indicando que o nome está sendo analisado
print('Seu nome em letras maiúsculas é {}'.format(name.upper())) # Imprime o nome do usuário em letras maiúsculas usando o método 'upper()' da string 'name'
print('Seu nome em minúsculas é {}'.format(name.lower())) # nome do usuário em letras minúsculas usando o método 'lower()' da string 'name'
print('Seu nome tem ao todo {} letras'.format(len(name.replace(' ','')))) # Remove os espaços em branco da string 'name' e retorna o comprimento da string sem espaços em branco usando a função 'len()'
name1 = name.split() # Separa o nome completo do usuário em uma lista de palavras usando o método 'split()' da string 'name'
print('Seu primeiro nome é {}, tem {} letras'.format(name1[0], len(name1[0]))) # retorna o primeiro nome da lista e o comprimento do primeiro nome usando a função 'len()'
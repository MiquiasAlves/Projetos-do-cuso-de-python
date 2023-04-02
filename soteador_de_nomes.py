import random # ou from random import shurflle
# solicitando os nomes dos participantes
name1 = (input('Digite o nome do primeiro aluno: '))
name2 = (input('Digite o nome do segundo aluno: '))
name3 = (input('Digite o nome do terceiro aluno: '))
name4 = (input('Digite o nome do quarto aluno: '))
name5 = (input('Digite o nome do quinto aluno '))
ordem_apresentaçao = [name1, name2, name3, name4, name5] # cria uma lista com as variáveis
random.shuffle(ordem_apresentaçao) # embaralhando a lista com os nomes aleatoriamente
# imprimindo a lista com a ordem de apresentação dos alunos
print('ordem_apresentaçao:')
for nome in ordem_apresentaçao:
    print(nome)
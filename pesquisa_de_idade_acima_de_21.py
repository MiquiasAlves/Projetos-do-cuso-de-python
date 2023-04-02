# variáveis que irão armazenar a soma das idades e o nome do homem mais velho
soma_idades = 0
nome_homem_mais_velho = ""
idade_homem_mais_velho = 0
# variável que irá contar o número de mulheres com menos de 21 anos
mulheres_menos_de_21 = 0
for i in range(4): # Loop para ler as informações das 4 pessoas
    # Lê o nome, idade e sexo da pessoa
    nome = input("Digite o nome da {}ª pessoa: ".format(i+1))
    idade = int(input("Digite a idade da {}ª pessoa: ".format(i+1)))
    print ('[1] Masculino')
    print ('[2] Feminino')
    sexo = input("Gênero da {}ª pessoa: ".format(i+1)) 
    # Adiciona a idade da pessoa à soma das idades
    soma_idades += idade
    # Verifica se a pessoa é um homem e se é o mais velho até agora
    if sexo == "1" and idade > idade_homem_mais_velho:
        nome_homem_mais_velho = nome
        idade_homem_mais_velho = idade
    # Verifica se a pessoa é uma mulher com menos de 21 anos
    if sexo == "2" and idade < 21:
        mulheres_menos_de_21 += 1
# Calcula a média de idade do grupo
media_idades = soma_idades / 4
# Exibe os resultados
print("Média de idade do grupo: {:.0f}".format(media_idades))
print("Nome do homem mais velho: {}".format(nome_homem_mais_velho))
print("Quantidade de mulheres com menos de 21 anos: {}".format(mulheres_menos_de_21))
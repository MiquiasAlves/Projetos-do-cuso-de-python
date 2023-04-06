# Solicita o nome do usuário
nome = str(input('Digite seu nome: '))
# Solicita o gênero do usuário, removendo espaços em branco e convertendo para letras maiúsculas
genero = str(input('informe seu gênero [Masculino, Feminino]: ')).strip().upper()
# Solicita a idade do usuário
idade = int(input('informe sua idade: '))
# Enquanto o gênero informado não for 'FEMININO' ou 'MASCULINO', solicita novamente o gênero
while genero not in 'FEMININO, MASCULINO':
    genero = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
# Exibe o nome, gênero e idade do usuário na tela
print(f'{nome}, seu gênero({genero}) e idade({idade} anos) foi registrado com sucesso.')

print('-' * 25)
print('CADASTRE UMA PESSOA')
print('-' * 25)
# Inicializa as variáveis que serão utilizadas para contar o número de pessoas cadastradas
tot18 = totH = totM = totM20 = 0
# Inicia um loop para cadastrar as pessoas
while True: 
    idade = int(input('Idade: '))  # Solicita a idade da pessoa
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]  # Solicita o sexo da pessoa

    if idade >= 18:
        tot18 += 1  # contador de pessoas com mais de 18 anos

    if sexo == 'M':
        totH += 1  # contador de homens cadastrados

    if sexo == 'F' and idade < 20: 
        totM20 += 1  # contador de mulheres com menos de 20 anos cadastradas

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]  # Pergunta se o usuário quer cadastrar outra pessoa

    if resp == 'N':
        break  # Sai do loop se o usuário não quiser cadastrar mais pessoas

# informações sobre as pessoas cadastradas
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'O total de mulheres com menos de 20 anos é {totM20}.')

from datetime import date
atual = date.today().year # Obtém o ano atual do sistema
name = str(input('Digite seu nome: '))
nascimento = int(input(f'{name}, Qual seu ano de nascimento: ')) # Solicita ao usuário o ano de nascimento
idade = atual - nascimento # calcula a idade do atleta
print('O atleta em {}anos.'.format(idade)) # Exibe a idade do atleta
# Verifica a categoria de acordo com a idade
if idade <= 9:
    print('Classificação: Mirim')
elif idade <= 14:
    print('Classificação: infantil')
elif idade <= 19:
    print('Clasificação: junior')
elif idade <= 25:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')
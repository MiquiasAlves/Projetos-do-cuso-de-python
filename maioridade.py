from datetime import date
ano_atual = date.today().year # Obtém o ano atual a partir do módulo date da biblioteca datetime
# variáveis maiores e menores com zero
maiores = 0
menores = 0
# Loop que pede o ano de nascimento de sete pessoas
for i in range(1, 8):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {i}ª pessoa: '))
    idade = ano_atual - ano_nascimento   # Calcula a idade da pessoa subtraindo o ano de nascimento do ano atual
     # Verifica se a pessoa é maior ou menor de idade e incrementa a variável correspondente
    if idade >= 21:
        maiores += 1 # contar o número de vezes
    else:
        menores += 1 # contar o número de vezes
print(f'Das 7 pessoas, {maiores} já atingiram a maioridade e {menores} ainda não.')
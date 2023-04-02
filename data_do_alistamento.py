from datetime import date
from time import sleep
nome = str(input('Qual é seu nome? ')) # Solicita o nome do usuário
print(f'Prazer, {nome}! Eu sou o atendente virtual do Exército!') # mensagem de boas-vindas
nasc = int(input(f'{nome}, agora preciso saber seu ano de nascimento? ')) # Solicita o ano de nascimento do usuário
ano_atual = date.today().year # Obtém o ano atual
idade = ano_atual - nasc # Calcula a idade do usuário
print('Obrigado pela informções!') # mensagem de agradecimento
print('Aguarde mais uns instantes, estou salvando suas informações no nosso banco de dados!') # mensagem de processamento
print('Processando...') # Pausa o programa
sleep(3)
print('Quem nasceu em {} tem {} anos no ano de {}'.format(nasc, idade, ano_atual))
# Verifica se o usuário precisa se alistar
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    print('Seu alistamento será em {}'.format(ano_atual + saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano_atual - saldo))
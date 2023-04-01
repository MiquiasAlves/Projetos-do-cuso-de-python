valor_casa = float(input('Digite o valor da casa desejada: R$ ')) # valor da casa desejada como um número decimal
salario = float(input('Digite o valor so seu salário em : R$ ')) # valor do salário do usuário como um número decimal
parcelamento = int(input('Digite a quantidade de parcelas 12x, 24x, 36x, 48x, 60x, 72x, 84x, 96x, 108x, 120x... : ')) # solicita o número de parcelas para o financiamento como um número inteiro
valor_mensal = valor_casa / parcelamento # valor mensal do financiamento dividindo o 'valor_casa' pelo 'parcelamento'
if valor_mensal > (salario * (30/100)): # verifica se o valor mensal do financiamento é superior a 30% do salário do usuário
    print('-----' * 20)
    print('Não foi dessa vez, seu empréstimo foi negado!') # mensagem informando que o empréstimo foi negado
    print('Vamos analisar novamente seus dados daqui a 6 mês!')
    print('Para mais informações vá até uma de nossas unidades mais próxima de você!')
    print('-----' * 20)
else:
    print('-----' * 20)
    print('Parabéns, o valor do financiamento foi aprovado!') # mensagem informando que o empréstimo foi aprovado
    print('O valor mensal a ser pago R${:.2f} em {} mês, equivale a {:.0f} anos!'.format(valor_mensal, parcelamento, parcelamento/12)) # mensagem informando o valor mensal a ser pago, o número de parcelas e a duração do financiamento em anos
    print('-----' * 20)
    print('-----' * 20)
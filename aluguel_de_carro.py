print('----' * 5)
print('Vamos calcular o valor do aluguel do carro')
print('----' * 5)
# solicita ao usuário o número de dias que o carro foi alugado e a distância percorrida em km
dias_alugados = int(input('Digite quantos dias passou com carro: ')) 
km_rodados = float(input('Quantos KM rodados: '))
# calcula o valor total do aluguel com base nos dias alugados e km rodados
valor_dia = int(dias_alugados * 120)
valor_km = float(km_rodados * 10)
# valor total a pagar, que é a soma do valor do aluguel por dia e do valor do aluguel por km
print('O valor por dia custou {}, valor por KM foi {} e o valor total a pagar será: {}'.format(valor_dia, valor_km, valor_dia + valor_km))
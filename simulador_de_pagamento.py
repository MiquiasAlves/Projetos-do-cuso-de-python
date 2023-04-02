preço = float(input('Qual o valor da compra R$? '))
# Menu de opções de pagamento
print('[1] Dinheiro/Pix')
print('[2] Cartão debito/credito à vista')
print('[3] Cartão em 2x')
print('[4] Cartão em até 12x com juros')
opçao = int(input('Escolha uma das opções: '))
if opçao == 1: # Desconto para pagamento em dinheiro/Pix
    print('O valor do compra com 10%, de desconto, vai custar R${:.2f}'.format(preço - (preço * (10/100))))
elif opçao == 2: # Desconto para pagamento em cartão de débito/crédito à vista
    print('O valor do compra com 5%, de desconto, vai custar R${:.2f}'.format(preço - (preço * (5/100))))
elif opçao == 3: # Parcelamento em 2x sem juros
    print(f'O valor com preço normal {preço:.2f}, parcelado em 2x')
elif opçao == 4: # Parcelamento em até 12x com juros
    parcelamento = int(input('Em quantas vezes quer parcelar? '))
    juros = ((preço * (1/100)) * parcelamento) + preço
    print('O preço para {} parcelas, fica no valor do {:.2f}'.format(parcelamento, juros))
else: # Opção inválida de pagamento
    print('OPÇÂO INVÁLIDA de pagamento. Tente novamente!')
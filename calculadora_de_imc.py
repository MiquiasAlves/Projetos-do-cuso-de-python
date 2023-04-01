print('----'*10)
print('Decubra se seu pesoa é ideal')
print('----'*10)
nome = str(input('Digite seu nome: ')) #nome do usúario
peso = float(input(f'{nome}, agora me informe qual seu peso? (Kg) ')) #peso do usúario
altura = float(input('Altura em (m)? ')) #altura do usúario em M
imc = peso / (altura ** 2) #cálculo para chegar no indice de massa corporal (IMC)
print(f'O imc dessa pessoa é de {imc}.')
if imc < 16:
    print('Subpeso Severo, procure um de nossos especialista')
elif imc <= 19.9 and imc >= 16:
    print('Subpeso, procure um de nossos especialista')
elif imc <= 24.9 and imc >= 20:
    print('Normal, parábens')
elif imc <= 29.9 and imc >= 25:
    print('Sobrepeso, procure um de nossos especialista')
elif imc <= 39.9 and imc >= 30:
    print('Obeso, procure um de nossos especialista')
else:
    print('Obeso mórbito, procure um de nossos especialista')
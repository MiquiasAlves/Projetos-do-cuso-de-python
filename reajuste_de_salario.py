print('------' * 4)
print('Vamos ver qual o reajuste do seu sálario')
print('------' * 4)
salario = float(input('Qual o valor de seu salário? ')) # solicita o valor do salário do usuário
if salario <= 1.250:
    print('Seu salário teve um reajuste de 10%, vai passar a ser: R${:.2f}'.format(salario * (10/100) + salario))
else:
    print('Seu salário teve um aumento de 15%, vai passar a ser: R${:.2f}'.format(salario * (15/100) + salario))
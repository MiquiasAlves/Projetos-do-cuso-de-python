from time import sleep
# Solicitando as notas ao usuário
nota1 = float(input('Digite a sua nota em atividades: '))
nota2 = float(input('Digite a sua nota no trabalho: '))
nota3 = float(input('Digite a sua nota no simulado: '))
nota4 = float(input('Digite a sua nota em avaliação: '))
m = (nota1 + nota2 + nota3 + nota4) / 4 #Calculando a média
print('Obrigado pelas informações!')
print('Aguarde um instante...')
sleep(3) 
# Verificando se o aluno foi aprovado, ficou de recuperação ou foi reprovado
if m >= 7:
    print('Sua média foi {:.1f}, Parabéns! Você foi aprovado!'.format(m))
    print('Boas férias!')
elif m >= 5.0 and m <= 6.9:
    print('Sua média foi {:.1f}, infelizmente você ficou de recuperação!'.format(m))
    print('Estude mais!')
else:
    print('Você foi reprovado! Sua média foi {:.1f}'.format(m))

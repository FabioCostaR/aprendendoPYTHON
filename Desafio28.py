# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5
# Peça para o usuario descobrir qual foi o numero escolhido pelo computador.
# Deve escrever se venceu ou errou.
import random
num = random.randint (0,5)
num1 = int(input('Escolha um numero entre 0 e 5 : '))
if num==num1:
    print("VOCE ACERTOU !!!")
else:
    print("VOCÊ ERROU !!!")
print(' *** FIM DE JOGO ***')
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
al1 = str(input('Entre com o nome do aluno 1 :'))
al2 = str(input( 'Entre com o nome do aluno 2 :'))
al3 = str(input('Entre com o nome do aluno 3 :'))
al4 = str(input('Entre com o nome do aluno 4 :'))
lista = [al1,al2,al3,al4]
random.shuffle(lista) #random.shuffle embaralha a lista.
print(lista)
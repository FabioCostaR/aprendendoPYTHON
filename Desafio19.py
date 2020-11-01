#Um professor quer sortear um dos seus quatro alunos para apagar o quadro
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo o nome do escolhido.
import random
nome1 = input("Entre com o nome 1 ")
nome2 = input('Entre com o nome 2 ')
nome3 = input('Entre com o nome 3 ')
nome4 = input('Entre com o nome 4 ')
lista = [nome1,nome2,nome3,nome4]

escolhido = random.choice(lista)
print(f'O escolhido foi o {escolhido}')
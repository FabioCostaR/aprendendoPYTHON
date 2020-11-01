#Crie um programa que leia o nome completo de uma pessoa e mostre
# 1) O nome com todas letras maiusculas
# 2) O nome com todas letras minisculas
# 3) Quantas letras tem ao sem espaço contar
# 4) Quantas letras tem o primeiro nome

nome = str(input("Qual é seu nome completo ? \n")).strip()
# 1
nome1 = nome.upper()
# 2
nome2 = nome.lower()
# 3)Vamos contar todas as letras e retirar os espaços
# Contar todas as letras do nome:
nome3 = len(nome)-nome.count(' ')
# 4) Fatia e conta a lista 0 ( primeira lista)

nome4a = nome.split()
nome4 = len(nome4a[0])


#Exibe os resultados
print (nome1)
print (nome2)
print(nome3)
print(nome4)
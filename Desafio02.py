#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas vindas
nome = str(input("Qual é seu nome ?\n"))
print ('Olá {}{}{},\nSeja Bem Vindo'.format('\033[1;36m',nome,'\033[m'))
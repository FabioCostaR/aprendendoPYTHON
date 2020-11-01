#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input("Entre com o seu nome: \n")).strip()
nome = nome.upper()
nom = nome.split()
print('Seu nome tem Silva?')
print ('SILVA' in nom)

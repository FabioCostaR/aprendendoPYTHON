#024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
nome = str(input(' Entre com o nome da cidade:\n ')).strip()
nome = nome.upper()
cidade = nome.split()
print(cidade[0]=='SANTO')
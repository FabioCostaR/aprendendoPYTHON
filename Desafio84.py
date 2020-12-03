#Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em
#uma lista. No final mostre:
#Quantas pessoas foram cadastradas.
#Uma lista das pessoas mais pesadas.
#Uma lista das pessoas mais leves.
dados=[]
lista=[]
maior=menor=0
while True:
    dados.append(input('NOME: '))
    dados.append(float(input('PESO(kg): ')))
    if len(lista)==0:
        maior=dados[1]
        menor=dados[1]
    else:
        if dados[1]>maior:
            maior=dados[1]
        if dados[1]<menor:
            menor=dados[1]
    lista.append(dados[:])
    dados.clear()
    escolha=str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if escolha not in 'SN':
        escolha = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    if escolha in 'N':
        break

print('=***'*20)
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'O maior peso foi de {maior} kg e as pessoas com esse peso foram: ',end=' ')
for p in lista:
    if p[1]==maior:
        print(f'{p[0]}', end=' ')
print(f'\n O menor peso foi de {menor} kg e as pessoas com esse peso foram: ',end=' ')
for p in lista:
    if p[1]==menor:
        print(f'{p[0]}', end=' ')
print('=***'*20)
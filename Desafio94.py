#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
#os dados em um dicionário, e todos os dicionários em uma lista. No final mostre:
#Quantas pessoas foram cadastradas.
#A média de idade do grupo.
#Uma lista com todas as mulheres.
#Uma lista com todas as pessoas com idade acima da média.
arquivo={}
soma=0
dados=[]
while True:
    arquivo.clear()
    nome= str(input('Nome: ')).strip()
    sexo=str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    idade= int(input('Idade: '))
    soma=soma+idade
    arquivo['Nome']=nome
    arquivo['Sexo']=sexo
    arquivo['Idade']=idade
    dados.append(arquivo.copy())
    escolha=str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if escolha not in 'SN':
        escolha = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if escolha in 'N':
        break
print('==='*15)
print(f'Ao todo temos {len(dados)} pessoas cadastradas.')
print('==='*15)
print(f'A media de idade é {soma/len(dados):5.2f} anos')
print('==='*15)
print(f'As mulheres cadastradas foram: ',end=' ')
for p in dados:
    if p['Sexo']=='F':
        print(p["Nome"], end=' ')
print()
print('==='*15)
print('Pessoas com idade acima da média: ',end=', ')
for p in dados:
    if p['Idade']>soma/len(dados):
        print(p["Nome"], end=', ')
print('==='*15)
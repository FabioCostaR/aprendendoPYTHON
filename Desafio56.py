#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final, mostre:
#A media de idade do grupo.
#Qual é o nome do homem mais velho.
#Quantas mulheres tem menos de 20 anos
somaidade=0
maioridadehomem=0
nomevelho=''
cont=0
for c in range(0,4):
    print(f'--------- {c+1}° PESSOA  --------')
    nome=str(input('NOME: ')).strip().upper()
    idade=int(input('IDADE: '))
    sexo=str(input('SEXO [M/F]: ')).strip()
    somaidade+=idade
    if sexo in 'Mm':
        if idade>maioridadehomem:
            maioridadehomem=idade
            nomevelho=nome
    if sexo in 'Ff':
        if idade<20:
            cont+=1
mediaidade=somaidade/4
print(f' A media de idade do grupo é {mediaidade}')
print(f' O homem mais velho da lista, chama-se {nomevelho}, e ele tem {maioridadehomem} anos')
print(f' {cont} mulheres tem menos de 20 anos')
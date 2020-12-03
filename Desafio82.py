#Crie um programa que vai ler vários números e colocar em uma lista
#Depois disso crie duas listas extras que vão conter apenas valores pares e impares
#digitados, respectivamente.
#No final, mostre o conteudo das três listas geradas.
lista=[]
pares=[]
impares=[]
while True:
    num=int(input('Entre com o valor: '))
    lista.append(num)
    opc=str(input('Deseja Continuar? [S/N]:')).strip().upper()[0]
    if opc not in 'SN':
        opc = str(input('Deseja Continuar? [S/N]:')).strip().upper()[0]
    if opc=='N':
        break
for c in range (0,len(lista)):
    if lista[c]%2==0:
        pares.append(lista[c])
    else:
        impares.append(lista[c])
print(f'Lista digitada: {lista}')
print(f'Lista de pares: {pares}')
print(f'Lista de impares: {impares}')

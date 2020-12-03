#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
#Quantos numeros foram digitados.
#A lista de valores ordenados de forma decrescente.
#Se o valor 5 foi digitado e está ou não está na lista.
c=0
lista=[]
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    c+=1
    opcao=str(input('Deseja continuar:[S/N] ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar:[S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'Foram digitados {c} numeros')
lista.sort(reverse=True)
print(lista)

if 5 in lista:
    print(f' O numero cinco foi digitado e está na posição {lista.index(5)+1}')
else:
    print('O numero cinco NÃO foi encontrado.')
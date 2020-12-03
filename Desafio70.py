#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuario vai continuar. No final mostre:
#Qual é o total gasto na compra
#Quantos produtos custam mais de R$1000.00
#Qual é o nome do produto mais barato.
total=barato=totmil=cont=0
bizu=''
print('_'*30)
print('    LOJAS SUPER DESCONTO  ')
print('-'*30)
while True:
    prod = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$ '))
    cont+=1
    escolha = str(input('Quer continuar ? [+/=] ')).strip().upper()[0]
    while escolha not in '+=':
        escolha = str(input('Quer continuar ? [+/=] ')).strip().upper()[0]
    total += preco
    if cont==1 or preco<barato:
        barato=preco
        bizu=prod
    if preco > 1000:
            totmil += 1
    if escolha=='=':
        break


print(f'Total: R${total:.2f}')
print(f'{totmil} produtos custam mais de R$1000.00')
print(f'O produto: {bizu} foi o mais barato custa R${barato:.2f}')




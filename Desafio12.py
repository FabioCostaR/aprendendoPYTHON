#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

n = float(input(' Qual é o valor do produto? '))
n1 = float(input(' Qual é a porcentagem de desconto?'))
desconto = (n1 * n)/100
print(f' O produto custa R${n:.2f}, com um desconto de {n1:.2f}%, ele sairá por R${n-desconto:.2f} ')
print(f' Valor do produto R${n:.2f}'
      f' Valor do desconto R${desconto:.2f}'
      f' Valor final do produto R${n-desconto:.2f}')

#Faça um programa que leia 5 valores numericos e guarde-os em uma lista.
#No final mostre qual foi o maior e o menor valor digitado e suas respectivas posições 
#Na lista.
maior=menor=0
valores = list()
for c in range (0,5):
    valores.append(int(input('Entre com o valor: ')))
    if c==0 or valores[c]>maior:
        maior=valores[c]
    if c==0 or valores[c]<menor:
        menor=valores[c]
print('=-'*20)
print(f'A lista digitada foi {valores}')
print(f'O maior numero digitado foi {maior} e está na posição {valores.index(maior)+1}')
print(f'O menor numero digitado foi {menor} e está na posição {valores.index(menor)+1}')
print('=-'*20)

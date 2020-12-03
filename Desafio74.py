#Crie um programa que vai gerar cinco numeros aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique qual é o numero maior
#E menor da tupla.
from random import randint
tupla=(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))
maior=menor=tupla[0]
c=0
print(f'A tupla aleatória é :{tupla}')
for c in range (0,5):
    if maior<tupla[c]:
        maior=tupla[c]
    if menor>tupla[c]:
        menor=tupla[c]

print(f'O maior elemento da tupla é {maior}')
print(f'O menor elemento da tupla é {menor}')


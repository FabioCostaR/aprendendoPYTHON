#Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = (100**100)


for c in range(0,5):
    peso = float(input('Digite o peso :'))
    if peso>maior:
        maior = peso
    elif peso<menor:
        menor = peso
print(f'O maior peso digitado foi {maior} kg\n'
      f'e o menor peso digitado foi {menor} kg')

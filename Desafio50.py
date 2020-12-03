#Faça um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares
#Se o numero digitado for impar, desconsidere-o
soma=0
for cont in range(0,6):
    nume = int(input('digite o numero: '))

    if nume%2==0:
        soma = soma + nume
print(f'A soma de todos os numeros pares digitados é {soma}')
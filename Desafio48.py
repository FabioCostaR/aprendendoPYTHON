#Faça um programa que calcule a soma entre todos os numeros impares que
#são multiplos de três e se encontram no intervalo de 1 ate 500
soma=0
for c in range(0,20):
    if c%2!=0:
        if c%3==0:
            soma=soma+c
print(soma)
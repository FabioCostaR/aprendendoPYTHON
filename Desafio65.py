#Crie um programa que leia vários numeros inteiros pelo teclado. No final da execução, mostre
# a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar
# ao usuário se ele quer continuar ou não continuar a digitar valores.

resp = 'S'
c=1
soma = maior = menor =0

while resp=='S':
    nume = int(input('Digite um numero inteiro :'))
    soma=soma+nume
    media = soma/c
    if nume>maior:
        maior=nume
    if c==1:
        menor=nume
    else:
        if nume<menor:
            menor=nume
    c+=1
    resp = str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]



print(f'Foram digitados {c-1} numeros inteiros \n'
      f'* A soma dos numeros digitados é {soma} \n'
      f'** A média aritmetica é {media} \n'
      f'*** O maior numero digitado foi o {maior} \n'
      f'**** O menor numero digitado foi o {menor}')


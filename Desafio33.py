#Faça um programa que leia três numeros e mostre qual deles é o maior e qual é o menor.
print("***Entre com tres valores numericos distintos***")
num1 = int(input('Entre com o primeiro numero :'))
num2 = int(input('Entre com o segundo numero :'))
num3 = int(input('Entre com o terceiro numero :'))
if (num1>num2) and (num1>num3) and (num2>num3):
    print(f'{num1} é o maior numero digitado')
    print(f'E {num3} é o menor numero digitado')
if (num1>num2) and (num1>num3) and (num2<num3):
    print(f'{num1} é o maior numero digitado')
    print(f'E {num2} é o menor numero digitado')
if (num2>num1) and (num2>num3) and (num1>num3):
    print(f'{num2} é o maior numero digitado')
    print(f'E {num3} é o menor numero digitado')
if (num2>num1) and (num2>num3) and (num1<num3):
    print(f'{num2} é o maior numero digitado')
    print(f'E {num1} é o menor numero digitado')
if (num3>num1) and (num3>num2) and (num1>num2):
    print(f'{num3} é o maior numero digitado')
    print(f'E {num2} é o menor numero digitado')
if (num3>num1) and (num3>num2) and (num2>num1):
    print(f'{num3} é o maior  numero digitado')
    print(f'E {num1} é o menor numero digitado')
if(num1==num2) or (num2==num3) or (num1==num3):
    print('Numeros iguais não são permitidos')
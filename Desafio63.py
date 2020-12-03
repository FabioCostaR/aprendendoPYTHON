#Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros termos
#de uma sequencia de Fibonacci
print('=*'*30)
print('SEQUENCIA DE FIBONACCI')
print('=*'*30)
n = int(input('Quantos termos você deseja? '))
c=3
t1=0
t2=1
print(f'{t2} ► ', end='')
while c<=n+1:
    t3=t2+t1
    t1= t2
    t2=t3
    print(f'{t3}', end='')
    print(' ► ' if c<n+1 else'', end='')
    c+=1


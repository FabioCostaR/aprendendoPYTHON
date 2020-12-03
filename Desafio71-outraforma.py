#Crie um programa que simule o funcionamento de um Caixa Eletronico.
#No inicio pergunte qual valor será sacado (INTEIRO)
#Programa vai informar quantas cédulas serão entregues de cada valor.
#Considere as cédulas de 50, 20, 10, e 1.

print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor=int(input('Que valor você quer sacar? R$'))
ced = 50
total=valor
totalced = 0
while True:
    if total>= ced:
        total -=ced
        totalced +=1
    else:
        if totalced>0:
         print(f'Total de {totalced} cédulas de R$ {ced}')
        if ced==50:
            ced =20
        elif ced ==20:
            ced = 10
        elif ced==10:
            ced=1
        totalced =0
        if total ==0:
            break

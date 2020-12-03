#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá se o usuário quer ou não continuar.
#No final mostre:
#Quantas pessoas tem mais de 18 anos
#Quantos homens foram cadastrados.
#Quantas mulheres tem menos de 20 anos
c=s=h=m=0
while True:
    print ('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int ( input('Idade: '))
    sexo = str(input('Sexo: [M\F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M\F] ')).strip().upper()[0]
    print('-'*20)
    escolha = str(input(' Deseja Continuar ? [S/N]: ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input(' Deseja Continuar ? [S/N]: ')).strip().upper()[0]
    c+=1
    if escolha=='N':
        break
    if idade>18:
        s+=1
    if sexo=='M':
        h+=1
    if sexo=='F'and idade<20:
        m+=1
print(f'FORAM CADASTRADOS: \n'
      f'{c} pessoas. \n'
      f'{s} pessoas com mais de 18 anos \n'
      f'{h} homens foram cadastrados \n'
      f'{m} mulheres com menos de 20 anos foram cadastradas ')
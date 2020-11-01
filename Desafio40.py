#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem final de acordo
#com a média atingida:
#Media abaixo de 5.0: Reprovado
#Media entre 5.0 e 6.9 Recuperação
#Media 7.0 ou superior APROVADO

nota1 = float(input(' Entre com a primeira nota do aluno: '))
if nota1<=10:
    nota1==nota1
elif nota1>10 and nota1<=100:
    nota1= nota1/10
elif nota1>100:
    print('Nota invalida')
    quit()
nota2 = float(input(' Entre com a segunda nota do aluno: '))
if nota2<=10:
    nota2==nota2
elif nota2>10 and nota2<=100:
    nota2= nota2/10
elif nota2>100:
    print('Nota invalida')
    quit()
media = (nota1+nota2)/2
print(f'Media = {media}')
if media<5:
    print ('Você está \033[01;31m REPROVADO')
elif media>=5 and media<7:
    print ('Você está em \033[01;33m RECUPERAÇÃO')
else:
    print('Você está \033[01;36m APROVADO')
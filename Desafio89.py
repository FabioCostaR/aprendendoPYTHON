#Crie um programa que leia o nome e duas notas de vários alunos e guarde
#tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e
# permita que o usuário possa mostrar as notas de cada aluno individualmente.

#dados=[nome, nota1, nota2]
#arquivos=[dados, dados, dados,...]
dados=[]
arquivo=list()
while True:
    nome=str(input('NOME: ')).strip().upper()
    nota1=float(input('Nota01: '))
    nota2=float(input('Nota02: '))
    media=(nota1+nota2)/2
    dados=[nome,nota1,nota2,media]
    arquivo.append(dados[:])
    dados.clear()
    op=str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if op not in 'SN':
        op = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if op in 'N':
        break
print('-='*20)
print(f' \033[01;32m {"NOME": <4}                  {"MÉDIA":>10} \033[m   ')

for i in range(0,len(arquivo)):
    print(f' {arquivo[i][0]:<10}              {arquivo[i][3]:>8.1f}')
print('-='*20)
while True:
    aluno=str(input('Mostrar as notas de qual aluno? (999 interrompe): ')).strip().upper()
    for c in range(0,len(arquivo)):
        if aluno==arquivo[c][0]:
            print(f'As notas do aluno {arquivo[c][0]} foram: {arquivo[c][1]} e {arquivo[c][2]}')
    print('-=' * 20)
    if aluno in '999':
        break
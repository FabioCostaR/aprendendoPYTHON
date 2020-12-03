#Faça um programa que leia o nome e a media de um aluno.
#guardando também a situação (aprovado ou reprovado) em um dicionário.
#No final mostre o conteúdo da estrutura na tela.

dados={}
dados['Nome']=str(input('Nome: ')).strip()
dados['Media']=float(input(f'Média de {dados["Nome"]}: '))
if dados['Media']>70:
    dados['Situacao']='Aprovado.'
else:
    dados['Situacao']='Reprovado.'
for k, v in dados.items():
    print(f'{k} é igual a {v}.')

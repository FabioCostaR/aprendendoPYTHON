#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
#cadastre-os(com idade) em um dicionário se por acaso a CTPS for diferente
# de zero, o dicionário receberá também o ano de contratação e o salário. Calcule
# e acrescente, além da idade, com quantos anos vai se aposentar.
from datetime import datetime
dados={}
dados['Nome']=str(input('NOME: ')).strip()
dados['Nasc']=int(input('Ano de nascimento: ' ))
dados['Idade'] =(datetime.now().year) - dados['Nasc']
dados['CTPS']=int(input('Carteira de Trabalho: (0 não tem): '))
if dados['CTPS']!=0:
    dados['Contratacao']=int(input('Ano de Contratação: '))
    dados['Salário']=float(input('Salário: '))
    dados['Aposentadoria'] = (35-((datetime.now().year)-dados['Contratacao']))+dados['Idade']
elif dados['CTPS']==0:
    dados['Aposentadoria']=dados['Idade']+35
print('=--='*10)
print('-='*5,'RELATÓRIO','-='*5)
print('=--='*10)
print(f'{dados["Nome"]}, nasceu em {dados["Nasc"]} e tem {dados["Idade"]}anos,')
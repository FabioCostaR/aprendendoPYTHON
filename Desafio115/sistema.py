from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    #print('Arquivo Existe')
    print()
else:
    print('Arquivo NÃO Existe')
    criarArquivo(arq)

while True:
    resposta = menu(['Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Sistema'])

    if resposta == 1:
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 2:
        #Opção de listar o conteudo do arquivo!
        lerArquivo(arq)

    elif resposta == 3:
        sleep(2.3)
        break
    else:
        print('ERRO !!!'
              'Digite uma opção válida!!!')
    sleep(2)

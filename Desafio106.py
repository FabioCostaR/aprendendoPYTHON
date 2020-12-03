#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar
#o comando e o manual vai aparecer.
#Quando o usuario digitar a palavra 'FIM' o programa encerrará.
#USE CORES.
def ajuda(msg):
    from time import sleep
    while True:
        tela=str('Sistema de Ajuda do PYTHON')
        print('\033[30;42m')
        print('~' *(len(tela)+4))
        print(f'  {tela}')
        print('~'*(len(tela)+4))
        print('\033[m')
        msg=str(input('Função ou Biblioteca (para encerrar FIM)-> ')).strip().lower()
        tela2=str(f'ACESSANDO O MANUAL DO COMANDO {msg}')
        sleep(1.5)
        print('\033[30;44m')
        print('.' * (len(tela2) + 4))
        print(f'  {tela2}')
        print('~' * (len(tela2) + 4))
        print('\033[m')
        help(msg)
        if msg=='fim':
            print('Até Logo.')
            break
print(ajuda('msg'))
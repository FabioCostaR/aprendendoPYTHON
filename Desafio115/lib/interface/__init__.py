def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31m ERRO !!!  \n Por Favor, digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário')
        else:
            return n


def linha(tam=30):
    return '~' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())


def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc

# Crie um módulo chamado moeda.py que tenha as funçoes incorporadas
# aumentar(),diminuir(),dobro() e metade().
# Faça também um programa que importe esse modulo e use alguas dessas funções.

# #Adapte o codigo do desafio107, criando uma funçao adicional chamada
# moeda() que consiga mostrar os valores com um valor monetário formatado

# Modifique as funções que foram criadas no desafio107 para que elas
# aceitem um parametro a mais, informando se o valor retornado por elas vai ser
# ou não ser formatado pela função moeda() desenvolvida no desafio 108

#Adicione ao modulo da moeda.py criado nos desafios anteriores,
#uma função chamada resumo(), que mostre na tela algumas informações
#geradas pelas funções que já temos no modulo criado até aqui



def aumentar(v=0, p=0, formato=False):
    """
    Função que aumenta um certo porcentual de um valor dado
    :param formato: Em formato moeda True or False
    :param v: valor de entrada
    :param p: porcentual de aumento desejado
    :return: valor +aumento
    """
    subir = v * (p / 100)
    novo = v + subir
    return novo if formato is False else moeda(novo)


def diminuir(valor=0, perc=0, formato=False):
    """
        Função que diminui um certo porcentual de um valor dado
        :param formato: Em formato moeda True or False
        :param valor : valor de entrada
        :param perc : porcentual de decrescimo desejado
        :return: valor - decrescimo
    """
    queda = (perc / 100) * valor
    novo = valor - queda
    return novo if formato is False else moeda(novo)


def dobro(valor=0, formato=False):
    """
    Função que calcula o dobro de um valor
    :param formato: Em formato moeda True or False
    :param valor: valor de entrada
    :return: 2 * valor de entrada
    """
    novo = valor * 2
    return novo if formato is False else moeda(novo)


def metade(valor=0, formato=False):
    """
    Função que calcula a metade do valor
    :param formato: Em formato moeda True or False
    :param valor: valor de entrada
    :return: entrada / 2
    """
    novo = valor / 2
    return novo if formato is False else moeda(novo)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(valor=0,acres=0,decr=0,formato=False):
    frase=str('RESUMO DO VALOR')
    print('-'*(len(frase)+4))
    print(f'  {frase}')
    print('-' * (len(frase) + 4))
    print(f'Preço analisado: \t\t\t{moeda(valor)}')
    print(f'Dobro do preço: \t\t\t{dobro(valor,formato)}')
    print(f'Metade do preço: \t\t\t{metade(valor,formato)}')
    print(f'Com {acres}% de aumento: \t\t{ aumentar(valor,acres,formato)}')
    print(f'Com {decr}% de desconto: \t\t{diminuir(valor,decr,formato)}')
    print('-' * (len(frase) + 4))
print('')
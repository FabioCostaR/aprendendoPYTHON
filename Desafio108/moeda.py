# Crie um módulo chamado moeda.py que tenha as funçoes incorporadas
# aumentar(),diminuir(),dobro() e metade().
# Faça também um programa que importe esse modulo e use alguas dessas funções.

# #Adapte o codigo do desafio107, criando uma funçao adicional chamada
# moeda() que consiga mostrar os valores com um valor monetário formatado
def aumentar(v=0, p=0):
    """
    Função que aumenta um certo porcentual de um valor dado
    :param v: valor de entrada
    :param p: porcentual de aumento desejado
    :return: valor +aumento
    """
    subir = v * (p / 100)
    novo = v + subir
    return novo


def diminuir(valor=0, perc=0):
    """
        Função que diminui um certo porcentual de um valor dado
        :param valor : valor de entrada
        :param perc : porcentual de decrescimo desejado
        :return: valor - decrescimo
    """
    queda = (perc / 100) * valor
    novo = valor - queda
    return novo


def dobro(valor=0):
    """
    Função que calcula o dobro de um valor
    :param valor: valor de entrada
    :return: 2 * valor de entrada
    """
    novo = valor * 2
    return novo


def metade(valor=0):
    """
    Função que calcula a metade do valor
    :param valor: valor de entrada
    :return: entrada / 2
    """
    novo = valor / 2
    return novo


def moeda(valor=0,moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')



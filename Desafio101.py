# Crie um programa que tenha uma função chamada voto() que vai receber como parametro
# o ano de nascimento de uma pessoa, retornado um valor literal indicando se uma pessoa
# tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
def voto(ano):
    """
    -> Faz o calculo da situação de voto
    :param ano: entrada do usuário, (ano de nascimento)
    :return: situação de voto, classificado em: Opcional, Obrigatório ou Negado
    """
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade < 15:
        print(f'Você tem {idade} anos, seu direito ao voto é NEGADO')
    elif 15 <= idade < 18:
        print(f'Você tem {idade} anos, seu direito ao voto é OPCIONAL')
    elif idade > 65:
        print(f'Você tem {idade} anos, seu direito ao voto é OPCIONAL')
    elif 18 <= idade <= 65:
        print(f'Você tem {idade} anos, seu direito ao voto é OBRIGATÓRIO')


idade = int(input('Em que ano você nasceu? '))
voto(idade)

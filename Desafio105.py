# Faça um programa que tenha uma função notas() que pode receber várias notas de
# alunos e vai retornar um dicionário com as seguintes informações:
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação(opcional)
# Adicione também docstrings da função.
def notas(*n, sit=True):
    """
    Função para analisar notas de um aluno
    :param n: uma ou mais notas
    :param sit: Reprovado, Recuperação, Aprovado.
    :return: dicionário com a informação do aluno
    """
    r = {}
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['total'] = len(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['sit'] = 'Aprovado'
        elif 4 <= r['media'] < 7:
            r['sit'] = 'Recuperação'
        elif r['media'] < 4:
            r['sit'] = 'Reprovado'
    return r


resp = notas(4, 5, 3, 2, sit=True)
help(notas)
print(resp)

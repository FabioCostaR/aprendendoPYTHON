# Faça um programa que tenha uma função chamada ficha(), que receba dois parametros
# opcionais: o nome de um jogador e quantos gols ele marcou
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha
# sido informado corretamente.

def ficha(nome='desconhecido', gols=0):
    print(f'O jogador {nome}, marcou {gols} gols na temporada.')


apelido = str(input('Qual o nome do jogador: '))
gols = str(input('Quantos gols ele marcou na temporada? '))
if len(apelido) == 0:
    nome = '<desconhecido>'
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

ficha(apelido, gols)

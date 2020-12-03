# Aprimore o desafio 093 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai
# ler a quantidade de gols feitos em cada partida. No final, tudo isso será, guar
# Dado em um dicionário, incluindo o total de gols feitos durante o campeonato
jogador = {}
gols = []
dados = []
while True:
    total = 0
    gols.clear()
    jogador['nome'] = str(input('Nome: ')).upper().strip()
    partidas = int(input(f'N° de Partidas que {jogador["nome"]} jogou:  '))
    for c in range(0, partidas):
        GOL = int(input(f'N° de gols feitos na partida {c + 1} que {jogador["nome"]} participou: '))
        gols.append(GOL)
        total = total + GOL
    jogador['gols'] = gols[:]
    jogador['total de gols'] = total
    jogador['media'] = total / len(gols)
    dados.append(jogador.copy())
    choise = str(input('Deseja Continuar[S/N]? ')).upper().strip()[0]
    if choise not in 'SN':
        choise = str(input('Deseja Continuar[S/N]? ')).upper().strip()[0]
    if choise in 'N':
        break

craque = str(input('Qual jogador você deseja detalhar? ')).strip().upper()
for c in range(0, len(dados)):
    if dados[c]['nome'] == craque:
        print(
            f'O jogador {dados[c]["nome"]} fez em {len(dados[c])} partidas, {dados[c]["total de gols"]} gols, ficando '
            f'com uma media de {dados[c]["media"]:.2f} gols por partida')

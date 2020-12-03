#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai
#ler a quantidade de gols feitos em cada partida. No final, tudo isso será, guar
#Dado em um dicionário, incluindo o total de gols feitos durante o campeonato
jogador={}
jogos=[]
total=0
jogador['Nome']=str(input('Nome do jogador: ')).strip()
partidas=int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range (0,partidas):
    gols=int(input(f'Numero de GOLS marcados no jogo {c+1}: '))
    jogos.append(gols)
    total=total+gols
jogador['Gol']=jogos[:]
jogador['Total']=total
print('***'*10)
for k,v in jogador.items():
    print(f'O campo {k} tem  valor {v}')
print('***'*10)
print(f'O jogador {jogador["Nome"]} fez {len(jogos)} partidas')
for c in range(0,len(jogos)):
    print(f'=> Na partida {c+1} ele fez {jogos[c]} gols.')
print('***'*10)
print(f'Foi um total de {len(jogos)} partidas e {total} gols.'
      f'\nTotalizando uma media de {total/len(jogos):.2f} gols por partida')
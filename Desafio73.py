#Crie uma tupla preenchida com os 20 primeiros colocados do Campeonato Bras. de Futebol
#na ordem de colocação. Depois mostre:
#Apenas os cinco primeiros colocados.
#Os ultimos quatro colocados.
#Uma lista dos times em ordem alfabética.
#Em que posição na tabela está o time do Chapecoense.
times=('INTERNACIONAL','ATLETICO MG', 'FLAMENGO','SANTOS','SÃO PAULO','GREMIO','FLUMINENSE','PALMEIRAS','CORINTHIANS',
       'FORTALEZA','BAHIA','SPORT','CEARÁ','ATLETICO GO','VASCO','ATHLETICO PR','CORITIBA','BRAGANTINO','BOTAFOGO','GOIAS')
print('\033[01;33m .\033[m '*20)
print(f'Os cinco primeiros colocados são: {times[0:4]}')
print('\033[01;33m .\033[m '*20)
print(f'Os quatro ultimos colocados são: {times[-4:]}')
print('\033[01;33m .\033[m '*20)
print(f'Em ordem alfabetica {sorted(times)}')
print('\033[01;33m .\033[m '*20)
escolha=str(input('Entre com um time: ')).strip().upper()
resposta =escolha in times
if resposta is False:
    escolha = str(input('Entre com um time: '))
print(f' O {escolha} está na {times.index(escolha)+1} posição')




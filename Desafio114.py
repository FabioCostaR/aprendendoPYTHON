#Crie um codigo em Python que teste se o site Pudim está acessivel no computador
import urllib
import urllib.request

try:
    site=urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('Deu Erro')
else:
    print('Deu Certo')
    print(site)
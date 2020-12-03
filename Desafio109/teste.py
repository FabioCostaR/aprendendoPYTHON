#Modifique as funções que foram criadas no desafio107 para que elas
#aceitem um parametro a mais, informando se o valor retornado por elas vai ser
#ou não ser formatado pela função moeda() desenvolvida no desafio 108

import moeda

p=float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p, True)} \n'
      f'O dobro de {p} e {moeda.dobro(p, True)} \n'
      f'Aumentando 10%, temos {(moeda.aumentar(p,10, True))} \n'
      f'Reduzindo 13%, temos {(moeda.diminuir(p,13, True))}')
#Adicione ao modulo da moeda.py criado nos desafios anteriores,
#uma função chamada resumo(), que mostre na tela algumas informações
#geradas pelas funções que já temos no modulo criado até aqui

import moeda

p=float(input('Digite o preço: R$'))
up=float(input('Acrescimo de : '))
dowm=float(input('Desconto de: '))
formato=str(input('Deseja em formato de dinheiro?[S/N] ')).upper().strip()[0]
if formato=='S':
      formato=True
else:
      formato=False
print(moeda.resumo(p,up,dowm,formato))
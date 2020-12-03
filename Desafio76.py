#Crie um programa que tenha uma tupla unica com nomes de produtos e seus
#respectivos preços, na sequencia.
#No final mostre uma listagem de preços, organizando os dados em forma tabular.
listagem=('pão',0.50,
          'mortadela',5.50,
          'queijo',19.90,
          'presunto',15.98)
print('='*30)
print('      TABELA DE PREÇOS')
print('='*30)
for pos in range(0,len(listagem)):
    if pos%2==0:
        print(f'{listagem[pos]:.<23}',end='')
    else:
        print(f'R${listagem[pos]:.>4.2f}')
print('='*30)
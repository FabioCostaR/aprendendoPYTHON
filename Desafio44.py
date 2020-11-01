#Elabore um programa que calcule o valor a ser pago por um produto, considerando
# Seu preço normal e condição de pagamento:
#A vista dinheiro/ cheque: 10% de desconto
#A vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#Em até 3x no cartão: 20% de juros
valor = float(input('Entre com o valor do produto: R$ '))
print('Selecione a opção de pagamento')
op1 = int(input('\033[01;31m [1] \033[m a vista \n'
                '\033[01;34m [2] \033[m a prazo \n'))
if op1==1:
    print('Você escolheu a opção pagamento à vista:')
    op2 = int(input('O pagamento será: \n'
                    '[1] no dinheiro \n'
                    '[2] no cheque \n'
                    '[3] no cartão \n'))
    if op2==1:
        print('O pagamento será em dinheiro')
        valor= valor -(valor*0.1)
        print(f' \033[01m VALOR TOTAL: \033[01;32m R${valor:.2f}')
    elif op2==2:
        print('O pagamento será no cheque')
        valor = valor - (valor * 0.1)
        print(f' \033[01m VALOR TOTAL: \033[01;32m R${valor:.2f}')
    elif op2==3:
        print('O pagamento será no cartão')
        valor = valor-(valor*0.05)
        print(f' \033[01m VALOR TOTAL: \033[01;32m R${valor:.2f}')
elif op1==2:
    print('Você escolheu a opção pagamento à prazo')
    op3 = int(input('A venda será parcelada em: \n'
                    '[1] Até 2 vezes \n'
                    '[2] Em 3 vezes \n'))
    if op3==1:
        print('O pagamento será parcelado em até 2 vezes ')
        print(f' \033[01m VALOR TOTAL: \033[01;32m R${valor:.2f}')
    elif op3==2:
        print(' O pagamento será parcelado em 3 vezes ')
        valor = valor+(valor*0.2)
        print(f' \033[01m VALOR TOTAL: \033[01;32m R${valor:.2f}')
else:
    print('\033[01m OPÇÃO INVÁLIDA')
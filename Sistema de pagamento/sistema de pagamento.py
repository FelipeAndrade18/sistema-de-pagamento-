from time import sleep
print('\033[1;30mSISTEMA  PARA FORMAS DE PAGAMENTO\033[m')
print('\033[1;35m-=-\033[m'*30)
normal = float(input('\033[1;30mQual valor do produto? R$ \033[m'))
print('\033[1;30mPROCESSANDO AS FORMAS DE PAGAMENTO..........\033[m')
sleep(3)
print('''\033[1;30mESCOLHA A FORMA DE PAGAMENTO :
[1] A vista no Dinheiro ou cheque com 10% de Desconto
[2] A Vista no Cartão com 5% de desconto
[3] Em 2x no cartão sem desconto e sem juros pagando o valor normal do produto
[4] 3x ou mais no Cartão de Crédito com 20% de juros sobre o valor normal\033[m ''')
print('\033[1;35m-=-\033[m'*30)
opção = int(input('\033[1;30mQual sua forma de pagamento escolhida ? :\033[1;30m'))
print('\033[1;35m-=-\033[m'*30)
print('\033[1;30mPROCESSANDO FORMA DE PAGAMENTO ESCOLHIDA ..........\033[m')
sleep(4)
if opção == 1:
    desconto = normal - (normal * 10 / 100)
    print('O produto custa R${:.2f} reais '.format(normal))
    print('Forma de pagamento escolhida: opção 1 você pagara R${:.2f} reais já com 10% de desconto em dinheiro ou cheque '.format(desconto))

elif opção == 2:
    desconto = normal - (normal * 5 / 100)
    print('O produto custa R${:.2f} reais'.format(normal))
    print('Forma de pagamento escolhida: opção 2 você pagara R${:.2f} reias já com 5% de desconto no cartão ! '.format(desconto))
elif opção == 3:
    print('Forma de pagamento escolhida: opção 3, você pagara R${:.2f} reias em 2x no cartão sem desconto e sem juros '.format(normal))
elif opção == 4:
    juros = normal + (normal * 20 / 100)
    print('O produto custa R${:.2f} reais'.format(normal))
    print('Forma de pagamento escolhida: opção 3, você pagara R${:.2f} reias já com 20% de juros para pagamento em 3x ou mais no cartão'.format(juros))
else:
    print('\033[1;31m OPÇÃO INVALIDADA TENTE NOVAMENTE \033[m !!!')

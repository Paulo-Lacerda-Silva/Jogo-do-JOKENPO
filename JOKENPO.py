from random import randint
from time import sleep

j = randint(0,2)
print('Vamos jogar JOKENPO')
print('''Digite [0] para pedra
Digite [1] para tesoura
Digite [2] para papel''')
n = int(input('Escolha a opção desejada: '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if j == 0 and n == 0:
    print('Os dois escolheram pedra, deu empate')
elif j == 0 and n == 1:
    print('O computador escolheu pedra, e pedra quebra a tesoura então o computador ganhou')
elif j == 0 and n == 2:
    print('O computador escolheu pedra, papel enrola pedra então voce ganhou ')


elif j == 1 and n == 1:
    print('Os dois escolheram tesoura, deu empate')
elif j == 1 and n == 0:
    print('O computador escolheu tesoura, pedra quebra tesoura então o voce ganhou')
elif j == 1 and n == 2:
    print('O computador escolheu tesoura, tesoura corta papel então o computador ganhou')


elif j == 2 and n == 2:
    print('Os dois escolheram papel, deu empate')
elif j == 2 and n == 1:
    print('O computador escolheu papel, tesoura corta papel então o voce ganhou')
elif j == 2 and n == 0:
    print('O computador escolheu papel, papel embrulha pedra, o computador ganhou')
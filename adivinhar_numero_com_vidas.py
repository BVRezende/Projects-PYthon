from emoji import emojize
from random import randint

# :broken_heart:
# :black_heart:
# :red_heart:

vidas_restantes = 5
vidas_perdidas = 0
flag = True

while flag:
    print('Vidas: {}{}'.format((vidas_restantes * emojize(':red_heart:')), (vidas_perdidas * emojize(':black_heart:'))))
    numero_sorteado = randint(1, 100)

    numero_escolhido = int(input('\nDigite um número: '))

    if numero_sorteado == numero_escolhido:
        print('\033[32mPARABÉNS, VOCÊ VENCEU!\033[m')
        flag = False
    else:
        vidas_restantes -= 1
        vidas_perdidas += 1

        if vidas_restantes == 0:
            print('\nVidas: {}{}'.format((vidas_restantes * emojize(':red_heart:')), (vidas_perdidas * emojize(':black_heart:'))))
            print('\033[31mQUE PENA, SUAS VIDAS ACABARAM... GAME OVER!\033[m')
            flag = False
        else:
            print('\033[31mNÚMERO INCORRETO, TENTE NOVAMENTE!\n\033[m')

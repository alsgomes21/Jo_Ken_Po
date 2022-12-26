from random import randint
from time import sleep

print('Bem vindo ao game PEDRA, PAPEL E TESOURA')

itens = ('Pedra', 'Papel','Tesoura')
computador = randint(0,2)


print('Suas opções são: ')
print('[0] PEDRA')
print('[1] Papel')
print('[2] Tesoura')

jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(2)
print('PO')
sleep(3)
print('-=' * 12)
print('Jogador jogou {}'.format(itens[jogador]))
print('O computador escolheu {}'.format(itens[computador]))

if computador == 0: # pedra
    if jogador == 0:
        print('Empate')

    elif jogador == 1:
        print('Jogador venceu')

    elif jogador == 2:
        print('Computador venceu')
    else:
        print('Jogada Inválida!')

elif computador == 1: # papel
    if jogador == 0:
        print('Computador venceu')
    elif jogador == 1:
        print('Empate')

    elif jogador == 2:
        print('Você venceu')

    else:
        print('Jogada Inválida!')

elif computador == 2: # tesoura
    if jogador == 0:
        print('Você venceu')
    elif jogador == 1:
        print('Computador venceu')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada Inválida!')
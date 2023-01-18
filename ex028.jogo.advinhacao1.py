from random import randint
from time import sleep
computador = randint (0,5)
# Faz o computador "PENSAR"
print ('\033[33m-=-' * 20)
print ('\033[34mVou pensar em um número entre 0 e 5. Tente advinhar...')
print('\033[33m-=-' * 20)
jogador = int(input('\033[mEm que número eu pensei? '))#Jogador tenta adivinhar
print('\033mPROCESSANDO...')
sleep(3)
if jogador == computador:
    print('\033[32mPARABÉNS! Você conseguiu me vencer!')
else:
    print(f'\033[31mGANHEI! Eu pensei no número {computador} e não no {jogador}!')
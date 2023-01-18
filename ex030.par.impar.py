número = int(input('\033[35mMe diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print(f'\033[37mO número {número} é \033[34mPAR')
else:
    print(f'\033[033[37mO número {número} é \033[34mÍMPAR')
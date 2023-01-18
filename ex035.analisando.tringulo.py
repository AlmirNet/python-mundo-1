print('-='*20)
print('\033[4;33;44m Analisandor de Trinâgulos')
print('\033[1;35;43m')
print('\033[30;42m -='*20)
print('\033[30;42m')
r1 = float(input('Primeiro segmento: '))
print('\033[m')
r2 = float(input('Segundo segmento: '))
print('\033[7;30m')
r3 = float(input('Terceiro segmento: '))
if r1 < r2 < + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(' Os segmentos acima PODEM FOEMAR triângulo! ')
else:
    print('Os segmentos acima NÃO PODEM \033[7;30m FORMAR triângulo \033[4;33;44m')
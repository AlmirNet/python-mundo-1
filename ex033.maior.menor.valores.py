a = int(input('Primeiro valor: '))
b = int(input('Segunhdo valor: '))
c = int(input('Terceira valor: '))
#Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor digitado foi {menor}')
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade-80) * 7
    print(f'Você deve pagar uma multa de \033[33mR${multa:.2f}')
print('\033[32mTenha um bom dia! Dirija com segurança!')
idade = int(input('Informe a sua idade -- '))
if idade >= 60:
    print('Você tem direito a desconto!')
else:
    print('Sem desconto!')

idade = int(input('Informe sua idade -- '))

if idade < 16:
    print('Não pode votar!')
elif idade == 16 or idade == 17:
    print('Voto opcional!')
elif 18 <= idade <= 69:
    print('Voto obrigatório!')
else:
    print('Voto opcional!')

vel = int(input('Informe a velocidade do carro -- '))
multa = (vel - 80) * 5
if vel > 80:
    print(f'Multa de R${multa:.2f}')
else:
    print('Velocidade dentro do limite')
nome = str(input("olá, me diga seu nome por gentileza: "))
print(f"opa bem vindo {nome} ")

dia = int(input("me diga o dia que vc nasceu: "))
mes = int(input("opa, me diga o mes que voce nasceu: "))
ano = int(input("e me diga seu ano de nascimento: "))
idade = 2025 - ano - 1

print(f"vc nasceu em {dia} / {mes} / {ano}")
print(f"voce tem {idade} anos")

if idade <= 11:
    print("vc é criança")

if idade >=12 and idade <=18:
    print("vc é adolescente")

if idade >= 19 and idade <=24:
    print(" és um jovem")

if idade >= 25 and idade <=40:
    print("vc é adulto") 

if idade >= 41 and idade <=60:
    print("vc é um meia idade")

if idade >= 60:
    print("voce é idoso")

soma = 0
while True:
    numero = int(input("digite um numero ate achar o valor especial: "))
    if numero == 0:
       break
    soma = soma + numero
    print(f" a soma de suas tentaivas é {soma}.")


# Atividade 1

numeroparimpar = int(input("Insira um número: "))
resultadoparimpar = numeroparimpar % 2
if resultadoparimpar == 0 :
    print("O número é par")
else:
    print("O número é ímpar")

# Atividade 2

numeroverif = int(input("Insira um número: "))

if numeroverif > 0:
    print("O número é positivo")
elif numeroverif == 0:
    print("O número é zero")
else:
    print("O número é negativo")

# Atividade 3

resposta = input("Pergunta aleatória. Responda: ")
if resposta == "a":
    print("resposta correta")
else:
    print("resposta errada")

# Atividade 4

primeirovalor = float(input("digite o primeiro valor: "))
segundovalor = float(input("digite o segundo valor: "))

divisaovalores = primeirovalor // segundovalor

senha = int(input("digite a senha: "))

if senha == divisaovalores:
    print("acesso liberado")
else:
    print("acesso negado")

# Atividade 5

quilo = float(input("quantos quilos de peixe? "))

if quilo > 50:
    multa = 4.00 * (quilo - 50)
    print(f"Olha a multa de {multa:.2f} reais!")
else:
    print("aprovado")

# Atividade 6

celsius = int(input("Insira a temperatura: "))

if celsius >= 30:
    print("Quente!")
elif celsius >= 20:
    print("Agradável!")
else:
    print("Frio!")

# Atividade 7

numero1digit = int(input("Insira o primeiro número: "))
numero2digit = int(input("Insira o segundo número: "))
numero3digit = int(input("Insira o terceiro número: "))

if numero1digit <= numero2digit <= numero3digit:
    print(f"{numero1digit}, {numero2digit}, {numero3digit}")
elif numero1digit <= numero3digit <= numero2digit:
    print(f"{numero1digit}, {numero3digit}, {numero2digit}")
elif numero2digit <= numero3digit <= numero1digit:
    print(f"{numero2digit}, {numero3digit}, {numero1digit}")
elif numero2digit <= numero1digit <= numero3digit:
    print(f"{numero2digit}, {numero1digit}, {numero3digit}")
elif numero3digit <= numero1digit <= numero2digit:
    print(f"{numero3digit}, {numero1digit}, {numero2digit}")
else:
    print(f"{numero3digit}, {numero2digit}, {numero1digit}")
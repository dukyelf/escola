# Questão 1

idade = int(input("Qual é a sua idade? "))  # Idade do usuário

if idade < 18: # se não for maior de idade
    print(f"Você tem {idade} anos, então você não pode dirigir") # Menor de 18
else: # se for maior de idade
    print(f"Você tem {idade} anos, então você pode dirigir") # Maior de 18

# Questão 2

nota = float(input("Qual é a sua nota? "))

if nota >= 7:
    print("A")
elif nota >= 5:
    print("PA")
else:
    print("NA")

# Questão 3

valorcompra = float(input("Insira o valor da compra -- "))

desconto = valorcompra - (valorcompra * 0.10)

if valorcompra > 100:
    print(f"Você recebeu um desconto de 10%, então você vai pagar {desconto:.2f}R$. =]")
else:
    print(f"Você vai pagar {valorcompra:.2f}R$. =]")

#  Questão 4

lado1 = float(input("Digite o primeiro lado do triângulo -- "))
lado2 = float(input("Digite o segundo lado do triângulo -- "))
lado3 = float(input("Digite o terceiro lado do triângulo -- "))

if lado1 == lado2 == lado3:
    print("Triângulo equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo isóceles")
else:
    print("Triângulo escaleno")

# Questão 5

idadeingressos = int(input("Qual é a sua idade? -- "))

if idadeingressos < 12:
    print(f"Você tem {idadeingressos} anos, então você vai pagar 10R$.")
elif idadeingressos >= 60:
    print(f"Você tem {idadeingressos} anos, então você vai pagar 15R$.")
else:
    print(f"Você tem {idadeingressos} anos, então você vai pagar 20R$.")

# Questão 6

numerointervalo = int(input("Digite um número -- "))

if numerointervalo >= 10 and numerointervalo <= 50:
    print(f"O número {numerointervalo} está dentro do intervalo.")
else:
    print(f"O número {numerointervalo} está fora do intervalo.")

# Questão 7

peso = float(input("Peso -- "))
altura = float(input("Alura -- "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")

# Questão 8

ano = int(input("Digite o ano -- "))

if ano % 4 == 0:
    print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} não é um ano bissexto")

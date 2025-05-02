print("### Jogo de Adivinhação ###")
print("Qual a capital do Mato Grosso?")
print("A) - Salvador")
print("B) - Congonhas")
print("C) - Rio Branco")
print("D) - Cuiabá")
print("E) - Campo Grande")

op = input("informe a letra da resposta correta: ")

if op == "D":
    print(f"A resposta {op} está correta!")
if op == "d":
    print(f"A resposta {op} está correta!")
else:
    print(f"A resposta {op} está INCORRETA!")

numero = int(input("Insira um número: "))

if numero > 10:
    print(f"O número {numero} é maior do que o número 10")
elif numero < 10:
    print(f"O número {numero} é menor do que o número 10")
else:
    print(f"O número 10 é igual ao número 10")
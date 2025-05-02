  # Primeira questão -- Par

n = int(input("Insira um número -- "))
soma = 0
for i in range(1, n+1):
    if i % 2 == 0:
        soma += i
print(f"A soma dos números pares de 1 até {n} é {soma}")

  # Ímpar --

n2 = int(input("Insira um número -- "))
soma2 = 0
for i in range(1, n2+1):
    if i % 2 != 0:
        soma2 += i
print(f"A soma dos números ímpares de 1 até {n2} é {soma2}")

  # Segunda questão --

contagem = 0
for i in range(10):
    idade = int(input("Insira uma idade -- "))
    if idade >= 18:
        contagem += 1
print(f"Quantidade de pessoas maiores de idade: {contagem}")

  # Segunda questão da segunda avaliação --

n3 = int(input("Insira um número -- "))
somadiv = 0
for i in range(1, n3):
    if n3 % i == 0:
        somadiv = somadiv + i
if somadiv == n:
    print(f"{n3} é um número perfeito")
else:
    print(f"{n3} não é um número perfeito")

  # Terceira questão --

controle = 0
soma3 = 0
n4 = float(input("Insira a 1ª nota -- "))
while n4 != -1:
    controle += 1
    soma3 += n4
    n4 = float(input(f"Insira a {controle+1}ª nota -- "))
if controle > 0:
    media = soma3 / controle
    print(f"A média das notas é {media}")
else:
    print("Nenhuma nota foi informada")

  # Pluh!
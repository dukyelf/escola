# 1ª questão

listanumeros = []
quantidadenumeros = int(input("Quantos números você quer digitar?   "))

for i in range(quantidadenumeros):
    listanumeros.append(int(input(f"Insira o {i+1}º número.   ")))

listanumeros.sort()

print("O maior número é:",listanumeros[quantidadenumeros-1])
print("O menor número é:",listanumeros[0])

# 2ª questão

n = int(input("Digite um número.   "))
fatorial = 1
for i in range(1, n+1):
   fatorial = fatorial * i
print(f"O fatorial de {n} é {fatorial}.")

# 3ª questão

fibonacci = int(input("Insira um número.  "))
prinum = 0
segnum = 1
fibolista = []

for i in range(fibonacci):
    fibolista.append(prinum)
    prinum, segnum = segnum, prinum + segnum

print(f"A sequência de Fibonacci é: {fibolista}")

#4ª questão

lista1 = []
lista2 = []

for i in range(3):
    lista1.append(int(input(f"Insira o 1º conjunto de números -- ")))

for i in range(3):
    lista2.append(int(input(f"Insira o 2º conjunto de números -- ")))

lista3 = lista1 + lista2    
lista3.sort()
lista3 = set(lista3)

print(*lista3)
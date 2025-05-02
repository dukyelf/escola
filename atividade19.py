# 1ª questão

listanumeros = []
quantidadenumeros = int(input("Quantos números você quer digitar?   "))

for i in range(quantidadenumeros):
    listanumeros.append(int(input(f"Insira o {i+1}º número.   ")))

listanumeros.sort()

print("O maior número é:",listanumeros[quantidadenumeros-1])
print("O menor número é:",listanumeros[0])

# 2ª questão

fatorial = int(input("Digite um número.   "))

fatlista = [1]
fatquantres = 1

for i in range(1, fatorial):
    fatquantres = fatquantres * (i+1)
    fatlista.append(fatquantres)

print(f"O fatorial de {fatorial} é {fatlista[fatorial-1]}.")

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
    lista1.append(int(input(f"Insira o 2º conjunto de números -- ")))
    
lista1.sort()
print(lista1)
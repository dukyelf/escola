import sys
'''# Questão 1

listanum = []
listanum2 = []
for i in range(10):
    listanum.append(int(input("Insira um número -- ")))

listanum2 = listanum.copy()
listanum.sort()

if listanum == listanum2:
    print("Os números estão em ordem crescente")
else:
    print("Os números não estão em ordem crescente")

# Questão 2

lista100 = []
for i in range(15):
    lista100.append(int(input("Insira um número -- ")))

lista100.reverse()
print(f"Lista invertida: {lista100}")

lista100.reverse()
lista100.insert(2, 35)
print(f"Lista após modificação: {lista100}")

while 7 in lista100:
    lista100.remove(7)
print(f"Lista após remoção do número 7 (se houver): {lista100}")

lista45 = []
lista45a = 0
while 45 in lista100:
    lista45a = lista100.index(45)
    lista45.append(lista45a)
    lista100.insert((lista45a), 1)

print(lista45)

# Terceira questão

numero = input("Insira uma lista de números inteiros separados por espaço -- ")
lista = numero.split(" ")
lista_int = [int(n) for n in lista]

# Quarta questão -- 

numero = input("Insira uma lista de números inteiros separados por espaço -- ")
lista = numero.split(" ")
lista_int = [int(n) for n in lista]
print(lista_int)

lista_int.sort()
print(lista_int)

diferenca = lista_int[-1] - lista_int[0]
print(diferenca)'''

# Quinta questão

print("-" *45)
print("Seja bem-vindo a pizzaria!")
print("-" *45)

valor = []

print("1 - Queijo: R$ 15")
print("2 - Pepperoni: R$ 20")
print("3 - Vegetariana: R$ 18")

pizza = int(input("Insira a pizza que você quer -- "))
if pizza == 1:
    valor.append(15)
elif pizza == 2:
    valor.append(20)
elif pizza == 3:
    valor.append(18)
else:
    print("Pizza não encontrada!")
    sys.exit()

print("-" *45)
print("1 -- Cogumelos: R$ 2 por unidade")
print("2 -- Azeitonas: R$ 1 por unidade")
print("3 -- Pimentão: R$ 1.5 por unidade")
print("4 -- Extra queijo: R$ 3 por unidade")
print("-" *45)

quantingredientes = int(input("Você quer quantos ingredientes? -- "))

if quantingredientes == 0:
    valortotal = sum(valor)
    print(f"O valor total foi R${valortotal:.2f}")
    sys.exit()

if quantingredientes > 4:
    print("Você só pode escolher 4 ingredientes")
    sys.exit()

print("-" *45)

for i in range(quantingredientes):
    ingrediente = int(input(f"Insira o {i+1}º ingrediente -- "))
    contingrediente = int(input("Quantos? -- "))
    if ingrediente == 1:
        valor.append(2*contingrediente)
    elif ingrediente == 2:
        valor.append(1*contingrediente)
    elif ingrediente == 3:
        valor.append(1.5*contingrediente)
    elif ingrediente == 4:
        valor.append(3*contingrediente)
    else:
        print("Ingrediente não encontrado!")
        sys.exit()

valortotal = sum(valor)

print("-" *45)
print(f"O total foi R${valortotal:.2f}")
print("-" *45)
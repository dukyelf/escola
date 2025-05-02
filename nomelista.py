import time

lista_nomes = []
for i in range(10):
    lista_nomes.append(input("Insira um nome -- "))

print("")
time.sleep(1)
for nome in lista_nomes:
    print(nome)
nome1 = ["Matheus", "Spencer", "Linus", "Jagger", "Jonathan Quin", 5, 6, 0.01111] # isso é uma lista

print(nome1[3])

nomes = []
controle = 0
while controle < 5:
    nomes.append(input("Informe um nome -- "))
    controle += 1
print(nomes)

for i in range(5):
    print(nomes[i])
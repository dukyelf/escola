num = int(input("Insira um número inteiro positivo -- "))
soma = 0
for item in range(0, num+1, 2):
    if item % 2 == 0:
        soma += item
print(soma)
import time
num = int(input("Insira um número inteiro -- "))
for item in range(num, 0, -1): # um valor = final, dois valores = inicio e final, três valores = inicio, final e passo
    print(item)
    time.sleep(1)
print("Lançamento!")
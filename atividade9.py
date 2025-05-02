# Enquanto uma condição for verdadeira, repita;
import time
numero = 0
while numero < 10:
    print("Mensagem")
    numero = numero + 1

contagem = int(input("Insira um número inteiro positivo -- "))

while contagem > 0:
    print(contagem)
    contagem = contagem - 1
    time.sleep(1)

    if contagem == 0:
        print("Lançamento!")



numero1 = int(input("Insira o primeiro número -- "))
soma = 0
while numero1 != 0:
    soma + soma + numero1
    numero1 == int(input("Insira o primeiro número -- "))
print(f"Soma total: {soma}")
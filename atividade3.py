numero3digit = int(input("Insira um número de três dígitos: "))

centena = numero3digit // 100
dezena = (numero3digit // 10) % 10
unidade = numero3digit % 10

resultado = centena + dezena + unidade

print("Soma dos três números: ", resultado)
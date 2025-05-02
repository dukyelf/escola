'''numero = int(input("Insira um número positivo -- "))
multi = 1

print(f"Os cinco primeiro múltiplos de {numero} são: ")

for item in range(0, 5, 1):
    print(numero * multi)
    multi += 1'''

quantnotas = int(input("Quantas notas você deseja informar -- "))
nota = []
for i in range(1, quantnotas+1):
    nota.append(float(input(f"Insira a {i}ª nota -- ")))
medianota = sum(nota) / len(nota)
print(f" A sua média foi {medianota}")

quantnum = int(input("Quantos números você deseja informar -- "))
somanum = []
for i in range(1, quantnum+1):
    somanum.append(int(input(f"Insira o {i}º número -- ")))
media = sum(somanum) / len(somanum)
print(f" A sua média foi {media}")



palavras = []
for i in range(3):
    palavras.append(input(f"Insira a {i+1}ª palavra -- "))

palavras.reverse()
for palavra in palavras:
    print(palavra)
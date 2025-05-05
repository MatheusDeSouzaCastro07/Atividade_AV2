numero = int(input("Digite um número inteiro para ver sua tabuada: "))
print(f"\nTabuada do {numero}:")
for n in range(1, 11):
    resultado = numero * n
    print(f"{numero} * {n} = {resultado}")
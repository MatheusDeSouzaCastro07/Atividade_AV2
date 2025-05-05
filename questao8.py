valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))
valores = [valor1, valor2, valor3]
valores.sort(reverse=True)
print("Valores em ordem decrescente:", valores[0], valores[1], valores[2])
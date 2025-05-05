lado1 = float(input("Digite o valor do primeiro lado do triângulo: "))
lado2 = float(input("Digite o valor do segundo lado do triâmgulo: "))
lado3 = float(input("Digite o valor do terceiro lado do triângulo: "))
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print("Triângulo equilátero (todos os lados são iguais).")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo isósceles (dois lados iguais).")
    else:
        print("Triângulo escaleno (todos os lados são diferentes).")
else:
    print("Os valores não formam um triângulo válido.")
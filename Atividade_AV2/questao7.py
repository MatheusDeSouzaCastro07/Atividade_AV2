def ler_valor (mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor == 0 or valor == 1:
                return valor
            else:
                print("Digite apenas 0 (PARA FALSO) ou 1 (PARA VERDADEIRO).")
        except ValueError:
            print("Entrada inválida. Digite apenas os números 0 (falso) ou 1 (verdadeiro).")
valor1 = ler_valor ("Digite o primeiro valor (0 para falso ou 1 para verdadeiro: ")
valor2 = ler_valor ("Digite o segundo valor (0 para falso ou 1 para verdadeiro: )")
if valor1 == 1 and valor2 == 1:
    print("Ambos os valores são verdadeiros")
elif valor1 == 0 and valor2 == 0:
    print("Ambos os valores são falsos")
else:
    print("Os valores são diferentes")
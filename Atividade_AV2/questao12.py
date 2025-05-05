valor_produto = float(input("Digite o valor do produto: "))
print("\nFormas de pagamento:")
print("1 - À Vista em dinheiro ou pix (15% de desconto)")
print("2 - À Vista no cartão de crédito (10% de desconto)")
print("3 - Parcelado em 2x no cartão (sem desconto)")
print("4 - Parcelado em 3x ou mais no cartão (com 10% de juros)")
codigo = int(input("Digite o código da forma de pagamento (1 a 4): "))
if codigo == 1:
    valor_final = valor_produto - (valor_produto * 0.15)
elif codigo == 2:
    valor_final = valor_produto - (valor_produto * 0.10)
elif codigo == 3:
    valor_final = valor_produto
elif codigo == 4:
    valor_final = valor_produto + (valor_produto * 0.10)
else:
    print("Código inválido!, Tente novamente!")
    valor_final = None
if valor_final is not None:
    print(f"\nValor final a pagar: R${valor_final:.2f}")
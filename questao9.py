peso = float(input("Digite o seu peso(kg): "))
altura = float(input("Digite a sua altura(m): "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")
if imc < 18.5:
    print("Abaixo do peso")
elif 18.6 <= imc <=24.9:
    print("Peso ideal (parabéns)")
elif 25.0 <= imc <= 29.9:
    print("Levemente acima do peso")
elif 30.0 <= imc <= 34.9:
    print("Obesidade grau I")
elif 35.0 <= imc <= 39.9:
    print("Obesidade grau II (severa)")
else:
    print("Obesidade grau III (mórbida)")   
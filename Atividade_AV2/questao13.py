nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade da pessoa: "))
if idade >= 18:
    print(f"{nome} é maior de idade")
else:
    print(f"{nome} é menor de idade")
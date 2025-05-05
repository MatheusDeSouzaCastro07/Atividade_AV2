nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"\n Nome do aluno: {nome_aluno}")
print(f"\n A média do aluno {nome_aluno} é: {media:.2f}")
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
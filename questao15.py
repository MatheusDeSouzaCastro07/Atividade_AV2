from datetime import date
ano_nascimento = int(input("Digite o ano do seu nasimento: "))
hoje = date.today()
ano_atual = hoje.year
mes_atual = hoje.month
dia_atual = hoje.day
anos = ano_atual - ano_nascimento
meses = anos * 12
dias = anos * 365
print(f"Você já viveu aproximadamente {anos} anos, {meses} meses e {dias} dias.")
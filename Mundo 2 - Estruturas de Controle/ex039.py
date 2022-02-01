from datetime import date

anoNasc = int(input("Ano de Nascimento: "))
anoAtual = date.today().year
idade = anoAtual - anoNasc

print(f"Quem nasceu em {anoNasc} tem {idade} anos em {anoAtual}.")

if (idade < 18):
    print(f"Ainda faltam {18 - idade} para o alistamento")
    print(f"Seu alistamento será em {anoNasc + 18}")
elif (idade > 18):
    print(f"Você já deveria ter se alistado há {idade - 18} anos.")
    print(f"Seu alistamento foi em {anoNasc + 18}.")
else:
    print(f"Você tem que se alistar IMEDIATAMENTE!")




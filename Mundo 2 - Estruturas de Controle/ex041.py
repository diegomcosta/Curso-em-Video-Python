from datetime import date

anoNasc = int(input("Ano de Nascimento: "))
anoAtual = date.today().year
idade = anoAtual - anoNasc

print(f"O atleta tem {idade} anos.")

if (idade < 9):
    classificação = "MIRIM"
elif (9 <= idade < 14):
    classificação = "INFANTIL"
elif (14 <= idade < 19):
    classificação = "JÚNIOR"
elif (19 <= idade < 25):
    classificação = "SÊNIOR"
else:
    classificação = "MASTER"

print(f"Classificação: {classificação}")

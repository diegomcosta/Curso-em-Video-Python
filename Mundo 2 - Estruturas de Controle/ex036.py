valor = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento? "))
valorFinanciamento = valor / (anos * 12)
print(f"Para pagar uma casa de R${valor:.2f} em {anos}anos a prestação será de R${valorFinanciamento:.2f}")

if (valorFinanciamento <= salario * 0.3):
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")
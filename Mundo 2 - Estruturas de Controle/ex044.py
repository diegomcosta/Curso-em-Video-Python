print("=" * 10, end=" ")
print("LOJAS DIEGO", end=" ")
print("=" * 10)

preco = float(input("Preço das compras: R$"))
print("\nFORMAS DE PAGAMENTO")
print("[ 1 ] à vista dinheiro/cheque")
print("[ 2 ] à vista cartão")
print("[ 3 ] 2x cartão")
print("[ 4 ] 3x ou mais no cartão\n")

op = int(input("Qual é a opção? "))

if (op == 1):
    npreco = preco - (preco * 0.1)  
elif (op == 2):
    npreco = preco - (preco * 0.05)
elif (op == 3):
    parcela = preco / 2
    print(f"Sua compra será parcelada em 2X de R${parcela:.2F} SEM JUROS")
elif (op == 4):
    parcela = int(input("Quantas parcelas? "))
    npreco = preco + (preco * 0.2)
    valparcela = npreco / parcela
    print(f"Sua compra será parcelada em {parcela}X de R${valparcela:.2f} COM JUROS",end=" ")
    print(f"de valor R${preco * 0.2:.2f}")
print(f"Sua compra de R${preco:.2f} vai custar R${npreco:.2f} no final.")

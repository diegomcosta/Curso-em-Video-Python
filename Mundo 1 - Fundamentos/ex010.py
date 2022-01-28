# a cotação do dólar a ser utilizada é de R$5,39 - dia 28/01/2021

real = float(input("Quanto dinheiro você tem na carteira? R$ "))
print(f"Com R${real:.2f} você pode comprar US${real/5.39:.2f}")

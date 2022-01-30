salario = float(input("Qual é o salário do funcionário? R$"))
if ( salario <= 1250 ):
    aumento = 15
else:
    aumento = 10
nsalario = salario + (salario * (aumento /100))
print(f"Quem ganhava R${salario:.2f} passa a ganhar R${nsalario:.2f} agora.")
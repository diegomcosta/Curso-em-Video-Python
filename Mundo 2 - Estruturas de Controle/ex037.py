n = int(input("Digite um número inteiro: "))
print("Escolha uma das bases para conversão:")
print("[ 1 ] converter para BINÁRIO")
print("[ 2 ] converter para OCTAL")
print("[ 3 ] converter para HEXADECIMAL")

op = int(input("Sua opção: "))

if (op == 1):
    base = "BINÁRIO"
    resultado = bin(n)
elif (op == 2):
    base = "OCTAL"
    resultado = oct(n) 
elif (op == 3):
    base = "HEXADECIMAL"
    resultado = hex(n)

print(f"{n} convertido para {base} é igual a {resultado[2:]}")


   
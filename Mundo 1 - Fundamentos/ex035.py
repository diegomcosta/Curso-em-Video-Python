print("-=-" * 20)
print("Analisador de Triângulos")
print("-=-" * 20)

n1 = float(input("Primeiro segmento: "))
n2 = float(input("Segundo segmento: "))
n3 = float(input("Terceiro segmento: "))

if (n2 - n3 < n1 < n2 + n3) and (n1 - n3 < n2 < n1 + n3) and (n1 - n2 < n3 < n1 + n2):
    print("Os segmentos acima PODEM formar triângulo!")
else:
    print("Os segmentos acima NÃO PODEM formar triângulo!")

import math
cat_op = float(input("Comprimento do cateto oposto: "))
cat_adj = float(input("Comprimento do cateto adjacente: "))

#Existem 2 maneiras de se resolver esse problema.

hip = ((cat_op**2) + (cat_adj**2)) ** 0.5 #usando a formula da hipotenusa mesmo: a² = b² + c²

print(f"A hipotenusa vai medir {hip:.2f}")

hipotenusa = math.hypot(cat_op, cat_adj)

print(f"A hipotenusa vai medir {hipotenusa:.2f}") #utilizando a biblioteca math e funções pré definidas


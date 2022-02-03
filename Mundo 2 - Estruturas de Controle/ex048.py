c = 0
s = 0
for i in range(1, 501):
    if (i % 2 != 0) and (i % 3 == 0):
        c += 1
        s += i
print(f" A soma dos {c} valores solicitados é {s}")

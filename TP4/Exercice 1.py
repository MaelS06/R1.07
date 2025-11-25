x = float(input("Donnez un nombre : "))
table = []
for i in range(10):
    y = x * i
    table.append(y)
for i in range(10):
    print(f"{x} * {i} = {round(table[i], 1)}")

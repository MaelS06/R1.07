a = 0
b = 0
c = 0
for i in range(10):
    n = int(input("Entrez un nombre entre 0 et 20"))
    if n >= 0 and n <= 20:
        if n < 10:
            a = a + 1
        elif n>=10 and n < 15:
            b = b + 1
        else :
            c = c + 1
    else :
        nb = int(input("Entrez un nombre entre 0 et 20"))
print ("Il y a", a, "valeurs inférieur strictement à 10,", b, "valeurs supérieur ou égale à 10 et inférieur strictement à 15,", c, "valeurs supérieur ou égale à 15")
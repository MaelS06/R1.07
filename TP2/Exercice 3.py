a=input("Entrez la premiere  valeur : ")
b=input("Entrez la deuxieme  valeur : ")
c=input("Entrez la troisieme valeur : ")

print("Les valeurs entrees sont : a = " + a + ", b = " + b + " et c = " + c)
print("Permutation: a ==> b, b ==> c, c ==> a")
"""      *******************************************
         * Completez le programme a partir d'ici.
         *******************************************
"""
tmp = b
tmp2 =c
b = a
c = tmp
a = tmp2
"""     *******************************************
         * Ne rien modifier apres cette ligne.
         *******************************************
"""

print("Les valeurs permutees sont : a = " + a + ", b = " + b + " et c = " + c)
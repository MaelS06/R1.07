T = input("Entrez la chaîne : ")

i = 0
for _ in T:
    i += 1
taille = i
print("Taille :", taille)

voyelles = "aeiouyAEIOUY"
nb_voyelles = 0

for c in T:
    if c in voyelles:
        nb_voyelles += 1

pourcentage = (nb_voyelles / taille) * 100 if taille > 0 else 0
print("Pourcentage de voyelles :", pourcentage)

mot = "wagon"
found = False
pos = -1

for i in range(taille - 4):
    correspond = True
    for j in range(5):
        if T[i + j].lower() != mot[j]:
            correspond = False
            break
    if correspond:
        found = True
        pos = i
        break

if found:
    print("La chaîne 'wagon' apparaît à partir de la position :", pos)
else:
    print("La chaîne 'wagon' n'est pas présente.")

nb_occ = 0

for i in range(taille - 4):
    correspond = True
    for j in range(5):
        if T[i + j].lower() != mot[j]:
            correspond = False
            break
    if correspond:
        nb_occ += 1

print("Nombre d'occurrences de 'wagon' :", nb_occ)

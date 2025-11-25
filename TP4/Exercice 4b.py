L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]

meilleur_cherche = L1[0]
meilleure_freq = L1.count(L1[0])

for nb in L1:
    cpt = L1.count(nb)

    if cpt > meilleure_freq:
        meilleure_freq = cpt
        meilleur_cherche = nb

print(f"Le nombre le plus frequent dans la liste est le : {meilleur_cherche} ({meilleure_freq} x)")

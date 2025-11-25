""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * """

L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]

mlr_cherche = L1[0]
mlr_cpt = 1

for k in range (len(L1)):
    cherche = L1[k]

    cpt = 0
    for k in range(1, len(L1)):
        if L1[k] == cherche :
            cpt += 1

    if cpt > mlr_cpt:
        mlr_cpt = cpt
        mlr_cherche = cherche

print(f"Le nombre le plus frequent dans la liste est le : {mlr_cherche} ({mlr_cpt} x)")

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""

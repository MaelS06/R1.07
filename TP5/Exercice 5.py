heures = float(input("Entrez le nombre d'heures travaillées : "))
taux = float(input("Entrez le salaire horaire : "))

if heures <= 160:
    salaire = heures * taux

elif heures <= 200:
    salaire = 160 * taux
    salaire += (heures - 160) * taux * 1.25

else:
    salaire = 160 * taux
    salaire += 40 * taux * 1.25
    salaire += (heures - 200) * taux * 1.50

print("Salaire total :", salaire)

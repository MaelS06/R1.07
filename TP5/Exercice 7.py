import os.path
from datetime import datetime

f1 = input("Entrez le nom du premier fichier : ")
f2 = input("Entrez le nom du second fichier : ")

def infos(f):
    if os.path.isfile(f):
        taille = os.path.getsize(f)
        date = os.path.getmtime(f)
        date_format = datetime.fromtimestamp(date)
        print(f"Fichier : {f}")
        print("  Taille :", taille, "octets")
        print("  Dernière modification :", date_format)
        return date
    else:
        print(f"Le fichier {f} n'existe pas.")
        return None

d1 = infos(f1)
d2 = infos(f2)

if d1 is not None and d2 is not None:
    if d1 > d2:
        print("Le fichier le plus récent est :", f1)
    else:
        print("Le fichier le plus récent est :", f2)

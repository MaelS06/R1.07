nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes = []
for i in range (nombreEtudiants) :
    notes.append(float(input(f"La note de l'èleve est : {i + 1}")))
moy = sum(notes) / nombreEtudiants
print(f"La moyenne de la classe est : {moy}")
x = moy - notes
print(f"{i + 1} | {notes} | {x}")



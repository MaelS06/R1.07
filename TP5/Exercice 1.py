nom1 = input("Entrez le nom de la personne 1 : ")
prenom1 = input("Entrez le prénom de la personne 1 : ")

nom2 = input("Entrez le nom de la personne 2 : ")
prenom2 = input("Entrez le prénom de la personne 2 : ")

nom1 = nom1.upper()
prenom1 = prenom1.capitalize()

nom2 = nom2.upper()
prenom2 = prenom2.capitalize()

p1 = (nom1, prenom1)
p2 = (nom2, prenom2)

if p1 <= p2:
    print(prenom1, nom1)
    print(prenom2, nom2)
else:
    print(prenom2, nom2)
    print(prenom1, nom1)

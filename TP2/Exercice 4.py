base = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
nbconvives = int(input("Entrez le nombre de personnes conviées à la fondue :"))
print("Pour faire une fondue fribourgeoise pour", nbconvives, ", il vous faut : ")
fromage = 200.0*nbconvives
eau = 0.5*nbconvives
ail = 0.5*nbconvives
pain = 100.0*nbconvives
print("-", fromage, "gr de fromage")
print("-", eau, "dL d'eau")
print("-", ail, "gousses d'ail")
print("-", pain, "gr de pain")




somme = 0
sommeCoef = 0
admis = True

for i in range(1, 6):
    s = input(f"Veuillez entrer la note du module {i} et le coefficient correspondant : ")
    note, coef = s.split()
    note = float(note)
    coef = int(coef)

    somme += note * coef
    sommeCoef += coef

    if note < 8:
        admis = False

moyenne = somme / sommeCoef
print("Moyenne :", moyenne)

if moyenne > 10 and admis:
    print("Admis")
else:
    print("Non admis")

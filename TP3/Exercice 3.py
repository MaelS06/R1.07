import random

x = random.randint(0, 100)
tentatives = 0
trouve = False

while not trouve:
    user_input = int(input("Devinez le nombre (entre 0 et 100) : "))
    tentatives += 1

    if user_input == x:
        print("Trouvez !")
        break
    elif user_input > x:
        print("Trop petit !")
    elif user_input < x:
        print("Trop grand !")
    elif user_input > 100 and user_input < 0:
        print("merci d'entrer une valuer entre 0 et 100 !")
print("Le nombre de tentative est :", tentatives)
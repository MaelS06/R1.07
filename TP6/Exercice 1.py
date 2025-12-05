print("\n=== e) Test avec une chaîne ===")
s = "machaine"
print("Chaîne :", s)
print("ID de la chaîne :", id(s))
print("Type :", type(s))

print("\nIdentifiants de chaque caractère :")
for i, c in enumerate(s):
    print(f"Caractère {i} : '{c}', type={type(c)}, id={id(c)}")
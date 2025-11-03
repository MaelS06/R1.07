Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> jour = int(input())
24
>>> heure = int(input())
13
>>> minute = int(input())
48
>>> jour = jour*(60*24)
>>> print(jour)
34560
>>> heure = heure*60
>>> print(heure)
780
>>> total = jour+minute+heure
>>> print(total)
35388

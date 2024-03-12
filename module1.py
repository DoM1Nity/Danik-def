from OmaModul import *

failide_kustutamine()

ümber_kirjuta_fail(input("Faili nimi: "))

kirjuta_failisse("päevad.txt")

päevad=loe_failist("Päevad.txt")

#1
print(päevad)
#2
for päev in päevad:
    print(päev)

from OmaModul import *
from random import *
file = open("Ankeet.txt", "r", encoding='utf-8')
kasutajanimed=[]
salas�nad=[]
while True:
    print("1-Administraatori registreerimine\n2-Kasutaja\n3-Andiminstarot")
    vastus=int(input("Sisestage arv"))
    if vastus==1:
       print("Administraatori registreerimine")
       kasutajanimed,salas�nad=registreerimine(kasutajanimed,salas�nad)
    elif vastus==2:
           print("Kasutaja")
           print("Tere tulemast viktoriinile!")
           nimi=input("Mis on sinu nimi? ")
           print("Tere", nimi)      
           �igevastus=0  
           for rida in file:
               N=rida.split(":")
               print(N[0])
               katsed=3
               while katsed>0:
                   sisend=input("Vastus: ").strip()
                   if sisend==N[1].strip():
                      �igevastus+=1
                      print("Tubli!")
                      break
                   else:
                      katsed-=1
                      print("Viga. Teil on",katsed,"katse.")
               else:
                  print("Enam katseid pole j��nud. �ige vastus on:",N[1].strip())
           print("�igete vastuste arv:",�igevastus)
    elif vastus==3:
       autoriseerimine(kasutajanimed,salas�nad)
       k�simused=loe_ankeet("Ankeet.txt")
       print(f"K�simused on: " + str(k�simused[0]),"Vastused on: " + str(k�simused[1]))
file.close()

   
failide_kustutamine()

�mber_kirjuta_fail(input("Faili nimi: "))

kirjuta_failisse("P�evad1.txt")

p�evad=loe_failist("P�evad1.txt")
print(p�evad)
for p�ev in p�evad:
    print(p�ev)

﻿from pickle import FALSE
from string import *
from time import sleep
def registreerimine(kasutajad:list,paroolid:list)->any:
    """Funktsioon tagastab kasutajad ja paroolid
    :param list kasutajad: kasutajad nimed list
    :param list paroolid: paroolide nimed list
    :trype: lisy,list
    """
    while True:
        nimi=input("Mis on sinu kasutajanimed? ")
        if nimi not in kasutajad:
            while True:
                parool=input("Mis on sinu salasõnad? ")
                flag_p=False
                flag_l=False
                flag_u=False
                flag_d=False
                if len(parool)>=8:                  
                    parool_list=list(parool)
                    for p in parool_list:
                        if p in punctuation:
                               flag_p=True
                        elif p in ascii_lowercase:
                              flag_l=True
                        elif p in ascii_uppercase:
                              flag_u=True
                        elif p in digits:
                              flag_d=True
                    if flag_p and flag_u and flag_l and flag_d:
                          kasutajad.append(nimi)
                          paroolid.append(parool)
                    break
                else:
                   print("Nõrk salasõna!")
            break
        else:
            print("Selline kasutaja on juba olemas!")
    return kasutajad, paroolid
def autoriseerimine(kasutajad:list,paroolid:list):
    """Funktsioon kuvab ekraanile "Tere tulemast!" kui kasutaja on olemas nimekirjas"""

    p=0
    while True:
        nimi=input("Sisesta kasutajanimi: ")
        if nimi in kasutajad:
            while True:
               parool=input("Sisesta salasõna: ")
               p+=1
               try:
                   if kasutajad.index(nimi)==paroolid.index(parool):
                       print(f"Tere tuleamst! {nimi}")
                       break
               except:
                   print("ale nimi või salasõna!")
                   if p==5:
                       print ("Proovi uuesti 10 sek pärast")
                       for i in range(10):
                           sleep(1)
                           print(f"On häänud {10-i} sek")
    else:
        print("Kasutajat pole")
def nime_või_parooli_muutmine(list_:list):
    """
    """
    muutuja=input("Vana nimi või parool: ")
    if muutuja in list_:
        indeks=list_.index(muutuja)
        muutuja=input("Uus nimi või parool: ")
        list_[indeks]=muutuja
    return list
def unustanud_üarooli_taastamine(kasutajad: list, paroolid: list):
    """Funktsioon aitab kasutajal unustatud parooli taastada."""
    nimi = input("Sisesta kasutajanimi, mille parooli soovid taastada: ")
    if nimi in kasutajad:
        indeks = kasutajad.index(nimi)
        vastus = input(f"Kas soovid taastada parooli kasutajale '{nimi}'? (jah/ei): ")
        if vastus.lower() == "jah":
            vana_parool = input("Sisesta vana parool: ")
            if vana_parool == paroolid[indeks]:
                uus_parool = input("Sisesta uus parool: ")
                paroolid[indeks] = uus_parool
                print("Parool on edukalt muudetud!")
            else:
                print("Vale vana parool! Parooli muutmine ebaõnnestus.")
        else:
            print("Parooli muutmine tühistatud.")
    else:
        print("Sellise kasutajanimega kasutajat ei leitud.")

    return kasutajad, paroolid
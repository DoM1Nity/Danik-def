﻿from string import *
from time import *
from os import path, remove
from random import *

def registreerimine(kasutajad:list,paroolid:list)->any:
    """Kirjeldus
    :param list kasutajad: Kirjeldus
    :param list paroolid: Kirjeldus
    :rtype: list,list
    """
    while True:
        nimi=input("Mis on sinu nimi? ")
        if nimi not in kasutajad:
            while True:
                parool=input("Mis on sinu parool? ")
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
    """Funktsioon kuvab ekraanile "Tere tulemast!" kui kasutaja on olemas nimekirjas
        Nimi on järjendis kasutajad
        Salasõna on paroolide järjendis
        Nimi ja salasõna indeksid on võrdsed
    :param list kasutajad:...
    :param list paroolid:...
    """
    p=0
    while True:
        nimi=input("Sisesta kasutajanimi: ")              
        if nimi in kasutajad:            
            while True:
                parool=input("Sisesta salasõna: ")
                p+=1
                try:
                    if kasutajad.index(nimi)==paroolid.index(parool):
                        print(f"Tere tulemast! {nimi}")
                        break                  
                except:
                    print("Vale nimi või salasõna!")
                    if p==5:
                        print("Proovi uuesti 10 sek pärast")
                        for i in range(10):
                            sleep(1)
                            print(f"On jäänud {10-i} sek")
            break
        else:
            print("Kasutajat pole")
def nimi_või_parooli_muutmine(list_:list):
    """
    """
    muutuja=input("Vana nimi või parool: ")
    if muutuja in list_:
        indeks=list_.index(muutuja)
        muutuja=input("Uus nimi või parool: ")
        list_[indeks]=muutuja
    return list_

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

def loe_failist(fail:str)->list:
    """Funktsioon loeb tekst *.txt failist
    """
    f=open(fail,"r",encoding="utf-8")
    järjend=[]
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend

def kirjuta_failisse(fail:str,järjend=[]):
    """Salvestame tekst failisse
    """
    n=int(input("Mitu: "))
    for i in range(n):
        järjend.append(input(f"{i+1}. sõna: "))
    f=open(fail,'a',encoding="utf-8")
    for element in järjend:
        f.write(element+"\n")
    f.close()

def ümber_kirjuta_fail(fail:str):
    """
    """
    f=open(fail,'w')
    text=input("Sisesta tekst:")
    f.write(text+"\n")
    f.close()

def failide_kustutamine():
    """
    """
    failinimi=input("Mis fail tahad eemaldada?") #path.isdir("Kaust")
    if path.isfile(failinimi):
       remove(failinimi)
       print(f"Fail {failinimi} oli kustutatud")
    else:
        print(f"Fail {failinimi} puudub")

def loe_ankeet(fail:str)->any:
    """
    """
    fail=open(fail,"r",encoding="utf-8")
    kus=[]
    vas=[]
    for line in fail:
        n=line.find(":")  #разделить
        kus.append(line[0:n].strip())
        vas.append(line[n+1:len(line)].strip())
    fail.close()
    return kus,vas


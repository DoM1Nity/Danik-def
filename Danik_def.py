from OmaModul import *

salasõnad=["Parool.1"]
kasutajanimed=["Kasutajanimed.1"]
while True:
    print(kasutajanimed)
    print(salasõnad)
    print("1-registreerimine\n2-autoriseerimine\n3-nime või parooli muutmine\n4-unustanud üarooli taastamine\n5-lõpetamine")
    vastus=int(input("Sisestage arv "))
    if vastus==1:
        print("registreerimine")
        kasutajanimed,salasõnad=registreerimine(kasutajanimed,salasõnad)
    elif vastus==2:
        print("autoriseerimine")
        autoriseerimine(kasutajanimed,salasõnad)
    elif vastus==3:
        print("nime või parooli muutmine")
        vastus=input("Kas muudame nime või parooli ")
        if vastus=="nime":
            kasutajanimed=nime_või_parooli_muutmine(kasutajanimed)
        elif vastus=="parool":
            salasõnad==nime_või_parooli_muutmine(salasõnad)
        elif vastus=="mõlemad":
            kasutajanimed=nime_või_parooli_muutmine(kasutajanimed)
            salasõnad==nime_või_parooli_muutmine(salasõnad)
    elif vastus == 4:
        print("Unustanud üarooli taastamine")
        kasutajanimed, salasõnad = unustanud_üarooli_taastamine(kasutajanimed, salasõnad)
    elif vastus==5:
        print("lõpetamine")
        break
    else:
        print("Tundmatu valik")  

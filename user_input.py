def citeste_consum():   
#Daca exista debit
    numar_persoane = int(
        input(
            "Cate persoane sunt la locatie? "
        )
            )
    debit_necesar = float(
        input(
            "Debitul necesar//daca nu se stie, valoare este 0 (m3/ora): "
            )
        )
    if debit_necesar == 0:
        #In lipsa debitului
        numar_bai = int(
            input(
                "Cate bai sunt? "
            )
        )
        numar_bucatarii = int(
            input(
                "Cate bucatarii sunt? "
            )
        )
        numar_electrocasnice = int(
            input(
                "Cate electrocasnice sunt?(masini de spalat rufe, masini de spalat vase, altele...) "
            )
        )

    ntu = float(input("Turbiditate (NTU): "))

    prezenta_rezervor = input(
        "Este rezervor? DA/NU "
        ).strip().lower()
    if prezenta_rezervor == "da":
        
        volum_rezervor = float(
            input(
                        "Volumul rezervorului [m3]: "
                    )
                )
        
        durata_varf = float(
            input(
                        "Durata aproximativa a varfului [minute]: "
                    )
                )
    else:
        volum_rezervor = 0
        durata_varf = 0

        
    if debit_necesar == 0:
        return{
            "debit_necesar": 0,
            "persoane": numar_persoane,
            "bai": numar_bai,
            "bucatarii": numar_bucatarii,
            "electrocasnice": numar_electrocasnice,
            "volum_rezervor": volum_rezervor,
            "durata_varf": durata_varf,
            "ntu": ntu,
        }
    else:
        return {
            "debit_necesar": debit_necesar,
            "persoane": numar_persoane,
            "volum_rezervor": volum_rezervor,
            "durata_varf": durata_varf,
            "ntu": ntu
        }
    
def citeste_tip_filtrare():

    print("\nTip filtrare:")
    print("1. Filtru mecanic")
    print("2. Filtru automat cu zeolita")

    alegere = input("Alege: ")

    if alegere == "1":
        return "mecanic"

    elif alegere == "2":
        return "zeolita"

    else:
        print("Alegere invalida.")
        return citeste_tip_filtrare()


#Analize
#fe = float(input("Fier (mg/L): "))
#mn = float(input("Mangan (mg/L): "))
#nh4 = float(input("Amoniu (mg/L): "))
#duritate = float(input("duritate (dF): "))#se va adauga un calculator intre grade franceze si germane
#pH = float(input("pH (mg/L): "))
#no3 = float(input("Nitrati (mg/L): "))
#no2 = float(input("Nitriti (mg/L): "))

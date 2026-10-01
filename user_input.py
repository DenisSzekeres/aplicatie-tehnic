def citeste_consum():

    # =====================================================
    # TIP PROIECT
    # =====================================================

    print("\n==================================================")
    print("       DIMENSIONARE INSTALATIE TRATARE APA")
    print("==================================================")
    print("\nTip proiect:")
    print("1. Rezidential")
    print("2. Comercial / HoReCa")
    print("3. Industrial")
    print("4. Alt tip de consum")

    tip_alegere = input("Alege: ").strip()

    if tip_alegere == "1":
        tip_proiect = "rezidential"
    elif tip_alegere == "2":
        tip_proiect = "comercial"
    elif tip_alegere == "3":
        tip_proiect = "industrial"
    elif tip_alegere == "4":
        tip_proiect = "altul"
    else:
        print("Alegere invalida. Incearca din nou.")
        return citeste_consum()

    # =====================================================
    # DATE CONSUM
    # =====================================================

    numar_persoane = None

    if tip_proiect == "rezidential":
        numar_persoane = int(
            input("Cate persoane sunt la locatie? ")
        )

    print("\nCum determinam consumul zilnic?")
    print("1. Consum cunoscut [m3/zi]")
    print("2. Estimare din numarul de persoane")
    print("3. Nu este disponibil")

    mod_consum_alegere = input("Alege: ").strip()

    if mod_consum_alegere == "1":
        mod_consum = "consum_cunoscut"
        consum_zilnic = float(
            input("Consum zilnic [m3/zi]: ")
        )

    elif mod_consum_alegere == "2":
        if numar_persoane is None:
            print(
                "Pentru estimarea din persoane este necesar "
                "numarul de persoane."
            )
            return citeste_consum()

        mod_consum = "estimare_persoane"
        consum_zilnic = None

    elif mod_consum_alegere == "3":
        mod_consum = "necunoscut"
        consum_zilnic = None

    else:
        print("Alegere invalida. Incearca din nou.")
        return citeste_consum()

    # =====================================================
    # DEBIT
    # =====================================================

    debit_necesar = float(
        input(
            "Debitul necesar / daca nu se stie, valoarea este 0 "
            "(m3/ora): "
        )
    )

    # =====================================================
    # CONSUMATORI
    # =====================================================

    if debit_necesar == 0:

        numar_bai = int(
            input("Cate bai sunt? ")
        )

        numar_bucatarii = int(
            input("Cate bucatarii sunt? ")
        )

        numar_electrocasnice = int(
            input(
                "Cate electrocasnice sunt? "
                "(masini de spalat rufe, masini de spalat vase, altele...) "
            )
        )

    else:
        numar_bai = 0
        numar_bucatarii = 0
        numar_electrocasnice = 0

    # =====================================================
    # APA
    # =====================================================

    ntu = float(
        input("Turbiditate (NTU): ")
    )

    duritate = float(
        input("Duritatea apei (°HF): ")
    )

    # =====================================================
    # REZERVOR
    # =====================================================

    prezenta_rezervor = input(
        "Este rezervor? DA/NU "
    ).strip().lower()

    if prezenta_rezervor == "da":

        volum_rezervor = float(
            input("Volumul rezervorului [m3]: ")
        )

        durata_varf = float(
            input("Durata aproximativa a varfului [minute]: ")
        )

        ore_reumplere_rezervor = float(
            input("In cate ore doriti sa se reumple rezervorul? ")
        )

    else:
        volum_rezervor = 0
        durata_varf = 0
        ore_reumplere_rezervor = 24

    # =====================================================
    # RETURN
    # =====================================================

    return {
        "tip_proiect": tip_proiect,
        "persoane": numar_persoane,
        "mod_consum": mod_consum,
        "consum_zilnic": consum_zilnic,

        "debit_necesar": debit_necesar,

        "bai": numar_bai,
        "bucatarii": numar_bucatarii,
        "electrocasnice": numar_electrocasnice,

        "volum_rezervor": volum_rezervor,
        "durata_varf": durata_varf,
        "ore_reumplere_rezervor": ore_reumplere_rezervor,

        "ntu": ntu,
        "duritate": duritate,
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


def afisare_date_debite(rezultat):

    print("\n========== REZULTAT CALCUL DEBIT ==========")

    if rezultat["n"] is not None:

        print(f"Numar consumatori: {rezultat['n']}")
        print(f"Debit instalat: {rezultat['debit_instalat']} m3/h")
        print(f"Coeficient simultaneitate: {rezultat['coeficient']}")
        print(f"Debit simultan: {rezultat['debit_simultan']} m3/h")

    print(f"Debit necesar: {rezultat['debit_necesar']} m3/h")

    if rezultat["volum_rezervor"] > 0:

        print("\n---------- REZERVOR TAMPON ----------")

        print(
            f"Volum rezervor: "
            f"{rezultat['volum_rezervor']} m3"
        )

        print(
            f"Durata varf: "
            f"{rezultat['durata_varf']} minute"
        )

        print(
            f"Debit proiect cu rezervor: "
            f"{rezultat['debit_proiect']} m3/h"
        )

    else:

        print("\nNu exista rezervor tampon.")

        print(
            f"Debit proiect: "
            f"{rezultat['debit_proiect']} m3/h"
        )

    print("==========================================")


def afiseaza_rezultat_filtrare(rezultat):

    print("\n========== REZULTAT FILTRARE ==========")

    if rezultat["status"] != "ok":

        print(rezultat["mesaj"])
        print("========================================")
        return

    filtru = rezultat["rezultat"]

    print(f"\nTurbiditate:         {rezultat['ntu']} NTU")
    print(f"Debit proiect:       {filtru['debit_proiect']} m3/h")

    print("\n---------- FILTRU RECOMANDAT ----------")

    print(f"Echipament:          {filtru['echipament']}")
    print(f"Model:               {filtru['model']}")

    # ---------------------------------
    # CINTROPUR
    # ---------------------------------

    if "debit_filtru" in filtru:

        print(f"Debit filtru:        {filtru['debit_filtru']} m3/h")
        print(f"Rezerva:             {filtru['rezerva_procent']} %")
        print(f"Racord:              {filtru['racord']}")
        
    # ---------------------------------
    # ZEOLITA
    # ---------------------------------

    elif "viteza_filtrare" in filtru:

        print(f"Viteza filtrare:     {filtru['viteza_filtrare']} m/h")
        print(f"Debit filtrare:      {filtru['debit_filtrare']} m3/h")
        print(f"Rezerva:             {filtru['rezerva_procent']} %")
        print(f"Dimensiune:          {filtru['butelie']}")
        print(f"Racord:              {filtru['racord']}")
        print(f"Zeolit:              {filtru['zeolit_l']} L")
        print(f"Zeolit:              {filtru['zeolit_kg']} kg")

        print(
            f"Debit spalare:       "
            f"{filtru['debit_spalare']} m3/h"
        )

    # ---------------------------------
    # OBSERVATIE
    # ---------------------------------

    if "observatie" in filtru:

        print("\nObservatie:")
        print(filtru["observatie"])

    print("========================================")
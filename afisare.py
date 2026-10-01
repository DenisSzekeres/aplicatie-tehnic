
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

def afiseaza_rezultat_dedurizare(rezultat):

    print("\n========== REZULTAT DEDURIZARE ==========")

    if rezultat.get("status") != "ok":
        print(rezultat.get("mesaj", "Nu a fost gasit un echipament."))
        print("=========================================")
        return

    r = rezultat["rezultat"]

    print(f"Model:               {r.get('model')}")
    print(f"Debit proiect:       {r.get('debit_proiect')} m3/h")

    if "debit_lucru" in r:
        print(f"Debit lucru:         {r.get('debit_lucru')} m3/h")
        print(f"Debit varf:          {r.get('debit_varf')} m3/h")
        print(f"Regim debit:         {r.get('regim_debit')}")

    if "disc" in r:
        print(f"Disc duritate:       {r.get('disc')}")
        print(f"Duritate disc:       {r.get('duritate_disc_hf')} °HF")
        print(f"Capacitate:          {r.get('capacitate_intre_regenerari_l')} L")
        print(f"Regenerari/zi:       {r.get('regenerari_zi')}")
        print(f"Zile intre regenerari: {r.get('zile_intre_regenerari')}")

    if "capacitate_echipament_hf_m3" in r:
        print(f"Configuratie:        {r.get('configuratie')}")
        print(f"Mod dimensionare:    {r.get('mod_dimensionare_debit')}")
        print(f"Debit maxim:         {r.get('debit_maxim')} m3/h")
        print(f"Capacitate:          {r.get('capacitate_echipament_hf_m3')} °HF x m3")
        print(f"Rezerva capacitate:  {r.get('rezerva_capacitate_procent')} %")
        print(f"Zile intre regenerari: {r.get('zile_intre_regenerari')}")

    if "debit_echipament" in r:
        print(f"Debit echipament:    {r.get('debit_echipament')} m3/h")
        print(f"Capacitate:          {r.get('capacitate_intre_regenerari_l')} L")
        print(f"Regenerari/zi:       {r.get('regenerari_zi')}")

    if "observatie" in r:
        print(f"\nObservatie: {r['observatie']}")

    print("=========================================")

import math
import database
#Calculare grade franceze in germane sau invers
def calculeaza_numar_consumatori(date):
    n = (
        date["electrocasnice"] 
        + date["bai"] 
        + date["bucatarii"])
    return n

def calculeaza_coeficient(date): 
    n = calculeaza_numar_consumatori(date)
    if n <= 1:
        k_simultan = 1
    else:
        k_simultan = max(database.K_MINIM, (round(1/math.sqrt(n-1),2)))
    return k_simultan
    #print(k_simultan)

def calculeaza_debit_instalat (date): 
    n = calculeaza_numar_consumatori(date)   
    debit_bai = database.DEBIT["baie"] * date["bai"]
    #print(debit_bai)
    debit_bucatarie = database.DEBIT["bucatarie"] * date["bucatarii"]
    #print(debit_bucatarie)
    debit_electrocasnice = database.DEBIT["electrocasnice"] * date["electrocasnice"]
    #print(debit_electrocasnice)
    debit_instalat = debit_electrocasnice + debit_bucatarie + debit_bai
    return debit_instalat
    #print(debit_calculat)

def calculeaza_debit_simultan(date):
    debit_instalat = calculeaza_debit_instalat(date)
    coeficient = calculeaza_coeficient(date)

    debit_simultan = round(debit_instalat * coeficient , 2)

    return debit_simultan

def calculeaza_debit_proiect_cu_rezervor(
        debit_necesar, 
        volum_rezervor, 
        durata_varf
    ):
    if volum_rezervor <= 0:
        return debit_necesar
    durata_ore = durata_varf/60
    debit_rezervor = volum_rezervor/durata_ore
    debit_proiect = debit_necesar - debit_rezervor
    debit_proiect = max(database.K_MINIM, debit_proiect)
    return round(debit_proiect,2)

def calculeaza_filtrare(debit_proiect, tip_filtrare, ntu):

    if tip_filtrare == "mecanic":
        return cauta_filtru_mecanic(debit_proiect)

    elif tip_filtrare == "zeolita":
        return cauta_filtru_zeolita(debit_proiect, ntu)

    else:
        return {
            "status": "eroare",
            "mesaj": "Tip de filtrare necunoscut."
        }


def cauta_filtru_mecanic(debit_proiect):
    """
    Cauta filtrele mecanice care pot asigura debitul proiect.
    """
    rezultate = []

    echipamente = database.ECHIPAMENTE_SEDIMENTE

    for nume_echipament, date_echipament in echipamente.items():

        if date_echipament["tip_filtrare"] != "mecanic":
            continue

        for model, date_model in date_echipament["modele"].items():

            if date_model["debit_maxim"] >= debit_proiect:

                rezultate.append({
                    "echipament": date_echipament["nume"],
                    "model": model,
                    "debit_proiect": debit_proiect,
                    "debit_maxim": date_model["debit_maxim"],
                    "racord": date_model.get("racord")
                })

    if not rezultate:

        return {
            "status": "negasit",
            "mesaj": "Nu exista un filtru mecanic pentru debitul proiect."
        }

    rezultate.sort(key=lambda x: x["debit_maxim"])

    return {
        "status": "ok",
        "rezultate": rezultate
    }

def cauta_filtru_zeolita(debit_proiect, ntu):

    zeolita = database.ECHIPAMENTE_SEDIMENTE["zeolita_automata"]

    # Stabilim viteza preferata in functie de NTU
    if ntu < 0.5:
        viteze_de_incercat = [50, 40, 30]

    elif ntu < 5:
        viteze_de_incercat = [40, 30]

    else:
        viteze_de_incercat = [30]

    # Rezerva maxima dorita
    debit_maxim_acceptat = round(debit_proiect * 1.10, 2)

    variante_recomandate = []
    variante_posibile = []

    for viteza in viteze_de_incercat:

        for model, date_model in zeolita["modele"].items():

            debit_filtrare = date_model["debit_la_viteza"].get(viteza)

            if debit_filtrare is None:
                continue

            # Filtrul trebuie sa poata asigura debitul proiect
            if debit_filtrare < debit_proiect:
                continue

            rezerva = (
                (debit_filtrare - debit_proiect)
                / debit_proiect
            ) * 100

            varianta = {
                "echipament": zeolita["nume"],
                "model": model,
                "debit_proiect": debit_proiect,
                "ntu": ntu,
                "viteza_filtrare": viteza,
                "debit_filtrare": debit_filtrare,
                "rezerva_procent": round(rezerva, 1),
                "debit_spalare": date_model["debit_spalare_m3_h"],
                "suprafata_filtranta_m2": date_model["suprafata_filtranta_m2"],
                "racord": date_model["racord"],
                "bautela": date_model["butelie"],
                "zeolit_l": date_model["zeolit_l"],
                "zeolit_kg": date_model["zeolit_kg"]
            }

            # Varianta respecta rezerva de maximum 10%
            if debit_filtrare <= debit_maxim_acceptat:
                variante_recomandate.append(varianta)

            # Orice varianta care poate asigura debitul
            variante_posibile.append(varianta)

        # Daca avem variante in limita de 10%,
        # ne oprim la viteza preferata.
        if variante_recomandate:
            break

    # ==========================================
    # CAZUL 1: AVEM VARIANTA CU REZERVA <= 10%
    # ==========================================

    if variante_recomandate:

        variante_recomandate.sort(
            key=lambda x: x["rezerva_procent"]
        )

        rezultat = variante_recomandate[0]

        rezultat["observatie"] = (
            "Varianta respecta rezerva maxima de 10%."
        )

        return {
            "status": "ok",
            "rezultat": rezultat
        }

    # ==========================================
    # CAZUL 2: NU AVEM REZERVA <= 10%
    # ALEGEM CEL MAI MIC FILTRU POSIBIL
    # ==========================================

    if variante_posibile:

        variante_posibile.sort(
            key=lambda x: x["debit_filtrare"]
        )

        rezultat = variante_posibile[0]

        rezultat["observatie"] = (
            "Nu exista o varianta cu rezerva de maximum 10%. "
            "A fost ales cel mai mic model disponibil "
            "care poate asigura debitul proiect."
        )

        return {
            "status": "ok",
            "rezultat": rezultat
        }

    # ==========================================
    # CAZUL 3: NICIUN FILTRU NU POATE ASIGURA DEBITUL
    # ==========================================

    return {
        "status": "negasit",
        "mesaj": (
            "Nu exista un filtru cu zeolita care sa poata "
            "asigura debitul proiect."
        )
    }





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
        rezultat = cauta_filtru_mecanic(debit_proiect)

    elif tip_filtrare == "zeolita":
        rezultat = cauta_filtru_zeolita(debit_proiect, ntu)

    else:
        return {
            "status": "eroare",
            "mesaj": "Tip de filtrare necunoscut."
        }

    # NTU este o informatie generala despre apa,
    # nu doar despre filtrarea cu zeolita.
    rezultat["ntu"] = ntu

    return rezultat


def cauta_filtru_mecanic(debit_proiect):

    rezultate = []

    echipamente = database.ECHIPAMENTE_SEDIMENTE

    for nume_echipament, date_echipament in echipamente.items():

        if date_echipament.get("tip_filtrare") != "mecanic":
            continue

        if "modele" not in date_echipament:
            continue

        for model, date_model in date_echipament["modele"].items():

            debit_filtru = date_model.get("debit_serviciu")

            if debit_filtru is None:
                continue

            if debit_filtru < debit_proiect:
                continue

            rezerva = (
                (debit_filtru - debit_proiect)
                / debit_proiect
            ) * 100

            rezultate.append({
                "echipament": date_echipament["nume"],
                "model": model,
                "debit_proiect": debit_proiect,
                "debit_filtru": debit_filtru,
                "rezerva_procent": round(rezerva, 1),
                "racord": date_model.get("racord"),
                "suprafata_filtrare": date_model.get(
                    "suprafata_filtrare"
                )
            })

    if not rezultate:

        return {
            "status": "negasit",
            "mesaj": (
                "Nu exista un filtru mecanic "
                "pentru debitul proiect."
            )
        }

    # Cel mai mic debit de serviciu care acopera debitul proiect
    rezultate.sort(
        key=lambda x: x["debit_filtru"]
    )

    return {
        "status": "ok",
        "rezultat": rezultate[0]
    }

def cauta_filtru_zeolita(debit_proiect, ntu):

    zeolita = database.ECHIPAMENTE_SEDIMENTE["zeolita_automata"]

    # ============================================================
    # VITEZA DE FILTRARE IN FUNCTIE DE NTU
    # ============================================================

    if ntu < 0.5:
        viteza_filtrare = 50

    elif ntu < 5:
        viteza_filtrare = 40

    elif ntu < 10:
        viteza_filtrare = 30

    else:
        return {
            "status": "negasit",
            "mesaj": (
                "NTU >= 10. Pentru acest interval este necesara "
                "o alta strategie de tratare (floculare/decantare)."
            )
        }

    # ============================================================
    # CAUTAM CEL MAI MIC MODEL CARE ACOPERA DEBITUL
    # LA VITEZA IMPUSA DE NTU
    # ============================================================

    variante_posibile = []

    for model, date_model in zeolita["modele"].items():

        debit_filtrare = date_model["debit_la_viteza"].get(
            viteza_filtrare
        )

        if debit_filtrare is None:
            continue

        if debit_filtrare < debit_proiect:
            continue

        # ========================================================
        # REZERVA DE DEBIT
        # ========================================================

        if debit_proiect > 0:
            rezerva = (
                (debit_filtrare - debit_proiect)
                / debit_proiect
            ) * 100
        else:
            rezerva = 0

        varianta = {
            "echipament": zeolita["nume"],
            "model": model,
            "debit_proiect": debit_proiect,
            "viteza_filtrare": viteza_filtrare,
            "debit_filtrare": debit_filtrare,
            "rezerva_procent": round(rezerva, 1),

            "debit_spalare": date_model[
                "debit_spalare_m3_h"
            ],

            "suprafata_filtranta_m2": date_model[
                "suprafata_filtranta_m2"
            ],

            "racord": date_model["racord"],
            "butelie": date_model["butelie"],
            "zeolit_l": date_model["zeolit_l"],
            "zeolit_kg": date_model["zeolit_kg"]
        }

        variante_posibile.append(varianta)

    # ============================================================
    # ALEGEM CEL MAI MIC ECHIPAMENT DISPONIBIL
    # ============================================================

    if not variante_posibile:
        return {
            "status": "negasit",
            "mesaj": (
                "Nu exista un filtru cu zeolita care sa poata "
                "asigura debitul proiect la viteza de filtrare "
                "impusa de NTU."
            )
        }

    # Cel mai mic debit disponibil care acopera proiectul
    variante_posibile.sort(
        key=lambda x: x["debit_filtrare"]
    )

    rezultat = variante_posibile[0]

    rezultat["observatie"] = (
        f"Viteza de filtrare stabilita automat la "
        f"{viteza_filtrare} m/h in functie de NTU. "
        f"A fost ales cel mai mic model disponibil "
        f"care poate asigura debitul proiect."
    )

    return {
        "status": "ok",
        "rezultat": rezultat
    }
# ============================================================
# DEDURIZATOARE
# ============================================================

def calculeaza_consum_zilnic(date):
    """
    Stabileste consumul zilnic in m3/zi.

    Daca este introdus consumul real, acesta are prioritate.
    Daca nu exista, folosim numarul de persoane.
    """

    if date.get("consum_zilnic") is not None:
        return date["consum_zilnic"]

    if date.get("persoane") is not None:
        # Valoare provizorie.
        # O vom muta ulterior in database.py.
        consum_persoana = 0.15

        return round(
            date["persoane"] * consum_persoana,
            2
        )

    return None


def calculeaza_necesar_dedurizare(
        consum_zilnic,
        duritate,
        regenerari_pe_zi
    ):
    """
    Calculeaza incarcarea de duritate intre doua regenerari.

    Rezultatul este exprimat in °HF x m3.
    """

    if consum_zilnic <= 0:
        raise ValueError(
            "Consumul zilnic trebuie sa fie mai mare decat 0."
        )

    if duritate <= 0:
        raise ValueError(
            "Duritatea trebuie sa fie mai mare decat 0."
        )

    if regenerari_pe_zi <= 0:
        raise ValueError(
            "Numarul de regenerari pe zi trebuie sa fie "
            "mai mare decat 0."
        )

    necesar = (
        consum_zilnic
        * duritate
        / regenerari_pe_zi
    )

    return round(necesar, 2)


def verifica_debit_dedurizator(echipament, debit_proiect):
    """
    Verifica debitul necesar fata de debitul de lucru
    si debitul de varf al echipamentului.
    """

    debit_lucru = echipament.get("debit_lucru_m3_h")
    debit_varf = echipament.get("debit_varf_m3_h")

    if debit_lucru is None:
        return {
            "ok": False,
            "tip": "necunoscut"
        }

    # Functionare normala
    if debit_proiect <= debit_lucru:
        return {
            "ok": True,
            "tip": "debit_lucru"
        }

    # Debit proiect peste debitul de lucru,
    # dar in limita debitului de varf
    if debit_varf is not None and debit_proiect <= debit_varf:
        return {
            "ok": True,
            "tip": "debit_varf"
        }

    return {
        "ok": False,
        "tip": "depasit"
    }


def verifica_duritate_dedurizator(
        echipament,
        duritate
    ):
    """
    Verifica duritatea maxima admisa de echipament.
    """

    duritate_maxima = echipament.get(
        "duritate_maxima_hf"
    )

    if duritate_maxima is None:
        return False

    return duritate <= duritate_maxima


# ============================================================
# ERGO 11
# ============================================================

def cauta_ergo_11(
        consum_zilnic,
        duritate,
        debit_proiect
    ):

    ergo = database.DEDURIZATOARE[
        "kinetico_ergo_11"
    ]

    # Verificare debit
    if not verifica_debit_dedurizator(
        ergo,
        debit_proiect
    ):
        return None

    # Verificare duritate
    verificare_debit = verifica_debit_dedurizator(
    ergo,
    debit_proiect
)

    if not verificare_debit["ok"]:
        return None

    # Tabelul producatorului
    tabel = ergo[
        "capacitate_litri_duritate"
    ]

    # Alegem valoarea corespunzatoare
    # urmatoarei duritati disponibile
    duritati = sorted(tabel.keys())

    capacitate_litri = None

    for valoare in duritati:

        if duritate <= valoare:
            capacitate_litri = tabel[valoare]
            break

    if capacitate_litri is None:
        return None

    capacitate_m3 = capacitate_litri / 1000

    # Consum zilnic raportat la volumul disponibil
    regenerari_zi = consum_zilnic / capacitate_m3

    regenerari_max = ergo.get(
        "regenerari_max_pe_zi"
    )

    if regenerari_max is not None:
        if regenerari_zi > regenerari_max:
            return None

    return {
        "model": ergo["nume"],
        "cod": "kinetico_ergo_11",

        "debit_proiect": debit_proiect,
        "debit_echipament": ergo[
            "debit_lucru_m3_h"
        ],

        "duritate": duritate,

        "capacitate_intre_regenerari_l":
            capacitate_litri,

        "capacitate_intre_regenerari_m3":
            capacitate_m3,

        "regenerari_zi":
            round(regenerari_zi, 2),

        "sare_regenerare_kg":
            ergo["sare_regenerare_kg"],

        "apa_regenerare_l":
            ergo["apa_regenerare_l"],

        "observatie":
            "ERGO 11 poate acoperi debitul si "
            "necesarul calculat."
    }


# ============================================================
# KINETICO 2030
# ============================================================

def cauta_2030(
        consum_zilnic,
        duritate,
        debit_proiect
    ):

    model = database.DEDURIZATOARE[
        "kinetico_2030"
    ]

    # Verificare debit
    if not verifica_debit_dedurizator(
        model,
        debit_proiect
    ):
        return None

    # Verificare duritate
    verificare_debit = verifica_debit_dedurizator(
    model,
    debit_proiect
)

    if not verificare_debit["ok"]:
        return None

    discuri = model[
        "discuri_duritate"
    ]

    # Alegem discul corespunzator duritatii.
    disc_ales = None

    for nume_disc, date_disc in discuri.items():

        if duritate <= date_disc["duritate_hf"]:

            disc_ales = {
                "nume": nume_disc,
                "duritate_hf":
                    date_disc["duritate_hf"],
                "litri":
                    date_disc[
                        "litri_intre_regenerari"
                    ]
            }

            break

    if disc_ales is None:
        return None

    capacitate_m3 = (
        disc_ales["litri"] / 1000
    )

    regenerari_zi = (
        consum_zilnic / capacitate_m3
    )

    # Stabilim regimul de debit utilizat

    if debit_proiect <= model["debit_lucru_m3_h"]:

        regim_debit = "debit de lucru"

    else:

        regim_debit = "debit de varf"


    # Timpul estimat intre doua regenerari

    zile_intre_regenerari = (
        capacitate_m3 / consum_zilnic
    )


    return {
        "model": model["nume"],
        "cod": "kinetico_2030",

        "debit_proiect": debit_proiect,

        "debit_lucru": model[
            "debit_lucru_m3_h"
        ],

        "debit_varf": model[
            "debit_varf_m3_h"
        ],

        "regim_debit": regim_debit,

        "duritate": duritate,

        "disc": disc_ales["nume"],

        "duritate_disc_hf":
            disc_ales["duritate_hf"],

        "capacitate_intre_regenerari_l":
            disc_ales["litri"],

        "capacitate_intre_regenerari_m3":
            capacitate_m3,

        "regenerari_zi":
            round(regenerari_zi, 2),

        "zile_intre_regenerari":
            round(zile_intre_regenerari, 2),

        "observatie":
            "MACH 2030 selectat in functie de "
            "duritate, consum si debit."
    }

# ============================================================
# WATERMARK
# ============================================================
def cauta_watermark(
        consum_zilnic,
        duritate,
        debit_proiect
    ):

    watermark = database.DEDURIZATOARE

    rezultate_finale = []

    # ========================================================
    # CAPACITATEA MINIMA NECESARA
    # ========================================================

    capacitate_necesara = (
        consum_zilnic
        * duritate
        * database.ZILE_MINIME_WATERMARK
    )

    # ========================================================
    # ORDINEA CONFIGURATIILOR
    # ========================================================

    configuratii_disponibile = [
    "simplex",
    "duplex",
    "triplex",
    "cuadruplex"
]

    # ========================================================
    # PARCURGEM CONFIGURATIILE
    # ========================================================

    for configuratie_cautata in configuratii_disponibile:

        rezultate_configuratie = []

        for cod_familie, familie in watermark.items():

            # ------------------------------------------------
            # Doar echipamente WaterMark
            # ------------------------------------------------

            if familie.get("producator") != "WaterMark":
                continue

            # ------------------------------------------------
            # Verificam configuratia
            # ------------------------------------------------

            if familie.get(
                "configuratie_sistem"
            ) != configuratie_cautata:
                continue

            if "modele" not in familie:
                continue

            # =================================================
            # PARCURGEM MODELELE
            # =================================================

            for cod_model, model in familie["modele"].items():

                # =================================================
                # DEBIT DIN CATALOG
                # =================================================

                debit = model.get(
                    "debit_lucru_m3_h"
                )

                # Unele familii nu au debitul in model.
                # In acest caz folosim debitul nominal
                # al familiei.

                if debit is None:

                    debit = familie.get(
                        "debit_nominal_m3_h"
                    )

                # Daca nu avem niciun debit cunoscut,
                # modelul nu poate fi dimensionat.

                if debit is None:
                    continue

                # =================================================
                # INTERVAL SAU VALOARE SIMPLA
                # =================================================

                if isinstance(debit, tuple):

                    debit_minim_catalog = debit[0]
                    debit_maxim_catalog = debit[1]

                else:

                    debit_minim_catalog = None
                    debit_maxim_catalog = debit

                # =================================================
                # DEBIT EFECTIV IN FUNCTIONARE ALTERNATIVA
                # =================================================

                debit_minim = calculeaza_debit_watermark(
                    familie,
                    model,
                    debit_minim_catalog
                )

                debit_maxim = calculeaza_debit_watermark(
                    familie,
                    model,
                    debit_maxim_catalog
                )

                # Daca nu avem debit maxim calculabil,
                # nu putem folosi modelul.

                if debit_maxim is None:
                    continue

                # =================================================
                # VERIFICARE DEBIT PROIECT
                # =================================================

                if debit_proiect > debit_maxim:
                    continue

                # =================================================
                # REGIM DEBIT
                # =================================================

                if debit_minim is not None:

                    if debit_proiect >= debit_minim:
                        regim_debit = "debit de lucru"
                    else:
                        regim_debit = "sub debitul minim"

                else:

                    regim_debit = "debit de lucru"

                # =================================================
                # CAPACITATI
                # =================================================

                capacitati = model.get(
                    "capacitati"
                )

                if capacitati is None:

                    capacitati = model.get(
                        "capacitati_paralel"
                    )

                if capacitati is None:
                    continue

                configuratii_capacitate = []

                # =================================================
                # VERIFICAM CAPACITATILE
                # =================================================

                for (
                    nume_configuratie,
                    date_configuratie
                ) in capacitati.items():

                    capacitate = date_configuratie.get(
                        "capacitate_hf_m3"
                    )

                    if capacitate is None:
                        continue

                    # Capacitatea trebuie sa acopere
                    # necesarul pentru minimum 2 zile.

                    if capacitate < capacitate_necesara:
                        continue

                    # =================================================
                    # ZILE INTRE REGENERARI
                    # =================================================

                    consum_duritate = (
                        consum_zilnic
                        * duritate
                    )

                    if consum_duritate > 0:

                        zile = (
                            capacitate
                            / consum_duritate
                        )

                    else:

                        zile = 0

                    configuratii_capacitate.append({

                        "configuratie":
                            nume_configuratie,

                        "capacitate_hf_m3":
                            capacitate,

                        "sare_kg":
                            date_configuratie.get(
                                "sare_kg"
                            ),

                        "zile_intre_regenerari":
                            round(
                                zile,
                                2
                            )
                    })

                # =================================================
                # NU EXISTA CAPACITATE SUFICIENTA
                # =================================================

                if not configuratii_capacitate:
                    continue

                # =================================================
                # ALEGEM CEA MAI MICA CAPACITATE SUFICIENTA
                # =================================================

                configuratii_capacitate.sort(
                    key=lambda x:
                        x["capacitate_hf_m3"]
                )

                configuratie_aleasa = (
                    configuratii_capacitate[0]
                )

                # =================================================
                # FACTOR ALTERNATIV
                # =================================================

                factor_alternativ = model.get(
                    "factor_sistem_alternativ"
                )

                if factor_alternativ is None:

                    factor_alternativ = familie.get(
                        "factor_sistem_alternativ",
                        1.0
                    )

                # =================================================
                # REZULTAT
                # =================================================

                rezultat = {

                    "model": model.get(
                        "model",
                        cod_model
                    ),

                    "cod": cod_model,

                    "familie": familie.get(
                        "nume"
                    ),

                    "configuratie_sistem":
                        configuratie_cautata,

                    "mod_dimensionare_debit":
                        familie.get(
                            "mod_dimensionare_debit",
                            "normal"
                        ),


                    "mod_functionare":
                        database.MOD_FUNCTIONARE_WATERMARK,

                    "debit_proiect":
                        debit_proiect,

                    "debit_minim":
                        debit_minim,

                    "debit_maxim":
                        debit_maxim,

                    "debit_catalog_minim":
                        debit_minim_catalog,

                    "debit_catalog_maxim":
                        debit_maxim_catalog,

                    "factor_alternativ":
                        factor_alternativ,

                    "regim_debit":
                        regim_debit,

                    "consum_zilnic":
                        consum_zilnic,

                    "duritate":
                        duritate,

                    "capacitate_necesara_hf_m3":
                        round(
                            capacitate_necesara,
                            2
                        ),

                    "configuratie":
                        configuratie_aleasa[
                            "configuratie"
                        ],

                    "capacitate_echipament_hf_m3":
                        configuratie_aleasa[
                            "capacitate_hf_m3"
                        ],

                    "sare_regenerare_kg":
                        configuratie_aleasa[
                            "sare_kg"
                        ],

                    "zile_intre_regenerari":
                        configuratie_aleasa[
                            "zile_intre_regenerari"
                        ],

                    "resina_l":
                        model.get(
                            "resina_l",
                            model.get(
                                "resina_l_total"
                            )
                        ),

                    "resina_l_total":
                        model.get(
                            "resina_l_total"
                        ),

                    "numar_coloane":
                        model.get(
                            "numar_coloane"
                        ),

                    "butelie":
                        model.get(
                            "butelie"
                        ),

                    "racord":
                        model.get(
                            "racord",
                            familie.get(
                                "racord"
                            )
                        ),

                    "pret_euro":
                        model.get(
                            "pret_euro"
                        )
                }

                # =================================================
                # REZERVA DE CAPACITATE
                # =================================================

                if capacitate_necesara > 0:

                    rezultat[
                        "rezerva_capacitate_procent"
                    ] = round(
                        (
                            (
                                rezultat[
                                    "capacitate_echipament_hf_m3"
                                ]
                                - capacitate_necesara
                            )
                            / capacitate_necesara
                        ) * 100,
                        1
                    )

                else:

                    rezultat[
                        "rezerva_capacitate_procent"
                    ] = 0

                # Adaugam rezultatul pentru configuratia
                # curenta.

                rezultate_configuratie.append(
    rezultat
)
        # ========================================================
        # DACA AVEM UN REZULTAT IN CONFIGURATIA CURENTA
        # NE OPRIM
        # ========================================================

        # ========================================================
        # ========================================================
        # DACA AVEM REZULTATE IN CONFIGURATIA CURENTA
        # LE PASTRAM SI CONTINUAM CU URMATOAREA CONFIGURATIE
        # ========================================================

        if rezultate_configuratie:

            # Alegem cel mai mic model suficient
            # din configuratia curenta.

            rezultate_configuratie.sort(
                key=lambda x: (
                    x["debit_maxim"]
                    if x["debit_maxim"] is not None
                    else float("inf"),

                    x["capacitate_echipament_hf_m3"]
                )
            )

            rezultat_configuratie = rezultate_configuratie[0]

            rezultat_configuratie["observatie"] = (
                "WaterMark disponibil pentru "
                "functionare alternativa, "
                "in functie de debit si capacitatea "
                "necesara pentru minimum "
                f"{database.ZILE_MINIME_WATERMARK} zile."
            )

            rezultate_finale.append(
                rezultat_configuratie
            )

    # ========================================================
    # DACA AVEM CEL PUTIN O VARIANTA
    # ========================================================

    if rezultate_finale:

        return {
            "status": "ok",
            "rezultate": rezultate_finale,
            "rezultat": rezultate_finale[0]
        }

    # ========================================================
    # NICIUN ECHIPAMENT GASIT
    # ========================================================

    return {
        "status": "negasit",
        "mesaj": (
            "Niciun dedurizator WaterMark nu poate "
            "acoperi debitul si capacitatea necesara "
            "pentru minimum "
            f"{database.ZILE_MINIME_WATERMARK} zile."
        )
    }

def calculeaza_debit_watermark(
        familie,
        model,
        debit_catalog
    ):

    # Daca nu exista debit catalog,
    # nu putem calcula debitul efectiv.
    if debit_catalog is None:
        return None

    # Modul de dimensionare este stabilit
    # in baza de date pentru fiecare familie:
    #
    # normal     -> folosim debitul din catalog
    # alternativ -> aplicam factorul sistemului alternativ
    # paralel    -> folosim debitul din catalog
    mod_dimensionare = familie.get(
        "mod_dimensionare_debit",
        "normal"
    )

    # SIMPLEX / sistem normal
    if mod_dimensionare == "normal":
        return debit_catalog

    # TRIPLEX / sistem dimensionat in paralel
    if mod_dimensionare == "paralel":
        return debit_catalog

    # DUPLEX si CUADRUPLEX / sistem alternativ
    if mod_dimensionare == "alternativ":
        factor = model.get(
            "factor_sistem_alternativ"
        )

        if factor is None:
            factor = familie.get(
                "factor_sistem_alternativ",
                1.0
            )

        return round(
            debit_catalog * factor,
            2
        )

    # Daca apare un mod necunoscut,
    # nu aplicam automat o formula gresita.
    raise ValueError(
        f"Mod de dimensionare WaterMark necunoscut: "
        f"{mod_dimensionare}"
    )

def calculeaza_dedurizator(date):
    """
    Alege dedurizatorul potrivit.

    Ordinea de alegere:

    1. ERGO 11
    2. Kinetico MACH 2030
    3. WaterMark

    Debit_proiect este obligatoriu.
    Duritatea este obligatorie.
    Consumul zilnic este calculat din datele introduse.
    """

    if date.get("debit_proiect") is None:
        raise ValueError(
            "Debit_proiect este necesar pentru "
            "dimensionarea dedurizatorului."
        )

    if date.get("duritate") is None:
        raise ValueError(
            "Duritatea apei este necesara pentru "
            "dimensionarea dedurizatorului."
        )

    consum_zilnic = calculeaza_consum_zilnic(date)

    if consum_zilnic is None:
        raise ValueError(
            "Introdu consumul zilnic sau numarul "
            "de persoane."
        )

    debit_proiect = date["debit_proiect"]
    duritate = date["duritate"]


    # ========================================================
    # 1. ERGO 11
    # ========================================================

    rezultat_ergo = cauta_ergo_11(
        consum_zilnic,
        duritate,
        debit_proiect
    )

    if rezultat_ergo is not None:

        return {
            "status": "ok",
            "rezultat": rezultat_ergo
        }


    # ========================================================
    # 2. KINETICO MACH 2030
    # ========================================================

    rezultat_2030 = cauta_2030(
        consum_zilnic,
        duritate,
        debit_proiect
    )

    if rezultat_2030 is not None:

        return {
            "status": "ok",
            "rezultat": rezultat_2030
        }


    # ========================================================
    # 3. WATERMARK
    # ========================================================

    rezultat_watermark = cauta_watermark(
        consum_zilnic,
        duritate,
        debit_proiect
    )

    if rezultat_watermark["status"] == "ok":

        return rezultat_watermark


    # ========================================================
    # NICIUN REZULTAT
    # ========================================================

    return {
        "status": "negasit",
        "mesaj": (
            "Niciun dedurizator disponibil nu poate "
            "acoperi debitul si necesarul calculat."
        )
    }




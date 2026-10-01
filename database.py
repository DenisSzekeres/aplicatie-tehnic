# database.py
# Baza de date pentru aplicatia de dimensionare a echipamentelor de tratare a apei.
# Valorile WaterMark de mai jos sunt preluate din catalogul Ionfilter, pag. 109-129.
# Terminologia este tradusa in romana.
#
# IMPORTANT:
# - capacitatile sunt exprimate in °HF x m3;
# - consumul de sare este kg NaCl / regenerare;
# - debitele sunt m3/h;
# - preturile sunt P.V.R. EUR din catalog;
# - pentru MTS, capacitatile din catalog sunt pentru functionare in paralel.
#   In sistem alternativ, catalogul indica multiplicarea capacitatii cu 0.5 la
#   Duplex WS-655 si cu 0.67 la Triplex WS-655; pentru gama WS-755 cu 0.75
#   (conform paginilor catalogului).

DEBIT = {
    "baie": 0.70,
    "bucatarie": 0.50,
    "electrocasnice": 0.50,
}

K_MINIM = 0.20

ZILE_MINIME_WATERMARK = 2

# Regula interna de dimensionare a aplicatiei pentru Kinetico MACH 2030.
# Nu este o valoare declarata de producator; este un prag de proiectare
# pentru a evita alegerea unui echipament cu regenerari excesiv de dese.
ZILE_MINIME_INTRE_REGENERARI_KINETICO = 1

# Modul de functionare WaterMark:
# "alternativ" = o coloana lucreaza, celelalte sunt in asteptare
# "paralel"    = coloanele lucreaza impreuna
#
# Pentru moment lasam alegerea pe "alternativ".
# Calculatorul va putea primi ulterior alegerea utilizatorului.
MOD_FUNCTIONARE_WATERMARK = "alternativ"

# ============================================================
# FILTRE DE SEDIMENTE
# ============================================================

ECHIPAMENTE_SEDIMENTE = {
    "cintropur_manual": {
        "nume": "Cintropur - purjare manuala",
        "categorie": "sedimente",
        "tip_intretinere": "manuala",
        "tip_filtrare": "mecanic",
        "mediu": "camasa filtranta",
        "modele": {
            "NW25": {
                "debit_serviciu": 5.5,
                "debit_maxim": None,
                "debit_spalare": None,
                "racord": '1"',
                "dimensiune": None,
                "cantitate_mediu": None,
                "suprafata_filtrare_cm2": 450,
            },
            "NW32": {
                "debit_serviciu": 6.5,
                "debit_maxim": None,
                "debit_spalare": None,
                "racord": '1 1/4"',
                "dimensiune": None,
                "cantitate_mediu": None,
                "suprafata_filtrare_cm2": 840,
            },
            "NW500": {
                "debit_serviciu": 18.0,
                "debit_maxim": None,
                "debit_spalare": None,
                "racord": '2"',
                "dimensiune": None,
                "cantitate_mediu": None,
                "suprafata_filtrare_cm2": 1288,
            },
        },
    },

    "kinetico_automat": {
        "nume": "Kinetico - purjare automata",
        "categorie": "sedimente",
        "tip_intretinere": "automata",
        "tip_filtrare": "mecanic",
        "mediu": "camasa inox",
        "modele": {},
    },

    "zeolita_automata": {
        "nume": "Filtru automat cu zeolita",
        "categorie": "sedimente",
        "tip_intretinere": "automata",
        "tehnologie": "mediu filtrant",
        "mediu": "zeolit",
        "modele": {
            "WSFZ470-17": {
                "cod": 920426,
                "butelie": "7 x 44",
                "suprafata_filtranta_m2": 0.02,
                "racord": '1"',
                "debit_la_viteza": {30: 0.7, 40: 1.0, 50: 1.2},
                "debit_spalare_m3_h": 1.0,
                "zeolit_l": 16,
                "zeolit_kg": 13,
                "tarif": "B",
                "pret_euro": 842.00,
            },
            "WSFZ470-21": {
                "cod": 920427,
                "butelie": "8 x 44",
                "suprafata_filtranta_m2": 0.03,
                "racord": '1"',
                "debit_la_viteza": {30: 1.0, 40: 1.3, 50: 1.6},
                "debit_spalare_m3_h": 1.3,
                "zeolit_l": 22,
                "zeolit_kg": 17,
                "tarif": "B",
                "pret_euro": 880.00,
            },
            "WSFZ470-30": {
                "cod": 920428,
                "butelie": "9 x 48",
                "suprafata_filtranta_m2": 0.04,
                "racord": '1"',
                "debit_la_viteza": {30: 1.2, 40: 1.6, 50: 2.1},
                "debit_spalare_m3_h": 1.6,
                "zeolit_l": 30,
                "zeolit_kg": 24,
                "tarif": "B",
                "pret_euro": 949.00,
            },
            "WSFZ470-40": {
                "cod": 920429,
                "butelie": "10 x 54",
                "suprafata_filtranta_m2": 0.05,
                "racord": '1"',
                "debit_la_viteza": {30: 1.5, 40: 2.0, 50: 2.5},
                "debit_spalare_m3_h": 2.0,
                "zeolit_l": 40,
                "zeolit_kg": 32,
                "tarif": "B",
                "pret_euro": 978.00,
            },
            "WSFZ530-60": {
                "cod": 920430,
                "butelie": "12 x 52",
                "suprafata_filtranta_m2": 0.08,
                "racord": '1 1/4"',
                "debit_la_viteza": {30: 2.2, 40: 2.9, 50: 3.6},
                "debit_spalare_m3_h": 2.9,
                "zeolit_l": 57,
                "zeolit_kg": 45,
                "tarif": "B",
                "pret_euro": 1065.00,
            },
            "WSFZ530-70": {
                "cod": 920431,
                "butelie": "13 x 54",
                "suprafata_filtranta_m2": 0.09,
                "racord": '1 1/4"',
                "debit_la_viteza": {30: 2.6, 40: 3.4, 50: 4.3},
                "debit_spalare_m3_h": 3.4,
                "zeolit_l": 69,
                "zeolit_kg": 55,
                "tarif": "B",
                "pret_euro": 1117.00,
            },
            "WSFZ530-100": {
                "cod": 920432,
                "butelie": "14 x 65",
                "suprafata_filtranta_m2": 0.10,
                "racord": '1 1/4"',
                "debit_la_viteza": {30: 3.0, 40: 4.0, 50: 5.0},
                "debit_spalare_m3_h": 4.0,
                "zeolit_l": 98,
                "zeolit_kg": 78,
                "tarif": "B",
                "pret_euro": 1366.00,
            },
            "WSFZ655-125": {
                "cod": 920433,
                "butelie": "16 x 65",
                "suprafata_filtranta_m2": 0.13,
                "racord": '1 1/2"',
                "debit_la_viteza": {30: 3.9, 40: 5.2, 50: 6.5},
                "debit_spalare_m3_h": 5.2,
                "zeolit_l": 124,
                "zeolit_kg": 99,
                "tarif": "B",
                "pret_euro": 1707.00,
            },
            "WSFZ655-170": {
                "cod": 920434,
                "butelie": "18 x 65",
                "suprafata_filtranta_m2": 0.16,
                "racord": '1 1/2"',
                "debit_la_viteza": {30: 4.9, 40: 6.6, 50: 8.2},
                "debit_spalare_m3_h": 6.6,
                "zeolit_l": 166,
                "zeolit_kg": 133,
                "tarif": "B",
                "pret_euro": 1910.00,
            },
            "WSFZ655-225": {
                "cod": 920435,
                "butelie": "21 x 62",
                "suprafata_filtranta_m2": 0.22,
                "racord": '1 1/2"',
                "debit_la_viteza": {30: 6.7, 40: 8.9, 50: 11.2},
                "debit_spalare_m3_h": 8.9,
                "zeolit_l": 214,
                "zeolit_kg": 171,
                "tarif": "B",
                "pret_euro": 2194.00,
            },
            "WSF755-300": {
                "cod": 920478,
                "butelie": "24 x 72",
                "suprafata_filtranta_m2": 0.26,
                "racord": '2"',
                "debit_la_viteza": {30: 7.8, 40: 10.4, 50: 13.0},
                "debit_spalare_m3_h": 10.4,
                "zeolit_l": 318,
                "zeolit_kg": 255,
                "tarif": "B",
                "pret_euro": 3542.00,
            },
        },
    },
}


# ============================================================
# DEDURIZATOARE
# ============================================================
#
# Strategia de dimensionare:
# - case / aplicatii rezidentiale: putem folosi persoane + consum;
# - industrial / fabrici: debit necesar + consumul real;
# - WaterMark: nu presupunem regenerari multiple/zi ca metoda de
#   dimensionare. Alegerea se face in primul rand dupa debit si
#   capacitatea necesara intre regenerari.
#
# Campurile "capacitati_regenerare" contin valorile din catalog.
# Nu sunt interpretate automat aici; calculator.py va decide
# ce regim de regenerare este acceptabil.

DEDURIZATOARE = {

        # --------------------------------------------------------
    # KINETICO ERGO 11
    # --------------------------------------------------------

    "kinetico_ergo_11": {

        "nume": "Kinetico ERGO 11",
        "producator": "Kinetico",
        "categorie": "dedurizator",
        "tip": "compact",

        "strategie_dimensionare": "persoane_si_consum",
        "regenerari_max_pe_zi": 2,

        "volum_rasina_l": 10.5,
        "capacitate_schimb_hf_m3": 23.7,

        "debit_lucru_m3_h": 2.1,

        "duritate_maxima_hf": 73,

        "presiune_min_bar": 1.7,
        "presiune_max_bar": 8.6,

        "sare_regenerare_kg": 0.36,
        "apa_regenerare_l": 25,
        "durata_regenerare_min": 15,

        "temperatura_min_c": 1,
        "temperatura_max_c": 45,

        "electric": False,
        "protectie_inghet": True,

        "dimensiuni_mm": {
            "latime": 297,
            "adancime": 608,
            "inaltime": 500
        },

        "capacitate_litri_duritate": {
            15: 1250,
            20: 938,
            25: 750,
            30: 625,
            40: 469,
            50: 375,
            60: 313,
            70: 268
        }
    },


    # =========================================================
    # KINETICO MACH 2030 S
    # =========================================================

    "kinetico_2030": {

        "nume": "Kinetico MACH 2030 S",
        "producator": "Kinetico",
        "categorie": "dedurizator",
        "tip": "duplex",
        "mod_operare": "alternativ",

        "strategie_dimensionare": "persoane_si_consum",

        "racorduri": [
            '1"',
            '1 1/4"'
        ],

        "butelii": {
            "numar": 2,
            "dimensiune": "178 x 889 mm",
            "volum_total_l": 19.8,
            "volum_rasina_l": 13.3,
            "tip_rasina": "cationica"
        },

        "programator": "disc selector",

        "contor": {
            "tip": "turbina din polipropilena",
            "debit_min_l_min": 1.1,
            "debit_max_l_min": 94.6
        },

        "regenerare": {
            "tip": "contracurent",
            "durata_min": 40,
            "apa_regenerare_l": 110,
            "debit_spalare_l_min": 5.3,
            "rezervor_sare": "18 x 35",
            "capacitate_sare_kg": 114
        },

        "presiune_min_bar": 2.5,
        "presiune_max_bar": 8.6,

        "temperatura_min_c": 2,
        "temperatura_max_c": 50,

        "ph_min": 5,
        "ph_max": 10,

        "clor_liber_max_ppm": 2,
        "duritate_maxima_hf": 77,

        "debit_lucru_m3_h": 2.0,
        "debit_varf_m3_h": 3.4,

        "greutate_transport_kg": 47.6,
        "greutate_functionare_kg": 64,

        "dimensiuni_mm": {
            "A": 1041,
            "B": 381,
            "C": 178,
            "D": 460,
            "E": 890
        },


        # -----------------------------------------------------
        # DISCURILE DE DURITATE
        # -----------------------------------------------------

        "discuri_duritate": {

            "D1": {
                "duritate_hf": 7,
                "litri_intre_regenerari": 4743
            },

            "D2": {
                "duritate_hf": 18,
                "litri_intre_regenerari": 2372
            },

            "D3": {
                "duritate_hf": 24,
                "litri_intre_regenerari": 1581
            },

            "D4": {
                "duritate_hf": 33,
                "litri_intre_regenerari": 1186
            },

            "D5": {
                "duritate_hf": 40,
                "litri_intre_regenerari": 949
            },

            "D6": {
                "duritate_hf": 47,
                "litri_intre_regenerari": 791
            },

            "D7": {
                "duritate_hf": 53,
                "litri_intre_regenerari": 678
            },

            "D8": {
                "duritate_hf": 59,
                "litri_intre_regenerari": 593
            }
        },


        # -----------------------------------------------------
        # CAPACITATEA IN FUNCTIE DE DOZA DE SARE
        # -----------------------------------------------------

        "configuratii_regenerare": {

            "0.82": {
                "sare_kg": 0.82,
                "capacitate_hf_m3": 50.9,

                "discuri": {
                    "D1": 7,
                    "D2": 18,
                    "D3": 24,
                    "D4": 33,
                    "D5": 40,
                    "D6": 47,
                    "D7": 53,
                    "D8": 59
                }
            },

            "1.10": {
                "sare_kg": 1.10,
                "capacitate_hf_m3": 57.6,

                "discuri": {
                    "D1": 9,
                    "D2": 19,
                    "D3": 28,
                    "D4": 38,
                    "D5": 45,
                    "D6": 53,
                    "D7": 60,
                    "D8": 67
                }
            },

            "1.20": {
                "sare_kg": 1.20,
                "capacitate_hf_m3": 63.4,

                "discuri": {
                    "D1": 11,
                    "D2": 21,
                    "D3": 31,
                    "D4": 40,
                    "D5": 48,
                    "D6": 57,
                    "D7": 65,
                    "D8": 74
                }
            },

            "1.40": {
                "sare_kg": 1.40,
                "capacitate_hf_m3": 68.0,

                "discuri": {
                    "D1": 12,
                    "D2": 23,
                    "D3": 33,
                    "D4": 43,
                    "D5": 52,
                    "D6": 62,
                    "D7": 71,
                    "D8": 77
                }
            }
        }
    },

    # --------------------------------------------------------
    # WATERMARK WS470UF - 1"
    # --------------------------------------------------------

    "watermark_ws470uf": {
        "nume": "WaterMark WS470UF",
        "producator": "WaterMark",
        "categorie": "dedurizator",
        "configuratie_sistem": "simplex",
        "mod_dimensionare_debit": "normal",
        "tip": "simplu",
        "serie": "WS470UF",
        "racord": '1"',
        "regenerare": "contracurent",
        "strategie_dimensionare": "debit_necesar",
        "modele": {
            "WSDE470UF_15": {
                "cod": 920206,
                "butelie": "8 x 35 cm",
                "resina_l": 15,
                "sare_l": 70,
                "debit_lucru_m3_h": (0.6, 0.9),
                "capacitati": {
                    "standard_240_g_l": {"capacitate_hf_m3": 90, "sare_kg": 3.6},
                    "optimizat_120_g_l": {"capacitate_hf_m3": 77, "sare_kg": 1.8},
                    "redus_80_g_l": {"capacitate_hf_m3": 63, "sare_kg": 1.2},
                },
                "dimensiuni_mm": {"A": 1077, "B": 215, "C": 897, "D": 180, "a": 815, "b": 400},
                "pret_euro": 915.00,
                "tarif": "B",
            },
            "WSDE470UF_25": {
                "cod": 920207,
                "butelie": "10 x 35 cm",
                "resina_l": 25,
                "sare_l": 70,
                "debit_lucru_m3_h": (1.0, 1.5),
                "capacitati": {
                    "standard_240_g_l": {"capacitate_hf_m3": 150, "sare_kg": 6.0},
                    "optimizat_120_g_l": {"capacitate_hf_m3": 128, "sare_kg": 3.0},
                    "redus_80_g_l": {"capacitate_hf_m3": 105, "sare_kg": 2.0},
                },
                "dimensiuni_mm": {"A": 1073, "B": 268, "C": 893, "D": 180, "a": 815, "b": 400},
                "pret_euro": 972.00,
                "tarif": "B",
            },
            "WSDE470UF_45": {
                "cod": 920208,
                "butelie": "10 x 54 cm",
                "resina_l": 45,
                "sare_l": 100,
                "debit_lucru_m3_h": (1.8, 2.7),
                "capacitati": {
                    "standard_240_g_l": {"capacitate_hf_m3": 270, "sare_kg": 10.8},
                    "optimizat_120_g_l": {"capacitate_hf_m3": 230, "sare_kg": 5.4},
                    "redus_80_g_l": {"capacitate_hf_m3": 189, "sare_kg": 3.6},
                },
                "dimensiuni_mm": {"A": 1561, "B": 268, "C": 1381, "D": 180, "a": 940, "b": 450},
                "pret_euro": 1100.00,
                "tarif": "B",
            },
            "WSDE470UF_75": {
                "cod": 920209,
                "butelie": "13 x 54 cm",
                "resina_l": 75,
                "sare_l": 200,
                "debit_lucru_m3_h": (3.0, 3.5),
                "capacitati": {
                    "standard_240_g_l": {"capacitate_hf_m3": 450, "sare_kg": 18.0},
                    "optimizat_120_g_l": {"capacitate_hf_m3": 383, "sare_kg": 9.0},
                    "redus_80_g_l": {"capacitate_hf_m3": 315, "sare_kg": 6.0},
                },
                "dimensiuni_mm": {"A": 1578, "B": 349, "C": 1398, "D": 180, "a": 1160, "b": 550},
                "pret_euro": 1331.00,
                "tarif": "B",
            },
        },
    },


    # --------------------------------------------------------
    # WATERMARK WS530UF - 1 1/4"
    # --------------------------------------------------------

    "watermark_ws530uf": {
        "nume": "WaterMark WS530UF",
        "producator": "WaterMark",
        "categorie": "dedurizator",
        "configuratie_sistem": "simplex",
        "mod_dimensionare_debit": "normal",
        "tip": "simplu",
        "serie": "WS530UF",
        "racord": '1 1/4"',
        "regenerare": "contracurent",
        "strategie_dimensionare": "debit_necesar",
        "modele": {
            "WSDE530UF_75": {
                "cod": 920400, "butelie": "13 x 54 cm", "resina_l": 75, "sare_l": 200,
                "debit_lucru_m3_h": (3.0, 4.5),
                "capacitati": {
                    "standard_240_g_l": {"capacitate_hf_m3": 450, "sare_kg": 18},
                    "optimizat_120_g_l": {"capacitate_hf_m3": 383, "sare_kg": 9},
                    "redus_80_g_l": {"capacitate_hf_m3": 315, "sare_kg": 6},
                },
                "dimensiuni_mm": {"A":1598,"B":349,"C":1398,"D":200,"a":1160,"b":550},
                "pret_euro": 1389.00, "tarif": "B",
            },
            "WSDE530UF_100": {
                "cod": 920401, "butelie": "14 x 65 cm", "resina_l": 100, "sare_l": 350,
                "debit_lucru_m3_h": (4.0, 6.0),
                "capacitati": {
                    "standard_240_g_l": {"capacitate_hf_m3": 600, "sare_kg": 24},
                    "optimizat_120_g_l": {"capacitate_hf_m3": 510, "sare_kg": 12},
                    "redus_80_g_l": {"capacitate_hf_m3": 420, "sare_kg": 8},
                },
                "dimensiuni_mm": {"A":1874,"B":366,"C":1674,"D":200,"a":1275,"b":740},
                "pret_euro": 1551.00, "tarif": "B",
            },
            "WSDE530UF_125": {
                "cod": 920402, "butelie": "16 x 65 cm", "resina_l": 125, "sare_l": 350,
                "debit_lucru_m3_h": (5.0, 6.3),
                "capacitati": {
                    "standard_240_g_l": {"capacitate_hf_m3": 750, "sare_kg": 30},
                    "optimizat_120_g_l": {"capacitate_hf_m3": 638, "sare_kg": 15},
                    "redus_80_g_l": {"capacitate_hf_m3": 525, "sare_kg": 10},
                },
                "dimensiuni_mm": {"A":1906,"B":411,"C":1706,"D":200,"a":1275,"b":740},
                "pret_euro": 1928.00, "tarif": "B",
            },
            "WSDE530UF_150": {
                "cod": 920403, "butelie": "18 x 65 cm", "resina_l": 150, "sare_l": 500,
                "debit_lucru_m3_h": (6.0, 6.3),
                "capacitati": {
                    "standard_240_g_l": {"capacitate_hf_m3": 900, "sare_kg": 36},
                    "optimizat_120_g_l": {"capacitate_hf_m3": 765, "sare_kg": 18},
                    "redus_80_g_l": {"capacitate_hf_m3": 630, "sare_kg": 12},
                },
                "dimensiuni_mm": {"A":1922,"B":491,"C":1722,"D":200,"a":1335,"b":840},
                "pret_euro": 2310.00, "tarif": "B",
            },
            "WSDE530UF_175": {
                "cod": 920404, "butelie": "18 x 65 cm", "resina_l": 175, "sare_l": 500,
                "debit_lucru_m3_h": (6.3, 6.3),
                "capacitati": {
                    "standard_240_g_l": {"capacitate_hf_m3": 1050, "sare_kg": 42},
                    "optimizat_120_g_l": {"capacitate_hf_m3": 893, "sare_kg": 21},
                    "redus_80_g_l": {"capacitate_hf_m3": 735, "sare_kg": 14},
                },
                "dimensiuni_mm": {"A":1922,"B":491,"C":1722,"D":200,"a":1335,"b":840},
                "pret_euro": 2281.00, "tarif": "B",
            },
            "WSDE530UF_200": {
                "cod": 920405, "butelie": "21 x 62 cm", "resina_l": 200, "sare_l": 500,
                "debit_lucru_m3_h": (6.3, 6.3),
                "capacitati": {
                    "standard_240_g_l": {"capacitate_hf_m3": 1200, "sare_kg": 48},
                    "optimizat_120_g_l": {"capacitate_hf_m3": 1020, "sare_kg": 24},
                    "redus_80_g_l": {"capacitate_hf_m3": 840, "sare_kg": 16},
                },
                "dimensiuni_mm": {"A":2118,"B":555,"C":1918,"D":200,"a":1335,"b":840},
                "pret_euro": 2431.00, "tarif": "B",
            },
            "WSDE530UF_225": {
                "cod": 920406, "butelie": "21 x 62 cm", "resina_l": 225, "sare_l": 750,
                "debit_lucru_m3_h": (6.3, 6.3),
                "capacitati": {
                    "standard_240_g_l": {"capacitate_hf_m3": 1350, "sare_kg": 54},
                    "optimizat_120_g_l": {"capacitate_hf_m3": 1148, "sare_kg": 27},
                    "redus_80_g_l": {"capacitate_hf_m3": 945, "sare_kg": 18},
                },
                "dimensiuni_mm": {"A":2188,"B":555,"C":1918,"D":200,"a":1395,"b":960},
                "pret_euro": 2582.00, "tarif": "B",
            },
        },
    },


    # --------------------------------------------------------
    # WATERMARK WS490UF DUPLEX - 1"
    # --------------------------------------------------------

    "watermark_ws490uf_duplex": {
        "nume": "WaterMark WS490UF Duplex",
        "producator": "WaterMark",
        "categorie": "dedurizator",
        "configuratie_sistem": "duplex",
        "mod_dimensionare_debit": "alternativ",
        "factor_sistem_alternativ": 1.0,
        "tip": "duplex",
        "serie": "WS490UF",
        "racord": '1"',
        "regenerare": "contracurent",
        "functionare": ["alternativ", "paralel", "dupa_debit_maxim"],
        "strategie_dimensionare": "debit_necesar",
        "modele": {
            "WSDE490UF_2x15": {"cod":920436,"butelie":"8 x 35 cm","resina_l_total":30,"sare_l":70,"debit_lucru_m3_h":(0.6,1.2),
                "capacitati":{"standard_240_g_l":{"capacitate_hf_m3":90,"sare_kg":3.6},"optimizat_120_g_l":{"capacitate_hf_m3":77,"sare_kg":1.8},"redus_80_g_l":{"capacitate_hf_m3":63,"sare_kg":1.2}},
                "dimensiuni_mm":{"A":1077,"B":215,"C":891,"D":180,"a":815,"b":400},"pret_euro":1236.00,"tarif":"B"},
            "WSDE490UF_2x25": {"cod":920437,"butelie":"10 x 35 cm","resina_l_total":50,"sare_l":70,"debit_lucru_m3_h":(1.0,2.4),
                "capacitati":{"standard_240_g_l":{"capacitate_hf_m3":150,"sare_kg":6},"optimizat_120_g_l":{"capacitate_hf_m3":128,"sare_kg":3},"redus_80_g_l":{"capacitate_hf_m3":105,"sare_kg":2}},
                "dimensiuni_mm":{"A":1073,"B":268,"C":893,"D":180,"a":815,"b":400},"pret_euro":1396.00,"tarif":"B"},
            "WSDE490UF_2x45": {"cod":920438,"butelie":"10 x 54 cm","resina_l_total":90,"sare_l":100,"debit_lucru_m3_h":(1.8,3.6),
                "capacitati":{"standard_240_g_l":{"capacitate_hf_m3":270,"sare_kg":10.8},"optimizat_120_g_l":{"capacitate_hf_m3":230,"sare_kg":5.4},"redus_80_g_l":{"capacitate_hf_m3":189,"sare_kg":3.6}},
                "dimensiuni_mm":{"A":1561,"B":268,"C":1381,"D":180,"a":875,"b":460},"pret_euro":1649.00,"tarif":"B"},
            "WSDE490UF_2x75": {"cod":920439,"butelie":"13 x 54 cm","resina_l_total":150,"sare_l":200,"debit_lucru_m3_h":(3.0,6.0),
                "capacitati":{"standard_240_g_l":{"capacitate_hf_m3":450,"sare_kg":18},"optimizat_120_g_l":{"capacitate_hf_m3":383,"sare_kg":9},"redus_80_g_l":{"capacitate_hf_m3":316,"sare_kg":6}},
                "dimensiuni_mm":{"A":1578,"B":349,"C":1398,"D":180,"a":1040,"b":585},"pret_euro":2121.00,"tarif":"B"},
            "WSDE490UF_2x100": {"cod":920440,"butelie":"14 x 65 cm","resina_l_total":200,"sare_l":200,"debit_lucru_m3_h":(3.5,7.0),
                "capacitati":{"standard_240_g_l":{"capacitate_hf_m3":600,"sare_kg":24},"optimizat_120_g_l":{"capacitate_hf_m3":510,"sare_kg":12},"redus_80_g_l":{"capacitate_hf_m3":420,"sare_kg":8}},
                "dimensiuni_mm":{"A":1854,"B":366,"C":1674,"D":180,"a":1040,"b":585},"pret_euro":2406.84,"tarif":"B"},
            "WSDE490UF_2x125": {"cod":920441,"butelie":"16 x 65 cm","resina_l_total":250,"sare_l":200,"debit_lucru_m3_h":(3.5,7.0),
                "capacitati":{"standard_240_g_l":{"capacitate_hf_m3":750,"sare_kg":30},"optimizat_120_g_l":{"capacitate_hf_m3":638,"sare_kg":15},"redus_80_g_l":{"capacitate_hf_m3":525,"sare_kg":10}},
                "dimensiuni_mm":{"A":1886,"B":411,"C":1706,"D":180,"a":1040,"b":585},"pret_euro":3042.00,"tarif":"B"},
            "WSDE490UF_2x150": {"cod":920442,"butelie":"18 x 65 cm","resina_l_total":300,"sare_l":350,"debit_lucru_m3_h":(3.5,7.0),
                "capacitati":{"standard_240_g_l":{"capacitate_hf_m3":900,"sare_kg":36},"optimizat_120_g_l":{"capacitate_hf_m3":765,"sare_kg":18},"redus_80_g_l":{"capacitate_hf_m3":630,"sare_kg":12}},
                "dimensiuni_mm":{"A":1902,"B":491,"C":1722,"D":180,"a":1275,"b":740},"pret_euro":3381.20,"tarif":"B"},
        },
    },
}


# ============================================================
# WATERMARK MULTITANQUE MTS-655
# ============================================================

def _mts_655_model(cod, model, resina_l, butelie, sare_l, apa_reg_l,
                   siles_1_3_2_5_kg, siles_2_4_kg,
                   capacitati, pret, dimensiuni):
    return {
        "cod": cod,
        "model": model,
        "resina_l": resina_l,
        "butelie": butelie,
        "sare_l": sare_l,
        "consum_apa_regenerare_l": apa_reg_l,
        "silex_1_3_2_5_mm_kg": siles_1_3_2_5_kg,
        "silex_2_4_mm_kg": siles_2_4_kg,
        "capacitati": capacitati,
        "debit_nominal_m3_h": 10.0,
        "debit_spalare_m3_h": 6.8,
        "racord": '1 1/2"',
        "pret_euro": pret,
        "tarif": "B",
        "dimensiuni_mm": dimensiuni,
    }


DEDURIZATOARE["watermark_mts_655_simplex"] = {
    "nume": "WaterMark MTS-655 Símplex",
    "producator": "WaterMark",
    "categorie": "dedurizator",
    "configuratie_sistem": "simplex",
    "mod_dimensionare_debit": "normal",
    "tip": "multitanc - simplex",
    "serie": "MTS-655",
    "racord": '1 1/2"',
    "strategie_dimensionare": "debit_necesar",
    "regenerare": "contracurent",
    "functionare": ["alternativ", "paralel", "dupa_debit"],
    "modele": {
        "MTS-655-1-50": _mts_655_model(920085,"MTS-655-1-50",50,"14 x 65",350,598,16,None,
            {"standard_96_g_l":{"capacitate_hf_m3":279,"sare_kg":4.8},"intermediar_161_g_l":{"capacitate_hf_m3":362,"sare_kg":8.1},"maxim_242_g_l":{"capacitate_hf_m3":433,"sare_kg":12.1}},2188,{"A":1604,"B":349,"C":1398,"D":206,"a":1275,"b":740}),
        "MTS-655-1-85": _mts_655_model(920043,"MTS-655-1-85",85,"16 x 65",350,598,21,None,
            {"standard_96_g_l":{"capacitate_hf_m3":415,"sare_kg":4.8},"intermediar_161_g_l":{"capacitate_hf_m3":540,"sare_kg":8.1},"maxim_242_g_l":{"capacitate_hf_m3":646,"sare_kg":12.1}},2720,{"A":1880,"B":366,"C":1674,"D":206,"a":1275,"b":740}),
        "MTS-655-1-115": _mts_655_model(920044,"MTS-655-1-115",115,"18 x 65",350,777,16,32,
            {"standard_96_g_l":{"capacitate_hf_m3":552,"sare_kg":4.8},"intermediar_161_g_l":{"capacitate_hf_m3":718,"sare_kg":8.1},"maxim_242_g_l":{"capacitate_hf_m3":859,"sare_kg":12.1}},2998,{"A":1911,"B":411,"C":1705,"D":206,"a":1275,"b":740}),
        "MTS-655-1-145": _mts_655_model(920045,"MTS-655-1-145",145,"21 x 62",500,1019,25,50,
            {"standard_96_g_l":{"capacitate_hf_m3":694,"sare_kg":19.2},"intermediar_161_g_l":{"capacitate_hf_m3":903,"sare_kg":32.2},"maxim_242_g_l":{"capacitate_hf_m3":1079,"sare_kg":48.4}},3450,{"A":1928,"B":491,"C":1722,"D":206,"a":1275,"b":740}),
        "MTS-655-1-200": _mts_655_model(920046,"MTS-655-1-200",200,"24 x 72",500,1359,40,56,
            {"standard_96_g_l":{"capacitate_hf_m3":968,"sare_kg":27.4},"intermediar_161_g_l":{"capacitate_hf_m3":1259,"sare_kg":45.9},"maxim_242_g_l":{"capacitate_hf_m3":1505,"sare_kg":69.0}},3704,{"A":1927,"B":555,"C":1721,"D":206,"a":1335,"b":840}),
        "MTS-655-1-285": _mts_655_model(920047,"MTS-655-1-285",285,"30 x 72",750,1993,56,88,
            {"standard_96_g_l":{"capacitate_hf_m3":1383,"sare_kg":40.8},"intermediar_161_g_l":{"capacitate_hf_m3":1799,"sare_kg":68.4},"maxim_242_g_l":{"capacitate_hf_m3":2150,"sare_kg":102.9}},4428,{"A":2124,"B":622,"C":1918,"D":206,"a":1335,"b":840}),
        "MTS-655-1-425": _mts_655_model(920048,"MTS-655-1-425",425,"36 x 72",750,2915,56,88,
            {"standard_96_g_l":{"capacitate_hf_m3":2077,"sare_kg":62.4},"intermediar_161_g_l":{"capacitate_hf_m3":2702,"sare_kg":104.7},"maxim_242_g_l":{"capacitate_hf_m3":3229,"sare_kg":157.3}},5678,{"A":2346,"B":787,"C":2140,"D":206,"a":1395,"b":960}),
    },
}


# ============================================================
# WATERMARK MTS-655 DUPLEX / TRIPLEX / CUADRUPLEX
# ============================================================

def _mts_multitanc_model(cod, model, resina_unitara_l, nr_col,
                         butelie, sare_l_total, apa_reg_l_total,
                         silex1_total, silex2_total,
                         cap_96, cap_161, cap_242,
                         pret, factor_alternativ=0.75):
    return {
        "cod": cod,
        "model": model,
        "numar_coloane": nr_col,
        "resina_l_pe_coloana": resina_unitara_l,
        "resina_l_total": resina_unitara_l * nr_col,
        "butelie": butelie,
        "sare_l_total": sare_l_total,
        "consum_apa_regenerare_l_total": apa_reg_l_total,
        "silex_1_3_2_5_mm_kg_total": silex1_total,
        "silex_2_4_mm_kg_total": silex2_total,
        "capacitati_paralel": {
            "standard_96_g_l": {"capacitate_hf_m3": cap_96[0], "sare_kg": cap_96[1]},
            "intermediar_161_g_l": {"capacitate_hf_m3": cap_161[0], "sare_kg": cap_161[1]},
            "maxim_242_g_l": {"capacitate_hf_m3": cap_242[0], "sare_kg": cap_242[1]},
        },
        "factor_sistem_alternativ": factor_alternativ,
        "racord": '1 1/2"',
        "pret_euro": pret,
        "tarif": "B",
    }


# DUPLEX 655
DEDURIZATOARE["watermark_mts_655_duplex"] = {
    "nume": "WaterMark MTS-655 Duplex",
    "producator": "WaterMark",
    "categorie": "dedurizator",
    "configuratie_sistem": "duplex",
    "mod_dimensionare_debit": "alternativ",
    "factor_sistem_alternativ": 0.5,
    "tip": "multitanc - duplex",
    "serie": "MTS-655",
    "racord": '1 1/2"',
    "strategie_dimensionare": "debit_necesar",
    "regenerare": "contracurent",
    "functionare": ["alternativ", "paralel", "dupa_debit"],
    "modele": {
        "MTS-655-2-50": _mts_multitanc_model(920086,"MTS-655-2-50",50,2,"14 x 65",350,598,16*2,None,(557,9.6),(725,16.2),(866,20.6),4156),
        "MTS-655-2-85": _mts_multitanc_model(920050,"MTS-655-2-85",85,2,"16 x 65",350,598,21*2,None,(813,9.2),(1081,13.8),(1292,18.4),5672),
        "MTS-655-2-115": _mts_multitanc_model(920051,"MTS-655-2-115",115,2,"18 x 65",350,777,16*2,32*2,(1105,13.8),(1437,22.9),(1717,34.4),6124),
        "MTS-655-2-145": _mts_multitanc_model(920052,"MTS-655-2-145",145,2,"21 x 62",500,1019,25*2,50*2,(1388,19.0),(1805,31.9),(2158,47.9),6888),
        "MTS-655-2-200": _mts_multitanc_model(920053,"MTS-655-2-200",200,2,"24 x 72",500,1359,40*2,56*2,(1935,27.4),(2517,45.9),(3009,69.0),7293),
        "MTS-655-2-285": _mts_multitanc_model(920054,"MTS-655-2-285",285,2,"30 x 72",750,1993,56*2,88*2,(2766,40.8),(3598,68.4),(4301,102.9),9145),
        "MTS-655-2-425": _mts_multitanc_model(920055,"MTS-655-2-425",425,2,"36 x 72",750,2915,56*2,88*2,(4154,62.4),(5403,104.7),(6459,157.3),11322),
    },
}

# TRIPLEX 655
DEDURIZATOARE["watermark_mts_655_triplex"] = {
    "nume": "WaterMark MTS-655 Triplex",
    "producator": "WaterMark",
    "categorie": "dedurizator",
    "configuratie_sistem": "triplex",
    "mod_dimensionare_debit": "paralel",
    "tip": "multitanc - triplex",
    "serie": "MTS-655",
    "racord": '1 1/2"',
    "strategie_dimensionare": "debit_necesar",
    "regenerare": "contracurent",
    "functionare": ["alternativ", "paralel", "dupa_debit"],
    "modele": {
        "MTS-655-3-85": _mts_multitanc_model(920057,"MTS-655-3-85",85,3,"16 x 65",350*2,598,21*3,None,(1246,13.7),(1621,22.9),(1938,34.4),8393,0.67),
        "MTS-655-3-115": _mts_multitanc_model(920058,"MTS-655-3-115",115,3,"18 x 65",350*2,777,16*3,32*3,(1657,20.6),(2155,31.9),(2567,47.9),9608,0.67),
        "MTS-655-3-145": _mts_multitanc_model(920059,"MTS-655-3-145",145,3,"21 x 62",500*2,1019,25*3,50*3,(2082,27.2),(2708,45.6),(3237,68.5),10303,0.67),
        "MTS-655-3-200": _mts_multitanc_model(920060,"MTS-655-3-200",200,3,"24 x 72",500*2,1359,40*3,56*3,(2903,40.8),(3776,68.4),(4514,102.9),11194,0.67),
        "MTS-655-3-285": _mts_multitanc_model(920061,"MTS-655-3-285",285,3,"30 x 72",750*2,1993,56*3,88*3,(4149,62.4),(5397,104.7),(6451,157.3),13776,0.67),
        "MTS-655-3-425": _mts_multitanc_model(920062,"MTS-655-3-425",425,3,"36 x 72",750*2,2915,56*3,88*3,(6231,81.6),(8105,136.9),(9688,205.7),16554,0.67),
    },
}

# CUADRUPLEX 655
DEDURIZATOARE["watermark_mts_655_cuadruplex"] = {
    "nume": "WaterMark MTS-655 Cuadruplex",
    "producator": "WaterMark",
    "categorie": "dedurizator",
    "configuratie_sistem": "cuadruplex",
    "mod_dimensionare_debit": "alternativ",
    "tip": "multitanc - cuadruplex",
    "serie": "MTS-655",
    "racord": '1 1/2"',
    "strategie_dimensionare": "debit_necesar",
    "regenerare": "contracurent",
    "functionare": ["alternativ", "paralel", "dupa_debit"],
    "modele": {
        "MTS-655-4-85": _mts_multitanc_model(920064,"MTS-655-4-85",85,4,"16 x 65",350*2,598,21*4,None,(1662,13.9),(2161,23.3),(2584,35.1),11113),
        "MTS-655-4-115": _mts_multitanc_model(920065,"MTS-655-4-115",115,4,"18 x 65",350*2,777,16*4,32*4,(2209,20.6),(2873,35.1),(3435,55.2),11819),
        "MTS-655-4-145": _mts_multitanc_model(920066,"MTS-655-4-145",145,4,"21 x 62",500*2,1019,25*4,50*4,(2776,27.4),(3611,45.9),(4316,69.0),13660),
        "MTS-655-4-200": _mts_multitanc_model(920067,"MTS-655-4-200",200,4,"24 x 72",500*2,1359,40*4,56*4,(3871,40.8),(5034,68.4),(6018,102.9),14818),
        "MTS-655-4-285": _mts_multitanc_model(920068,"MTS-655-4-285",285,4,"30 x 72",750*2,1993,56*4,88*4,(5532,81.6),(7196,136.9),(8602,205.7),17191),
        "MTS-655-4-425": _mts_multitanc_model(920069,"MTS-655-4-425",425,4,"36 x 72",750*2,2915,56*4,88*4,(8309,96.0),(10806,161.0),(12918,242.0),19622),
    },
}


# ============================================================
# WATERMARK MTS-755
# ============================================================

def _mts_755_model(cod, model, resina_l, nr_col, butelie, sare_l, apa_reg_l,
                   silex1, silex2, caps, pret):
    return {
        "cod": cod,
        "model": model,
        "numar_coloane": nr_col,
        "resina_l_pe_coloana": resina_l,
        "resina_l_total": resina_l * nr_col,
        "butelie": butelie,
        "sare_l_total": sare_l,
        "consum_apa_regenerare_l_total": apa_reg_l,
        "silex_1_3_2_5_mm_kg_total": silex1,
        "silex_2_4_mm_kg_total": silex2,
        "capacitati_paralel": {
            "standard_96_g_l": {"capacitate_hf_m3": caps[0][0], "sare_kg": caps[0][1]},
            "intermediar_161_g_l": {"capacitate_hf_m3": caps[1][0], "sare_kg": caps[1][1]},
            "maxim_242_g_l": {"capacitate_hf_m3": caps[2][0], "sare_kg": caps[2][1]},
        },
        "factor_sistem_alternativ": 0.75,
        "racord": '2"',
        "pret_euro": pret,
        "tarif": "B",
    }


def _family_755(name, tip, configuratie_sistem, models):

    if configuratie_sistem == "simplex":
        mod_dimensionare_debit = "normal"

    elif configuratie_sistem == "duplex":
        mod_dimensionare_debit = "alternativ"

    elif configuratie_sistem == "triplex":
        mod_dimensionare_debit = "paralel"

    elif configuratie_sistem == "cuadruplex":
        mod_dimensionare_debit = "alternativ"

    else:
        mod_dimensionare_debit = "normal"

    return {
        "nume": name,
        "producator": "WaterMark",
        "categorie": "dedurizator",
        "tip": tip,
        "configuratie_sistem": configuratie_sistem,
                "mod_dimensionare_debit": {
            "simplex": "normal",
            "duplex": "alternativ",
            "triplex": "paralel",
            "cuadruplex": "alternativ"
        }[configuratie_sistem],
        "serie": "MTS-755",
        "racord": '2"',
        "strategie_dimensionare": "debit_necesar",
        "regenerare": "contracurent",
        "functionare": ["alternativ", "paralel", "dupa_debit"],
        "debit_nominal_m3_h": 15.9,
        "debit_varf_m3_h": 20.0,
        "debit_spalare_m3_h": 12.0,
        "modele": models,
    }


# SIMPLEX 755
DEDURIZATOARE["watermark_mts_755_simplex"] = _family_755(
    "WaterMark MTS-755 Símplex",
    "multitanc - simplex",
    "simplex",
    {
        "MTS-755-1-200": _mts_755_model(920446,"MTS-755-1-200",200,1,"24 x 72",500,1359,40,56,((957,19.2),(1246,32.2),(1488,48.4)),4115),
        "MTS-755-1-285": _mts_755_model(920447,"MTS-755-1-285",285,1,"30 x 72",750,1993,56,88,((1364,27.4),(1775,45.9),(2121,69.0)),4891),
        "MTS-755-1-425": _mts_755_model(920448,"MTS-755-1-425",425,1,"36 x 72",1500,3962,56,99,((2034,40.8),(2647,68.4),(3163,102.9)),6135),
        "MTS-755-1-566": _mts_755_model(920449,"MTS-755-1-566",566,1,"36 x 72",1500,4273,56,99,((2709,54.3),(3525,91.1),(4212,137.0)),8503),
        "MTS-755-1-650": _mts_755_model(920450,"MTS-755-1-650",650,1,"42 x 72",1500,5950,86,152,((3111,70.6),(4048,118.3),(4837,177.9)),8584),
        "MTS-755-1-735": _mts_755_model(920451,"MTS-755-1-735",735,1,"42 x 72",2000,7000,86,152,((3518,81.6),(4577,136.9),(5469,205.7)),10928),
        "MTS-755-1-850": _mts_755_model(920452,"MTS-755-1-850",850,1,"42 x 72",1500,5145,86,152,((4068,96.0),(5293,161.0),(6325,242.0)),11443),
        "MTS-755-1-1000": _mts_755_model(920453,"MTS-755-1-1000",1000,1,"42 x 72",2000,7000,86,152,((4786,96.0),(6228,161.0),(7441,242.0)),12271),
    }
)

# DUPLEX 755
DEDURIZATOARE["watermark_mts_755_duplex"] = _family_755(
    "WaterMark MTS-755 Duplex",
    "multitanc - duplex",
    "duplex",
    {
        "MTS-755-2-200": _mts_755_model(920454,"MTS-755-2-200",200,2,"24 x 72",500,1359,40*2,56*2,((1914,19.2),(2491,32.2),(2977,48.4)),8150),
        "MTS-755-2-285": _mts_755_model(920455,"MTS-755-2-285",285,2,"30 x 72",750,1993,56*2,88*2,((2728,27.4),(3550,45.9),(4242,69.0)),9591),
        "MTS-755-2-425": _mts_755_model(920456,"MTS-755-2-425",425,2,"36 x 72",1500,3962,56*2,99*2,((4068,40.8),(5293,68.4),(6325,102.9)),11981),
        "MTS-755-2-566": _mts_755_model(920457,"MTS-755-2-566",566,2,"36 x 72",1500,4273,56*2,99*2,((5418,54.3),(7050,91.1),(8424,137.0)),15640),
        "MTS-755-2-650": _mts_755_model(920458,"MTS-755-2-650",650,2,"42 x 72",1500,5950,86*2,152*2,((6222,70.6),(8096,118.3),(9674,177.9)),16404),
        "MTS-755-2-730": _mts_755_model(920459,"MTS-755-2-730",735,2,"42 x 72",2000,7000,86*2,152*2,((7036,81.6),(9155,136.9),(10939,205.7)),21046),
        "MTS-755-2-850": _mts_755_model(920460,"MTS-755-2-850",850,2,"42 x 72",1500,5145,86*2,152*2,((8137,96.0),(10587,161.0),(12650,242.0)),22111),
        "MTS-755-2-1000": _mts_755_model(920461,"MTS-755-2-1000",1000,2,"42 x 72",2000,7000,86*2,152*2,((9572,96.0),(12455,161.0),(14883,242.0)),23662),
    }
)

# TRIPLEX 755
DEDURIZATOARE["watermark_mts_755_triplex"] = _family_755(
    "WaterMark MTS-755 Triplex",
    "multitanc - triplex",
    "triplex",
    {
        "MTS-755-3-200": _mts_755_model(920462,"MTS-755-3-200",200,3,"24 x 72",500,1359,40*3,56*3,((2872,19.2),(3737,32.2),(4465,48.4)),12277),
        "MTS-755-3-285": _mts_755_model(920463,"MTS-755-3-285",285,3,"30 x 72",750,1993,56*3,88*3,((4092,27.4),(5325,45.9),(6362,69.0)),14430),
        "MTS-755-3-425": _mts_755_model(920464,"MTS-755-3-425",425,3,"36 x 72",1500,3962,56*3,99*3,((6102,40.8),(7940,68.4),(9488,102.9)),18111),
        "MTS-755-3-566": _mts_755_model(920465,"MTS-755-3-566",566,3,"36 x 72",1500,4273,56*3,99*3,((8127,54.3),(10574,91.1),(12635,137.0)),23789),
        "MTS-755-3-650": _mts_755_model(920466,"MTS-755-3-650",650,3,"42 x 72",1500,5950,86*3,152*3,((9333,70.6),(12144,118.3),(14511,177.9)),24982),
        "MTS-755-3-735": _mts_755_model(920467,"MTS-755-3-735",735,3,"42 x 72",2000,7000,86*3,152*3,((10554,81.6),(13732,136.9),(16408,205.7)),31904),
        "MTS-755-3-850": _mts_755_model(920468,"MTS-755-3-850",850,3,"42 x 72",1500,5145,86*3,152*3,((12205,96.0),(15880,161.0),(18976,242.0)),33531),
        "MTS-755-3-1000": _mts_755_model(920469,"MTS-755-3-1000",1000,3,"42 x 72",2000,7000,86*3,152*3,((14359,96.0),(18683,161.0),(22324,242.0)),35915),
    }
)

# CUADRUPLEX 755
DEDURIZATOARE["watermark_mts_755_cuadruplex"] = _family_755(
    "WaterMark MTS-755 Cuadruplex",
    "multitanc - cuadruplex",
    "cuadruplex",
    {
        "MTS-755-4-200": _mts_755_model(920470,"MTS-755-4-200",200,4,"24 x 72",500,1359,40*4,56*4,((3829,27.4),(4982,45.9),(5953,69.0)),15906),
        "MTS-755-4-285": _mts_755_model(920471,"MTS-755-4-285",285,4,"30 x 72",750,1993,56*4,88*4,((5456,40.8),(7099,68.4),(8483,102.9)),18777),
        "MTS-755-4-425": _mts_755_model(920472,"MTS-755-4-425",425,4,"36 x 72",1500,3962,56*4,99*4,((8137,54.3),(10587,91.1),(12650,137.0)),23540),
        "MTS-755-4-566": _mts_755_model(920473,"MTS-755-4-566",566,4,"36 x 72",1500,4273,56*4,99*4,((10836,70.6),(14099,118.3),(16847,177.9)),30822),
        "MTS-755-4-650": _mts_755_model(920474,"MTS-755-4-650",650,4,"42 x 72",1500,5950,86*4,152*4,((12444,81.6),(16192,136.9),(19348,205.7)),32385),
        "MTS-755-4-735": _mts_755_model(920475,"MTS-755-4-735",735,4,"42 x 72",2000,7000,86*4,152*4,((14071,96.0),(18309,161.0),(21878,242.0)),41675),
        "MTS-755-4-850": _mts_755_model(920476,"MTS-755-4-850",850,4,"42 x 72",1500,5145,86*4,152*4,((16273,96.0),(21174,161.0),(25301,242.0)),43851),
        "MTS-755-4-1000": _mts_755_model(920477,"MTS-755-4-1000",1000,4,"42 x 72",2000,7000,86*4,152*4,((19145,96.0),(24910,161.0),(29766,242.0)),46942),
    }
)


# ============================================================
# REGULI / INFORMATII GENERALE DIN CATALOG
# ============================================================

WATERMARK = {
    "presiune_min_bar": 2.0,
    "presiune_max_bar": 8.5,
    "temperatura_min_c": 4,
    "temperatura_max_c": 40,
    "alimentare": "110/240 Vac - 12 Vac",
    "rasina": "GreenResin",
    "mediu_distribuitor": "silex",
    "strategie_dimensionare": "debit_necesar",
    "observatie": (
        "Pentru aplicatia noastra, WaterMark nu va fi dimensionat presupunand "
        "regenerari multiple pe zi. Calculatorul va verifica debitul necesar "
        "si capacitatea disponibila intre regenerari."
    ),
}

WATERMARK_MTS_655 = {
    "presiune_min_bar": 2.0,
    "presiune_max_bar": 8.5,
    "temperatura_min_c": 4,
    "temperatura_max_c": 35,
    "racord": '1 1/2"',
    "debit_nominal_m3_h": 10.0,
    "debit_spalare_m3_h": 6.8,
}

WATERMARK_MTS_755 = {
    "presiune_min_bar": 2.0,
    "presiune_max_bar": 8.5,
    "temperatura_min_c": 4,
    "temperatura_max_c": 35,
    "racord": '2"',
    "debit_nominal_m3_h": 15.9,
    "debit_varf_m3_h": 20.0,
    "debit_spalare_m3_h": 12.0,
}


# ============================================================
# OBSERVATIE PENTRU KINETICO
# ============================================================
#
# Kinetico ERGO si 2030 nu apar in PDF-ul WaterMark incarcat acum.
# Nu introducem valori inventate in aceasta baza.
# Le vom adauga in acelasi format cand avem catalogul Kinetico
# corespunzator.
#
# Pentru ele vom putea seta ulterior:
#
# "strategie_dimensionare": "persoane_si_consum"
# "regenerari_recomandate_maxim_pe_zi": 1 sau 2
#
# in functie de model si de datele catalogului.


# ============================================================
# VERSIUNE BAZA DE DATE
# ============================================================

VERSIUNE_DATABASE = "0.1"

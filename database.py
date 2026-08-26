DEBIT = {
    "baie": 0.7,
    "bucatarie": 0.50,
    "electrocasnice": 0.50
}

K_MINIM = 0.2

ECHIPAMENTE_SEDIMENTE = {
    "cintropur_manual" : {
        "nume" : "Cintropur - purjare mauala",
        "categorie" : "sedimente",
        "tip_intretinere" : "manuala",
        "tip_filtrare" : "mecanic",
        "mediu" : "camasa filtranta",
        "modele" : {
            "NW25" : {
                "debit_serviciu": 5.5,
                "debit_maxim": None,
                "debit_spalare": None,
                "racord": "1",
                "dimensiune": None,
                "cantitate_mediu": None,
                "suprafata_filtrare" : 450
            },
            "NW32" : {
                "debit_serviciu": 6.5,
                "debit_maxim": None,
                "debit_spalare": None,
                "racord": "1 1/4",
                "dimensiune": None,
                "cantitate_mediu": None,
                "suprafata_filtrare" : 840
            },
            "NW500" : {
                "debit_serviciu": 18,
                "debit_maxim": None,
                "debit_spalare": None,
                "racord": "2",
                "dimensiune": None,
                "cantitate_mediu": None,
                "suprafata_filtrare" : 1288
            }
        }
    },

    "kinetico_automat" : {
        "nume" : "Kinetico - purjare",
        "categorie" : "sedimente",
        "tip_purjare" : "automata",
        "mediu" : "camasa inox",
        "modele" : {
            #se introduc modele
        }
    },
    "zeolita_automata": {

        "nume": "Filtru automat cu zeolita",
        "categorie": "sedimente",
        "tip_intretinere" : "automata",
        "tehnologie" : "mediu",
        "mediu": "zeolit",

        "modele": {

            "WSFZ470-17": {
                "cod": 920426,
                "butelie": "7 x 44",
                "suprafata_filtranta_m2": 0.02,
                "racord": '1"',

                "debit_la_viteza": {
                    30: 0.7,
                    40: 1.0,
                    50: 1.2
                },

                "debit_spalare_m3_h": 1.0,

                "zeolit_l": 16,
                "zeolit_kg": 13,

                "tarif": "B",
                "pret_euro": 842.00
            },


            "WSFZ470-21": {
                "cod": 920427,
                "butelie": "8 x 44",
                "suprafata_filtranta_m2": 0.03,
                "racord": '1"',

                "debit_la_viteza": {
                    30: 1.0,
                    40: 1.3,
                    50: 1.6
                },

                "debit_spalare_m3_h": 1.3,

                "zeolit_l": 22,
                "zeolit_kg": 17,

                "tarif": "B",
                "pret_euro": 880.00
            },


            "WSFZ470-30": {
                "cod": 920428,
                "butelie": "9 x 48",
                "suprafata_filtranta_m2": 0.04,
                "racord": '1"',

                "debit_la_viteza": {
                    30: 1.2,
                    40: 1.6,
                    50: 2.1
                },

                "debit_spalare_m3_h": 1.6,

                "zeolit_l": 30,
                "zeolit_kg": 24,

                "tarif": "B",
                "pret_euro": 949.00
            },


            "WSFZ470-40": {
                "cod": 920429,
                "butelie": "10 x 54",
                "suprafata_filtranta_m2": 0.05,
                "racord": '1"',

                "debit_la_viteza": {
                    30: 1.5,
                    40: 2.0,
                    50: 2.5
                },

                "debit_spalare_m3_h": 2.0,

                "zeolit_l": 40,
                "zeolit_kg": 32,

                "tarif": "B",
                "pret_euro": 978.00
            },


            "WSFZ530-60": {
                "cod": 920430,
                "butelie": "12 x 52",
                "suprafata_filtranta_m2": 0.08,
                "racord": '1 1/4"',

                "debit_la_viteza": {
                    30: 2.2,
                    40: 2.9,
                    50: 3.6
                },

                "debit_spalare_m3_h": 2.9,

                "zeolit_l": 57,
                "zeolit_kg": 45,

                "tarif": "B",
                "pret_euro": 1065.00
            },


            "WSFZ530-70": {
                "cod": 920431,
                "butelie": "13 x 54",
                "suprafata_filtranta_m2": 0.09,
                "racord": '1 1/4"',

                "debit_la_viteza": {
                    30: 2.6,
                    40: 3.4,
                    50: 4.3
                },

                "debit_spalare_m3_h": 3.4,

                "zeolit_l": 69,
                "zeolit_kg": 55,

                "tarif": "B",
                "pret_euro": 1117.00
            },


            "WSFZ530-100": {
                "cod": 920432,
                "butelie": "14 x 65",
                "suprafata_filtranta_m2": 0.10,
                "racord": '1 1/4"',

                "debit_la_viteza": {
                    30: 3.0,
                    40: 4.0,
                    50: 5.0
                },

                "debit_spalare_m3_h": 4.0,

                "zeolit_l": 98,
                "zeolit_kg": 78,

                "tarif": "B",
                "pret_euro": 1366.00
            },


            "WSFZ655-125": {
                "cod": 920433,
                "butelie": "16 x 65",
                "suprafata_filtranta_m2": 0.13,
                "racord": '1 1/2"',

                "debit_la_viteza": {
                    30: 3.9,
                    40: 5.2,
                    50: 6.5
                },

                "debit_spalare_m3_h": 5.2,

                "zeolit_l": 124,
                "zeolit_kg": 99,

                "tarif": "B",
                "pret_euro": 1707.00
            },


            "WSFZ655-170": {
                "cod": 920434,
                "butelie": "18 x 65",
                "suprafata_filtranta_m2": 0.16,
                "racord": '1 1/2"',

                "debit_la_viteza": {
                    30: 4.9,
                    40: 6.6,
                    50: 8.2
                },

                "debit_spalare_m3_h": 6.6,

                "zeolit_l": 166,
                "zeolit_kg": 133,

                "tarif": "B",
                "pret_euro": 1910.00
            },


            "WSFZ655-225": {
                "cod": 920435,
                "butelie": "21 x 62",
                "suprafata_filtranta_m2": 0.22,
                "racord": '1 1/2"',

                "debit_la_viteza": {
                    30: 6.7,
                    40: 8.9,
                    50: 11.2
                },

                "debit_spalare_m3_h": 8.9,

                "zeolit_l": 214,
                "zeolit_kg": 171,

                "tarif": "B",
                "pret_euro": 2194.00
            },


            "WSF755-300": {
                "cod": 920478,
                "butelie": "24 x 72",
                "suprafata_filtranta_m2": 0.26,
                "racord": '2"',

                "debit_la_viteza": {
                    30: 7.8,
                    40: 10.4,
                    50: 13.0
                },

                "debit_spalare_m3_h": 10.4,

                "zeolit_l": 318,
                "zeolit_kg": 255,

                "tarif": "B",
                "pret_euro": 3542.00
            }
        }
    }
}

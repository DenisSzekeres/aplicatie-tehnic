import user_input
import calculator
import afisare


# ============================================================
# 1. CITIRE DATE
# ============================================================

date = user_input.citeste_consum()


# ============================================================
# 2. CALCUL DEBIT
# ============================================================

if date["debit_necesar"] > 0:

    debit_calculat = date["debit_necesar"]

else:

    debit_calculat = calculator.calculeaza_debit_simultan(date)


# ============================================================
# 3. DEBITE DE PROIECT
# ============================================================

# Dedurizatorul este dupa rezervor.
debit_proiect_dedurizator = debit_calculat


# Filtrul este inaintea rezervorului.
if date["volum_rezervor"] > 0:

    debit_proiect_filtru = calculator.calculeaza_debit_proiect_cu_rezervor(
        debit_calculat,
        date["volum_rezervor"],
        date["durata_varf"],
        date["ore_reumplere_rezervor"]
    )

else:

    debit_proiect_filtru = debit_calculat


# ============================================================
# 4. AFISARE DEBITE
# ============================================================

print("\n")
print("=" * 50)
print("        REZULTAT DIMENSIONARE")
print("=" * 50)

print(
    f"\nDebit proiect: "
    f"{debit_calculat:.2f} m3/h"
)

if date["volum_rezervor"] > 0:

    print(
        f"Debit proiect filtru: "
        f"{debit_proiect_filtru:.2f} m3/h"
    )

    print(
        f"Debit proiect dedurizator: "
        f"{debit_proiect_dedurizator:.2f} m3/h"
    )

    date_rezervor = calculator.calculeaza_date_rezervor(
        debit_calculat,
        date["volum_rezervor"],
        date["durata_varf"],
        date["ore_reumplere_rezervor"]
    )

    print(
        f"Consum in perioada de varf: "
        f"{date_rezervor['volum_consum_varf']:.2f} m3"
    )
    print(
        f"Rezerva disponibila in rezervor: "
        f"{date_rezervor['rezerva_volum']:.2f} m3"
    )
    print(
        f"Debit de reumplere: "
        f"{date_rezervor['debit_reumplere']:.2f} m3/h"
    )


# ============================================================
# 5. ALEGERE FILTRARE
# ============================================================

tip_filtrare = user_input.citeste_tip_filtrare()

rezultat_filtrare = calculator.calculeaza_filtrare(
    debit_proiect_filtru,
    tip_filtrare,
    date["ntu"]
)


# ============================================================
# 6. AFISARE FILTRARE
# ============================================================

afisare.afiseaza_rezultat_filtrare(
    rezultat_filtrare
)


# ============================================================
# 7. ALEGERE DEDURIZATOR
# ============================================================

date_dedurizare = {
    "tip_proiect": date["tip_proiect"],
    "persoane": date["persoane"],
    "mod_consum": date["mod_consum"],
    "consum_zilnic": date["consum_zilnic"],
    "duritate": date["duritate"],
    "debit_proiect": debit_proiect_dedurizator
}

if (
    date.get("consum_zilnic") is None
    and date.get("persoane") is None
):
    print("\n========== DEDURIZARE ==========")
    print(
        "Nu se poate dimensiona dedurizatorul deoarece "
        "consumul zilnic nu este disponibil."
    )
    print(
        "Introdu consumul zilnic sau numarul de persoane "
        "pentru a continua dimensionarea dedurizatorului."
    )
else:
    # ============================================================
# 8. DIMENSIONARE DEDURIZATOR
# ============================================================

    if (
        date["mod_consum"] == "necunoscut"
        and date["consum_zilnic"] is None
    ):
        print("\n========== REZULTAT DEDURIZARE ==========")
        print()
        print(
            "Dedurizatorul nu poate fi dimensionat."
        )
        print()
        print(
            "Motiv: consumul zilnic nu este disponibil."
        )
        print()
        print(
            "Pentru dimensionare este necesar:"
        )
        print(
            "- consumul zilnic [m3/zi]"
        )
        print(
            "sau"
        )
        print(
            "- estimarea consumului din numarul de persoane."
        )
        print("=" * 41)

    else:

        rezultat_dedurizare = (
            calculator.calculeaza_dedurizator(
                date_dedurizare
            )
        )

        afisare.afiseaza_rezultat_dedurizare(
            rezultat_dedurizare
        )
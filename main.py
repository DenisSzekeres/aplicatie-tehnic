import user_input
import calculator


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
# El trebuie sa poata asigura debitul total calculat.

debit_proiect_dedurizator = debit_calculat


# Filtrul este inaintea rezervorului.
# Daca exista rezervor, acesta poate reduce debitul
# necesar filtrului in timpul varfului.

if date["volum_rezervor"] > 0:

    debit_proiect_filtru = (
    calculator.calculeaza_debit_proiect_cu_rezervor(
        debit_calculat,
        date["volum_rezervor"],
        date["durata_varf"]
    )
)

else:

    debit_proiect_filtru = debit_calculat


# ============================================================
# 4. AFISARE DEBITE
# ============================================================

print("\n==============================")
print("CALCUL DEBITE")
print("==============================")

print(
    f"Debit calculat: "
    f"{debit_calculat} m3/h"
)

print(
    f"Debit proiect filtru: "
    f"{debit_proiect_filtru} m3/h"
)

print(
    f"Debit proiect dedurizator: "
    f"{debit_proiect_dedurizator} m3/h"
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


print("\n==============================")
print("REZULTAT FILTRARE")
print("==============================")


print(rezultat_filtrare)


# ============================================================
# 6. ALEGERE DEDURIZATOR
# ============================================================

date_dedurizare = {
    "persoane": date["persoane"],
    "duritate": date["duritate"],
    "debit_proiect": debit_proiect_dedurizator
}


rezultat_dedurizare = (
    calculator.calculeaza_dedurizator(
        date_dedurizare
    )
)


print("\n==============================")
print("REZULTAT DEDURIZARE")
print("==============================")


print(rezultat_dedurizare)
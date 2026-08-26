import user_input
import calculator
import afisare
#citim datele
date = user_input.citeste_consum()

#Verificam daca debitul este cunoscut
if date["debit_necesar"] == 0:
    nr_consumatori = calculator.calculeaza_numar_consumatori(date)

    debit_instalat = calculator.calculeaza_debit_instalat(date)

    coeficient = calculator.calculeaza_coeficient(date)

    debit_simultan = calculator.calculeaza_debit_simultan(date)

    debit_necesar = debit_simultan

else:

    debit_necesar = date["debit_necesar"]

    nr_consumatori = None
    debit_instalat = None
    coeficient = None
    debit_simultan = None

debit_proiect = calculator.calculeaza_debit_proiect_cu_rezervor(
    debit_necesar,
    date["volum_rezervor"],
    date["durata_varf"]
)

rezultat = {
    "n": nr_consumatori,
    "debit_instalat": debit_instalat,
    "coeficient": coeficient,
    "debit_simultan": debit_simultan,
    "debit_necesar": debit_necesar,
    "debit_proiect": debit_proiect,
    "volum_rezervor": date["volum_rezervor"],
    "durata_varf": date["durata_varf"]
}

afisare.afisare_date_debite(rezultat)

print("\n========== FILTRARE ==========")
print("1. Filtrare mecanica")
print("2. Filtrare automata cu zeolita")

alegere = input("Alege tipul de filtrare: ")


if alegere == "1":

    tip_filtrare = "mecanic"

elif alegere == "2":

    tip_filtrare = "zeolita"

else:

    print("Alegere invalida.")
    exit()

rezultat_filtrare = calculator.calculeaza_filtrare(
    debit_proiect,
    tip_filtrare,
    date["ntu"]
)

afisare.afiseaza_rezultat_filtrare(
    rezultat_filtrare
)
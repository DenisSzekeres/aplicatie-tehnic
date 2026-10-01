import streamlit as st
import calculator


# ============================================================
# CONFIGURARE PAGINA
# ============================================================

st.set_page_config(
    page_title="Water Treatment Configurator",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# TEMA NAZZURO
# ============================================================

st.html(
    """
    <style>

    /* ======================================================
       VARIABILE VIZUALE
       ====================================================== */

    :root {
        --gold: #C8B58A;
        --gold-dark: #B29D70;
        --cream: #F7F6F3;
        --white: #FFFFFF;
        --text: #1A1A1A;
        --muted: #777777;
        --border: #E8E4DC;
        --success: #607A63;
        --warning: #A98245;
    }


    /* ======================================================
       FUNDAL
       ====================================================== */

    .stApp {
        background: #F7F6F3;
        color: #1A1A1A;
    }

    .main {
        background: #F7F6F3;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }


    /* ======================================================
       TEXT GENERAL
       ====================================================== */

    html,
    body,
    [class*="css"] {
        font-family:
            -apple-system,
            BlinkMacSystemFont,
            "Segoe UI",
            sans-serif;
    }

    h1,
    h2,
    h3 {
        color: #1A1A1A;
        letter-spacing: -0.02em;
    }

    p {
        color: #777777;
    }


    /* ======================================================
       HEADER
       ====================================================== */

    .app-header {
        background: #FFFFFF;
        border: 1px solid #E8E4DC;
        border-radius: 18px;
        padding: 34px 38px;
        margin-bottom: 30px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.035);
    }

    .header-eyebrow {
        color: #C8B58A;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.20em;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .header-title {
        color: #1A1A1A;
        font-size: 2.4rem;
        font-weight: 600;
        line-height: 1.1;
        margin: 0;
    }

    .header-subtitle {
        color: #777777;
        font-size: 1rem;
        margin-top: 12px;
        max-width: 720px;
        line-height: 1.6;
    }


    /* ======================================================
       SECTION TITLE
       ====================================================== */

    .section-title {
        margin-top: 28px;
        margin-bottom: 14px;
    }

    .section-eyebrow {
        color: #C8B58A;
        font-size: 0.70rem;
        font-weight: 700;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        margin-bottom: 5px;
    }

    .section-heading {
        color: #1A1A1A;
        font-size: 1.35rem;
        font-weight: 600;
        margin: 0;
    }

    .section-description {
        color: #777777;
        font-size: 0.88rem;
        margin-top: 5px;
    }


    /* ======================================================
       CARD GENERAL
       ====================================================== */

    .technical-card {
        background: #FFFFFF;
        border: 1px solid #E8E4DC;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 18px;
        box-shadow: 0 6px 24px rgba(0, 0, 0, 0.035);
    }

    .technical-card:hover {
        border-color: #D8CCB4;
    }


    /* ======================================================
       INPUT CARD
       ====================================================== */

    .input-card {
        background: #FFFFFF;
        border: 1px solid #E8E4DC;
        border-radius: 16px;
        padding: 20px 24px 8px 24px;
        margin-bottom: 18px;
        box-shadow: 0 5px 22px rgba(0, 0, 0, 0.025);
    }


    /* ======================================================
       CARD TITLU
       ====================================================== */

    .card-label {
        color: #C8B58A;
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        margin-bottom: 7px;
    }

    .card-title {
        color: #1A1A1A;
        font-size: 1.15rem;
        font-weight: 600;
        margin-bottom: 15px;
    }

    .card-model {
        color: #1A1A1A;
        font-size: 1.55rem;
        font-weight: 600;
        margin-bottom: 20px;
    }


    /* ======================================================
       METRIC CARD
       ====================================================== */

    .metric-card {
        background: #FFFFFF;
        border: 1px solid #E8E4DC;
        border-radius: 18px;
        padding: 27px 30px;
        margin-bottom: 18px;
        box-shadow: 0 7px 28px rgba(0, 0, 0, 0.04);
    }

    .metric-label {
        color: #777777;
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.14em;
        text-transform: uppercase;
    }

    .metric-value {
        color: #1A1A1A;
        font-size: 2.35rem;
        font-weight: 600;
        line-height: 1.15;
        margin-top: 7px;
    }

    .metric-unit {
        color: #C8B58A;
        font-size: 0.95rem;
        font-weight: 600;
    }


    /* ======================================================
       TECHNICAL ROW
       ====================================================== */

    .technical-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #EEEAE2;
        padding: 11px 0;
        gap: 20px;
    }

    .technical-row:last-child {
        border-bottom: none;
    }

    .technical-name {
        color: #777777;
        font-size: 0.86rem;
    }

    .technical-value {
        color: #1A1A1A;
        font-size: 0.91rem;
        font-weight: 600;
        text-align: right;
    }


    /* ======================================================
       BADGE
       ====================================================== */

    .badge {
        display: inline-block;
        border-radius: 30px;
        padding: 6px 12px;
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 14px;
    }

    .badge-gold {
        background: #F1EBDD;
        color: #806D45;
    }

    .badge-success {
        background: #EAF0EA;
        color: #536957;
    }

    .badge-warning {
        background: #F4EBDD;
        color: #8A6838;
    }


    /* ======================================================
       OBSERVATIE
       ====================================================== */

    .observation {
        background: #FAF8F3;
        border-left: 3px solid #C8B58A;
        border-radius: 0 10px 10px 0;
        padding: 14px 16px;
        margin-top: 18px;
        color: #666666;
        font-size: 0.83rem;
        line-height: 1.55;
    }


    /* ======================================================
       CALCULATE BUTTON
       ====================================================== */

    .stButton > button {
        width: 100%;
        min-height: 52px;
        border-radius: 12px;
        border: 1px solid #C8B58A;
        background: #C8B58A;
        color: #FFFFFF;
        font-size: 0.92rem;
        font-weight: 700;
        letter-spacing: 0.04em;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background: #B29D70;
        border-color: #B29D70;
        color: #FFFFFF;
    }


    /* ======================================================
       INPUTURI STREAMLIT
       ====================================================== */

    div[data-baseweb="input"] {
        border-radius: 10px;
    }

    div[data-baseweb="select"] > div {
        border-radius: 10px;
    }

    .stNumberInput label,
    .stSelectbox label,
    .stRadio label {
        color: #555555 !important;
        font-size: 0.83rem !important;
    }


    /* ======================================================
       DIVIDER
       ====================================================== */

    .gold-divider {
        height: 1px;
        background: #E8E4DC;
        margin: 30px 0;
    }


    /* ======================================================
       FOOTER
       ====================================================== */

    .app-footer {
        text-align: center;
        color: #999999;
        font-size: 0.72rem;
        margin-top: 45px;
        padding-top: 20px;
        border-top: 1px solid #E8E4DC;
    }


    /* ======================================================
       MOBILE
       ====================================================== */

    @media (max-width: 768px) {

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
            padding-top: 1rem;
        }

        .app-header {
            padding: 25px 22px;
            border-radius: 14px;
        }

        .header-title {
            font-size: 1.85rem;
        }

        .technical-card,
        .input-card,
        .metric-card {
            padding: 18px;
            border-radius: 14px;
        }

        .metric-value {
            font-size: 1.9rem;
        }

        .result-card {
            padding: 20px;
        }

        .result-card-top {
            flex-direction: column;
            gap: 10px;
        }

        .technical-grid {
            grid-template-columns: 1fr;
        }

        .final-summary {
            padding: 22px 20px;
        }

        .final-summary-grid {
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 18px 12px;
        }

    }


    /* ======================================================
       REZULTATE - CARDURI PREMIUM
       ====================================================== */

    .result-section {
        margin-top: 34px;
    }

    .compact-card {
        min-height: 150px;
    }

    .result-card {
        padding: 28px;
    }

    .result-card-top {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 20px;
        margin-bottom: 18px;
    }

    .result-card-top .badge {
        flex-shrink: 0;
        margin-top: 2px;
        margin-bottom: 0;
    }

    .result-subtitle {
        color: #777777;
        font-size: 0.88rem;
        margin-top: -12px;
        margin-bottom: 18px;
    }

    .technical-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 1px;
        background: #EEEAE2;
        border: 1px solid #EEEAE2;
        border-radius: 12px;
        overflow: hidden;
        margin-top: 18px;
    }

    .technical-mini {
        background: #FFFFFF;
        padding: 15px 16px;
        display: flex;
        flex-direction: column;
        gap: 5px;
        min-width: 0;
    }

    .technical-mini span {
        color: #888888;
        font-size: 0.74rem;
        line-height: 1.25;
    }

    .technical-mini strong {
        color: #1A1A1A;
        font-size: 0.92rem;
        font-weight: 600;
        line-height: 1.3;
        word-break: break-word;
    }

    .final-summary {
        background: #1A1A1A;
        color: #FFFFFF;
        border-radius: 18px;
        padding: 26px 28px;
        margin-top: 28px;
        box-shadow: 0 10px 35px rgba(0, 0, 0, 0.08);
    }

    .final-summary-label {
        color: #C8B58A;
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        margin-bottom: 20px;
    }

    .final-summary-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 20px;
    }

    .final-summary-grid div {
        display: flex;
        flex-direction: column;
        gap: 5px;
    }

    .final-summary-grid span {
        color: #AAAAAA;
        font-size: 0.74rem;
    }

    .final-summary-grid strong {
        color: #FFFFFF;
        font-size: 0.98rem;
        font-weight: 600;
    }

    </style>
    """)


# ============================================================
# HEADER
# ============================================================

st.html(
    """
    <div class="app-header">

        <div class="header-eyebrow">
            WATER TREATMENT
        </div>

        <div class="header-title">
            Technical Configurator
        </div>

        <div class="header-subtitle">
            Dimensionare tehnică pentru sisteme de filtrare,
            dedurizare și tratare a apei.
        </div>

    </div>
    """
)


# ============================================================
# DATE PROIECT
# ============================================================

st.html(
    """
    <div class="section-title">
        <div class="section-eyebrow">01 · PROIECT</div>
        <div class="section-heading">Date proiect</div>
        <div class="section-description">
            Stabilim tipul instalației și modul de dimensionare.
        </div>
    </div>
    """
)

#st.markdown('<div class="input-card">')

tip_proiect_afisare = st.selectbox(
    "Tip proiect",
    [
        "Rezidențial",
        "Comercial / HoReCa",
        "Industrial",
        "Alt tip de consum"
    ]
)

if tip_proiect_afisare == "Rezidențial":
    tip_proiect = "rezidential"
elif tip_proiect_afisare == "Comercial / HoReCa":
    tip_proiect = "comercial"
elif tip_proiect_afisare == "Industrial":
    tip_proiect = "industrial"
else:
    tip_proiect = "altul"

#st.markdown("</div>")


# ============================================================
# CONSUM
# ============================================================

st.html(
    """
    <div class="section-title">
        <div class="section-eyebrow">02 · CONSUM</div>
        <div class="section-heading">Necesar de apă</div>
        <div class="section-description">
            Consum zilnic cunoscut sau estimat.
        </div>
    </div>
    """
)

#st.markdown('<div class="input-card">')

persoane = None

if tip_proiect == "rezidential":

    mod_consum_afisare = st.radio(
        "Cum determinăm consumul zilnic?",
        [
            "Estimare din numărul de persoane",
            "Consum cunoscut",
            "Necunoscut"
        ],
        horizontal=True
    )

    if mod_consum_afisare == "Estimare din numărul de persoane":

        persoane = st.number_input(
            "Număr persoane",
            min_value=1,
            value=4,
            step=1
        )

        mod_consum = "estimare_persoane"
        consum_zilnic = None

    elif mod_consum_afisare == "Consum cunoscut":

        consum_zilnic = st.number_input(
            "Consum zilnic",
            min_value=0.0,
            value=0.0,
            step=0.1,
            format="%.2f"
        )

        mod_consum = "consum_cunoscut"

        if consum_zilnic <= 0:
            consum_zilnic = None

    else:

        mod_consum = "necunoscut"
        consum_zilnic = None

else:

    mod_consum_afisare = st.radio(
        "Cum determinăm consumul zilnic?",
        [
            "Consum cunoscut",
            "Necunoscut"
        ],
        horizontal=True
    )

    if mod_consum_afisare == "Consum cunoscut":

        consum_zilnic = st.number_input(
            "Consum zilnic",
            min_value=0.0,
            value=0.0,
            step=0.1,
            format="%.2f"
        )

        mod_consum = "consum_cunoscut"

        if consum_zilnic <= 0:
            consum_zilnic = None

    else:

        mod_consum = "necunoscut"
        consum_zilnic = None

#st.markdown("</div>")


# ============================================================
# DEBIT
# ============================================================

st.html(
    """
    <div class="section-title">
        <div class="section-eyebrow">03 · DEBIT</div>
        <div class="section-heading">Debit proiect</div>
        <div class="section-description">
            Introdu debitul dacă este cunoscut sau lasă aplicația să îl calculeze.
        </div>
    </div>
    """
)

#st.markdown('<div class="input-card">')

debit_necesar = st.number_input(
    "Debit necesar [m³/h]",
    min_value=0.0,
    value=0.0,
    step=0.1,
    format="%.2f"
)

if debit_necesar == 0:

    st.html(
        """
        <div style="
            color:#777;
            font-size:0.82rem;
            margin-top:5px;
            margin-bottom:12px;
        ">
            Debit necunoscut — îl vom calcula din consumatori.
        </div>
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        bai = st.number_input(
            "Băi",
            min_value=0,
            value=2,
            step=1
        )

    with col2:
        bucatarii = st.number_input(
            "Bucătării",
            min_value=0,
            value=1,
            step=1
        )

    with col3:
        electrocasnice = st.number_input(
            "Electrocasnice",
            min_value=0,
            value=1,
            step=1
        )

else:

    bai = 0
    bucatarii = 0
    electrocasnice = 0

#st.markdown("</div>")


# ============================================================
# ANALIZA APEI
# ============================================================

st.html(
    """
    <div class="section-title">
        <div class="section-eyebrow">04 · APĂ</div>
        <div class="section-heading">Analiza apei</div>
        <div class="section-description">
            Parametrii principali utilizați pentru alegerea echipamentelor.
        </div>
    </div>
    """
)

#st.markdown('<div class="input-card">')

col1, col2 = st.columns(2)

with col1:
    ntu = st.number_input(
        "Turbiditate [NTU]",
        min_value=0.0,
        value=1.0,
        step=0.1,
        format="%.2f"
    )

with col2:
    duritate = st.number_input(
        "Duritate [°HF]",
        min_value=0.0,
        value=10.0,
        step=1.0,
        format="%.1f"
    )

#st.markdown("</div>")


# ============================================================
# REZERVOR
# ============================================================

st.html(
    """
    <div class="section-title">
        <div class="section-eyebrow">05 · REZERVOR</div>
        <div class="section-heading">Rezervor tampon</div>
        <div class="section-description">
            Rezervorul este tratat ca tampon între sursă și consum.
        </div>
    </div>
    """
)

#st.markdown('<div class="input-card">')

are_rezervor = st.radio(
    "Există rezervor tampon?",
    ["Nu", "Da"],
    horizontal=True
)

if are_rezervor == "Da":

    volum_rezervor = st.number_input(
        "Volum rezervor [m³]",
        min_value=0.01,
        value=0.5,
        step=0.1,
        format="%.2f"
    )

    durata_varf = st.number_input(
        "Durata vârfului [minute]",
        min_value=1.0,
        value=20.0,
        step=1.0
    )

    ore_reumplere = st.number_input(
        "Timp dorit pentru reumplere [ore]",
        min_value=0.1,
        value=24.0,
        step=1.0
    )

else:

    volum_rezervor = 0
    durata_varf = 0
    ore_reumplere = 24

#st.markdown("</div>")


# ============================================================
# FILTRARE
# ============================================================

st.html(
    """
    <div class="section-title">
        <div class="section-eyebrow">06 · FILTRARE</div>
        <div class="section-heading">Tehnologia de filtrare</div>
        <div class="section-description">
            Alegem tipul de filtrare utilizat pentru dimensionare.
        </div>
    </div>
    """
)

#st.markdown('<div class="input-card">')

tip_filtrare_afisare = st.radio(
    "Tip filtrare",
    [
        "Filtru mecanic",
        "Filtru automat cu zeolit"
    ],
    horizontal=True
)

if tip_filtrare_afisare == "Filtru mecanic":
    tip_filtrare = "mecanic"
else:
    tip_filtrare = "zeolita"

#st.markdown("</div>")


# ============================================================
# BUTON CALCUL
# ============================================================

st.html(
    """
    <div class="gold-divider"></div>
    """
)

calculeaza = st.button(
    "CALCULEAZĂ DIMENSIONAREA",
    use_container_width=True
)


# ============================================================
# CALCUL
# ============================================================

if calculeaza:

    try:

        # ----------------------------------------------------
        # DATE
        # ----------------------------------------------------

        date = {
            "tip_proiect": tip_proiect,
            "persoane": persoane,
            "mod_consum": mod_consum,
            "consum_zilnic": consum_zilnic,
            "debit_necesar": debit_necesar,
            "bai": bai,
            "bucatarii": bucatarii,
            "electrocasnice": electrocasnice,
            "volum_rezervor": volum_rezervor,
            "durata_varf": durata_varf,
            "ore_reumplere_rezervor": ore_reumplere,
            "ntu": ntu,
            "duritate": duritate,
        }


        # ----------------------------------------------------
        # DEBIT PRINCIPAL
        # ----------------------------------------------------

        if debit_necesar > 0:

            debit_calculat = debit_necesar

        else:

            debit_calculat = calculator.calculeaza_debit_simultan(
                date
            )


        # ----------------------------------------------------
        # DEBITE DE PROIECT
        # ----------------------------------------------------

        debit_proiect_dedurizator = debit_calculat

        if volum_rezervor > 0:

            debit_proiect_filtru = (
                calculator.calculeaza_debit_proiect_cu_rezervor(
                    debit_calculat,
                    volum_rezervor,
                    durata_varf,
                    ore_reumplere
                )
            )

        else:

            debit_proiect_filtru = debit_calculat


        # ----------------------------------------------------
        # REZERVOR
        # ----------------------------------------------------

        date_rezervor = None

        if volum_rezervor > 0:

            date_rezervor = calculator.calculeaza_date_rezervor(
                debit_calculat,
                volum_rezervor,
                durata_varf,
                ore_reumplere
            )


        # ----------------------------------------------------
        # FILTRARE
        # ----------------------------------------------------

        rezultat_filtrare = calculator.calculeaza_filtrare(
            debit_proiect_filtru,
            tip_filtrare,
            ntu
        )


        # ----------------------------------------------------
        # DEDURIZARE
        # ----------------------------------------------------

        date_dedurizare = {
            "tip_proiect": tip_proiect,
            "persoane": persoane,
            "mod_consum": mod_consum,
            "consum_zilnic": consum_zilnic,
            "duritate": duritate,
            "debit_proiect": debit_proiect_dedurizator
        }

        rezultat_dedurizare = calculator.calculeaza_dedurizator(
            date_dedurizare
        )


        # ====================================================
        # REZULTATE
        # ====================================================

        st.html(
            """
            <div class="section-title">
                <div class="section-eyebrow">REZULTATE</div>
                <div class="section-heading">Dimensionare tehnică</div>
                <div class="section-description">
                    Rezultatele calculate pentru configurația introdusă.
                </div>
            </div>
            """
        )

        st.html(
            f"""
            <div class="metric-card">
                <div class="metric-label">DEBIT PROIECT</div>
                <div class="metric-value">
                    {debit_calculat:.2f}
                    <span class="metric-unit">m³/h</span>
                </div>
            </div>
            """
        )

        col1, col2 = st.columns(2)

        with col1:
            pozitionare_filtru = (
                "Înainte de rezervor"
                if volum_rezervor > 0
                else "Linia principală"
            )

            st.html(
                f"""
                <div class="technical-card compact-card">
                    <div class="card-label">FILTRARE</div>
                    <div class="card-title">Debit proiect filtru</div>

                    <div class="technical-row">
                        <span class="technical-name">Debit</span>
                        <span class="technical-value">
                            {debit_proiect_filtru:.2f} m³/h
                        </span>
                    </div>

                    <div class="technical-row">
                        <span class="technical-name">Poziționare</span>
                        <span class="technical-value">
                            {pozitionare_filtru}
                        </span>
                    </div>
                </div>
                """
            )

        with col2:
            pozitionare_dedurizator = (
                "După rezervor"
                if volum_rezervor > 0
                else "Linia principală"
            )

            st.html(
                f"""
                <div class="technical-card compact-card">
                    <div class="card-label">DEDURIZARE</div>
                    <div class="card-title">Debit proiect dedurizator</div>

                    <div class="technical-row">
                        <span class="technical-name">Debit</span>
                        <span class="technical-value">
                            {debit_proiect_dedurizator:.2f} m³/h
                        </span>
                    </div>

                    <div class="technical-row">
                        <span class="technical-name">Duritate</span>
                        <span class="technical-value">
                            {duritate:.1f} °HF
                        </span>
                    </div>

                    <div class="technical-row">
                        <span class="technical-name">Poziționare</span>
                        <span class="technical-value">
                            {pozitionare_dedurizator}
                        </span>
                    </div>
                </div>
                """
            )

        st.html(
            """
            <div class="section-title result-section">
                <div class="section-eyebrow">FILTRARE</div>
                <div class="section-heading">Filtru recomandat</div>
            </div>
            """
        )

        if rezultat_filtrare.get("status") == "ok":

            filtru = rezultat_filtrare["rezultat"]

            model_filtru = filtru.get("model", "-")
            echipament_filtru = filtru.get("echipament", "-")
            debit_filtru_proiect = filtru.get("debit_proiect", "-")
            observatie_filtru = filtru.get("observatie")

            rows_filtru = f"""
                <div class="technical-row">
                    <span class="technical-name">Echipament</span>
                    <span class="technical-value">{echipament_filtru}</span>
                </div>

                <div class="technical-row">
                    <span class="technical-name">Debit proiect</span>
                    <span class="technical-value">{debit_filtru_proiect} m³/h</span>
                </div>
            """

            if "debit_filtru" in filtru:
                rows_filtru += f"""
                <div class="technical-row">
                    <span class="technical-name">Debit filtru</span>
                    <span class="technical-value">
                        {filtru.get("debit_filtru", "-")} m³/h
                    </span>
                </div>

                <div class="technical-row">
                    <span class="technical-name">Rezervă</span>
                    <span class="technical-value">
                        {filtru.get("rezerva_procent", "-")} %
                    </span>
                </div>

                <div class="technical-row">
                    <span class="technical-name">Racord</span>
                    <span class="technical-value">
                        {filtru.get("racord", "-")}
                    </span>
                </div>
                """

            elif "viteza_filtrare" in filtru:
                rows_filtru += f"""
                <div class="technical-grid">
                    <div class="technical-mini">
                        <span>Viteză filtrare</span>
                        <strong>{filtru.get("viteza_filtrare", "-")} m/h</strong>
                    </div>

                    <div class="technical-mini">
                        <span>Debit filtrare</span>
                        <strong>{filtru.get("debit_filtrare", "-")} m³/h</strong>
                    </div>

                    <div class="technical-mini">
                        <span>Rezervă</span>
                        <strong>{filtru.get("rezerva_procent", "-")} %</strong>
                    </div>

                    <div class="technical-mini">
                        <span>Butelie</span>
                        <strong>{filtru.get("butelie", "-")}</strong>
                    </div>

                    <div class="technical-mini">
                        <span>Racord</span>
                        <strong>{filtru.get("racord", "-")}</strong>
                    </div>

                    <div class="technical-mini">
                        <span>Zeolit</span>
                        <strong>
                            {filtru.get("zeolit_l", "-")} L /
                            {filtru.get("zeolit_kg", "-")} kg
                        </strong>
                    </div>

                    <div class="technical-mini">
                        <span>Debit spălare</span>
                        <strong>{filtru.get("debit_spalare", "-")} m³/h</strong>
                    </div>
                </div>
                """

            observation_filtru = (
                f'<div class="observation">{observatie_filtru}</div>'
                if observatie_filtru
                else ""
            )

            st.html(
                f"""
                <div class="technical-card result-card">

                    <div class="result-card-top">
                        <div>
                            <div class="card-label">ECHIPAMENT DE FILTRARE</div>
                            <div class="card-model">{model_filtru}</div>
                        </div>

                        <span class="badge badge-success">
                            COMPATIBIL
                        </span>
                    </div>

                    <div class="result-subtitle">
                        {echipament_filtru}
                    </div>

                    {rows_filtru}

                    {observation_filtru}

                </div>
                """
            )

        else:
            st.error(
                rezultat_filtrare.get(
                    "mesaj",
                    "Nu a fost identificat un filtru compatibil."
                )
            )

        st.html(
            """
            <div class="section-title result-section">
                <div class="section-eyebrow">DEDURIZARE</div>
                <div class="section-heading">Dedurizator recomandat</div>
            </div>
            """
        )

        status_dedurizator = rezultat_dedurizare.get("status")

        if status_dedurizator in ["ok", "partial"]:

            r = rezultat_dedurizare.get("rezultat", {})

            if status_dedurizator == "partial":
                badge_text = "DIMENSIONARE HIDRAULICĂ"
                badge_class = "badge-warning"
            else:
                badge_text = "DIMENSIONARE COMPLETĂ"
                badge_class = "badge-success"

            rows_dedurizator = f"""
                <div class="technical-row">
                    <span class="technical-name">Debit proiect</span>
                    <span class="technical-value">
                        {r.get("debit_proiect", "-")} m³/h
                    </span>
                </div>

                <div class="technical-row">
                    <span class="technical-name">Debit echipament</span>
                    <span class="technical-value">
                        {r.get("debit_echipament", r.get("debit_lucru", "-"))} m³/h
                    </span>
                </div>

                <div class="technical-row">
                    <span class="technical-name">Duritate</span>
                    <span class="technical-value">
                        {r.get("duritate", "-")} °HF
                    </span>
                </div>
            """

            extra_rows = ""

            optional_rows = [
                ("Capacitate între regenerări",
                 r.get("capacitate_intre_regenerari_l"),
                 lambda x: f"{x} L"),
                ("Capacitate",
                 r.get("capacitate_intre_regenerari_m3"),
                 lambda x: f"{x} m³"),
                ("Regenerări / zi",
                 r.get("regenerari_zi"),
                 lambda x: f"{x}"),
                ("Zile între regenerări",
                 r.get("zile_intre_regenerari"),
                 lambda x: f"{x}"),
                ("Disc duritate",
                 r.get("disc"),
                 lambda x: f"{x}"),
                ("Configurație",
                 r.get("configuratie"),
                 lambda x: f"{x}"),
                ("Mod dimensionare debit",
                 r.get("mod_dimensionare_debit"),
                 lambda x: f"{x}"),
                ("Debit maxim",
                 r.get("debit_maxim"),
                 lambda x: f"{x} m³/h"),
                ("Capacitate echipament",
                 r.get("capacitate_echipament_hf_m3"),
                 lambda x: f"{x} °HF × m³"),
                ("Rezervă capacitate",
                 r.get("rezerva_capacitate_procent"),
                 lambda x: f"{x} %"),
                ("Sare / regenerare",
                 r.get("sare_regenerare_kg"),
                 lambda x: f"{x} kg"),
            ]

            for label, value, formatter in optional_rows:
                if value is not None:
                    extra_rows += f"""
                    <div class="technical-row">
                        <span class="technical-name">{label}</span>
                        <span class="technical-value">{formatter(value)}</span>
                    </div>
                    """

            observation_dedurizator = (
                f'<div class="observation">{r["observatie"]}</div>'
                if r.get("observatie")
                else ""
            )

            st.html(
                f"""
                <div class="technical-card result-card">

                    <div class="result-card-top">
                        <div>
                            <div class="card-label">DEDURIZATOR</div>
                            <div class="card-model">
                                {r.get("model", "-")}
                            </div>
                        </div>

                        <span class="badge {badge_class}">
                            {badge_text}
                        </span>
                    </div>

                    {rows_dedurizator}

                    {extra_rows}

                    {observation_dedurizator}

                </div>
                """
            )

        elif status_dedurizator == "partial_negasit":

            st.warning(
                rezultat_dedurizare.get(
                    "mesaj",
                    "Nu a fost identificat un dedurizator compatibil."
                )
            )

        else:

            st.error(
                rezultat_dedurizare.get(
                    "mesaj",
                    "Nu a fost identificat un dedurizator compatibil."
                )
            )

        if date_rezervor is not None:

            st.html(
                """
                <div class="section-title result-section">
                    <div class="section-eyebrow">REZERVOR</div>
                    <div class="section-heading">
                        Dimensionare rezervor tampon
                    </div>
                </div>
                """
            )

            st.html(
                f"""
                <div class="technical-card result-card">

                    <div class="result-card-top">
                        <div>
                            <div class="card-label">REZERVOR TAMPON</div>
                            <div class="card-model">
                                {volum_rezervor:.2f} m³
                            </div>
                        </div>

                        <span class="badge badge-gold">
                            CONFIGURAT
                        </span>
                    </div>

                    <div class="technical-grid">

                        <div class="technical-mini">
                            <span>Durata vârfului</span>
                            <strong>{durata_varf:.0f} minute</strong>
                        </div>

                        <div class="technical-mini">
                            <span>Consum în perioada de vârf</span>
                            <strong>
                                {date_rezervor["volum_consum_varf"]:.2f} m³
                            </strong>
                        </div>

                        <div class="technical-mini">
                            <span>Rezervă disponibilă</span>
                            <strong>
                                {date_rezervor["rezerva_volum"]:.2f} m³
                            </strong>
                        </div>

                        <div class="technical-mini">
                            <span>Debit reumplere</span>
                            <strong>
                                {date_rezervor["debit_reumplere"]:.2f} m³/h
                            </strong>
                        </div>

                        <div class="technical-mini">
                            <span>Autonomie la vârf</span>
                            <strong>
                                {date_rezervor["autonomie_varf"]:.2f} h
                            </strong>
                        </div>

                    </div>

                </div>
                """
            )

        st.html(
            f"""
            <div class="final-summary">

                <div class="final-summary-label">
                    CONFIGURAȚIE PROIECT
                </div>

                <div class="final-summary-grid">

                    <div>
                        <span>Debit</span>
                        <strong>{debit_calculat:.2f} m³/h</strong>
                    </div>

                    <div>
                        <span>Turbiditate</span>
                        <strong>{ntu:.2f} NTU</strong>
                    </div>

                    <div>
                        <span>Duritate</span>
                        <strong>{duritate:.1f} °HF</strong>
                    </div>

                    <div>
                        <span>Rezervor</span>
                        <strong>
                            {
                                f"{volum_rezervor:.2f} m³"
                                if volum_rezervor > 0
                                else "Fără rezervor"
                            }
                        </strong>
                    </div>

                </div>

            </div>
            """
        )

    except Exception as e:

        st.error(
            f"A apărut o eroare: {e}"
        )


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="app-footer">
        Water Treatment Technical Configurator
        · Technical Dimensioning
    </div>
    """
)
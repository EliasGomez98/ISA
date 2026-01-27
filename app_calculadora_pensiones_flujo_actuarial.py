import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="CEIP: Capital semilla y aportes capitalizables", layout="wide")

# --- MODELO DE MORTALIDAD (Tablas SPP-2025-S) ---
q_hombres = np.array([5.03940441e-03, 3.46560981e-04, 3.24551757e-04, 2.94943411e-04, 2.60475316e-04, 2.23760630e-04, 1.86883138e-04, 1.52672598e-04, 1.22969336e-04, 9.96950011e-05, 8.48315434e-05, 8.06616603e-05, 9.06884446e-05, 1.20166096e-04, 1.76206656e-04, 2.67840964e-04, 3.52324554e-04, 4.33768281e-04, 5.04452933e-04, 5.59512306e-04, 6.19850609e-04, 6.53317023e-04, 6.65194866e-04, 6.62101937e-04, 6.50192810e-04, 6.34583634e-04, 6.19450216e-04, 6.07461846e-04, 5.99871931e-04, 5.96806480e-04, 5.97630105e-04, 6.01395192e-04, 6.07234551e-04, 6.14653791e-04, 6.23719615e-04, 6.34728401e-04, 6.47645406e-04, 6.61920814e-04, 6.76973759e-04, 6.92740774e-04, 7.09664637e-04, 7.28306091e-04, 7.49128249e-04, 7.72628131e-04, 7.99423244e-04, 8.30235684e-04, 8.65810569e-04, 9.06963797e-04, 9.54598470e-04, 1.00969386e-03, 1.07318796e-03, 1.14589886e-03, 1.22842315e-03, 1.32108604e-03, 1.42395750e-03, 1.53700628e-03, 1.66029054e-03, 1.79420766e-03, 1.93976303e-03, 2.09888391e-03, 2.27453628e-03, 2.47079474e-03, 2.69286976e-03, 2.94715228e-03, 3.24092633e-03, 3.58205516e-03, 3.97830944e-03, 4.43619561e-03, 4.95954585e-03, 5.54914023e-03, 6.20313974e-03, 6.91687723e-03, 7.68250023e-03, 8.49294350e-03, 9.34798822e-03, 1.02531107e-02, 1.12139401e-02, 1.22344176e-02, 1.33255102e-02, 1.45115013e-02, 1.58195548e-02, 1.72738809e-02, 1.89013401e-02, 2.07163406e-02, 2.27196924e-02, 2.49116994e-02, 2.72901126e-02, 2.98683385e-02, 3.26658882e-02, 3.57012879e-02, 3.90248589e-02, 4.57601232e-02, 5.36909587e-02, 6.26063082e-02, 7.31191617e-02, 8.52321165e-02, 9.91396984e-02, 1.15060379e-01, 1.33240680e-01, 1.53959588e-01, 1.77533386e-01, 2.04321057e-01, 2.34730372e-01, 2.69224805e-01, 3.08331430e-01, 3.52649956e-01, 3.71543161e-01, 3.90545633e-01, 4.09628615e-01, 4.28766004e-01, 1.00000000e+00])

q_mujeres = np.array([3.28401115e-03, 2.48698449e-04, 2.18468949e-04, 1.84235210e-04, 1.51723433e-04, 1.23259870e-04, 1.00373723e-04, 8.34064961e-05, 7.16928800e-05, 6.45448135e-05, 6.09952836e-05, 6.03111637e-05, 6.16858602e-05, 6.51867706e-05, 7.09168073e-05, 8.03599609e-05, 8.82498788e-05, 9.65069278e-05, 1.05067123e-04, 1.13606999e-04, 1.22241114e-04, 1.31035453e-04, 1.40046533e-04, 1.49544218e-04, 1.59748899e-04, 1.70650764e-04, 1.83620191e-04, 1.92341051e-04, 1.98159106e-04, 2.02962855e-04, 2.08733001e-04, 2.17176368e-04, 2.29439630e-04, 2.45616641e-04, 2.64994028e-04, 2.86401967e-04, 3.08348193e-04, 3.29293979e-04, 3.48157963e-04, 3.64837167e-04, 3.80275690e-04, 3.95926415e-04, 4.13142968e-04, 4.32790785e-04, 4.55090935e-04, 4.79792095e-04, 5.06584789e-04, 5.35606386e-04, 5.67662205e-04, 6.04081934e-04, 6.46177082e-04, 6.94597786e-04, 7.48859403e-04, 8.07337942e-04, 8.67709899e-04, 9.27869957e-04, 9.87067511e-04, 1.04688784e-03, 1.11160321e-03, 1.18783094e-03, 1.28347169e-03, 1.40623729e-03, 1.56221520e-03, 1.75481125e-03, 1.98422695e-03, 2.24758137e-03, 2.53992507e-03, 2.85523585e-03, 3.18773085e-03, 3.53413659e-03, 3.89546375e-03, 4.27374321e-03, 4.66973902e-03, 5.08951425e-03, 5.54614663e-03, 6.04909444e-03, 6.60481705e-03, 7.22335774e-03, 7.91634793e-03, 8.70413264e-03, 9.61372709e-03, 1.06693579e-02, 1.18965545e-02, 1.33086886e-02, 1.49105176e-02, 1.67091020e-02, 1.87024831e-02, 2.08995105e-02, 2.33173188e-02, 2.59526379e-02, 2.88260585e-02, 3.44007851e-02, 4.09302574e-02, 4.85329405e-02, 5.73293010e-02, 6.76123547e-02, 7.96173972e-02, 9.35751692e-02, 1.09788895e-01, 1.28609460e-01, 1.50443082e-01, 1.75760253e-01, 2.05106172e-01, 2.39112922e-01, 2.78513692e-01, 3.24159406e-01, 3.45335222e-01, 3.67228247e-01, 3.89838481e-01, 4.13165924e-01, 1.00000000e+00])

# --- CÁLCULO ACTUARIAL ---
def calcular_vpa_interno(sexo, tasa, tipo_renta, frec_nombre, años_t, jubilacion):
    v = 1 / (1 + tasa)
    q_x = q_hombres if sexo == "Masculino" else q_mujeres
    p_x = 1 - q_x
    map_frec = {"Mensual": 12, "Bimestral": 6, "Trimestral": 4, "Anual": 1}
    k = map_frec[frec_nombre]
    factor_anualidad = 0
    t_p_jub = 1.0
    if tipo_renta == "Vitalicia":
        for t in range(jubilacion, 111):
            factor_anualidad += t_p_jub * (v**(t - jubilacion))
            if t < 110: t_p_jub *= p_x[t]
        factor_anualidad = factor_anualidad - ((k - 1) / (2 * k))
    else:
        for t in range(int(años_t)):
            factor_anualidad += (v**t)
        factor_anualidad = factor_anualidad - ((k - 1) / (2 * k)) * (1 - v**años_t)

    return factor_anualidad, k

def obtener_prob_supervivencia(edad_final, q_x):
    prob = 1.0
    for i in range(0, edad_final):
        prob *= (1 - q_x[i])
    return prob

# --- INTERFAZ ---
st.image("https://upload.wikimedia.org/wikipedia/commons/8/8d/SBS_logotipo.svg", width=500)
st.title("🏦 CEIP - Simulador Actuarial")
st.markdown("En cumplimiento de la Resolución SBS N.° 04043-2025, se pone a disposición del CEIP una herramienta de cálculo actuarial del capital semilla y del aporte mensual, orientada a establecer una alternativa sostenible a la pensión no contributiva Pensión 65.")

with st.sidebar:
    st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/8/8d/SBS_logotipo.svg" class="sidebar-logo" width="200">', unsafe_allow_html=True)
    st.header("⚙️ Configuración")
    modo_calculo = st.radio("Modo de Cálculo:", ["Definir pensión objetivo", "Definir inversión/aporte"], index=1)

    with st.expander("👤 Perfil del Beneficiario", expanded=True):
        sexo = st.selectbox("Sexo:", ["Masculino", "Femenino"], index=1)
        edad_jub = st.slider("Edad de Jubilación:", 50, 75, 65)

        st.subheader("Periodo de Aporte")
        edad_inicio_aporte = st.slider("Comienzo de aporte (edad):", 0, 25, 6)
        edad_fin_aporte = st.slider("Fin de aporte (edad):", edad_inicio_aporte + 1, 40, 18)
        años_aporte = edad_fin_aporte - edad_inicio_aporte

    with st.expander("📈 Parámetros Financieros"):
        st.subheader("Ingresar Tasas de Acumulación y Descuento")
        
        # Tasa Acumulación (Durante el ahorro)
        t_acum = st.number_input(
                "Tasa Acumulación (Ahorro)",
                min_value=0.0,
                max_value=20.0,
                value=4.3,
                step=0.1,
                format="%.2f"
            ) / 100
        
        # Tasa Jubilación (Para la renta)
        t_jub = st.number_input(
                "Tasa Descuento (Renta)",
                min_value=0.0,
                max_value=20.0,
                value=4.3,
                step=0.1,
                format="%.2f"
            ) / 100

        st.subheader("Tipo de Pensión")
        frecuencia_pension = st.selectbox("Frecuencia:", ["Mensual", "Bimestral", "Trimestral", "Anual"], index=1)
        tipo_pension = st.selectbox("Tipo:", ["Vitalicia", "Temporal"], index=0)
        años_t_temporal = st.number_input("Años (si es temporal):", value=20)

# --- PROCESAMIENTO ---
q_x = q_hombres if sexo == "Masculino" else q_mujeres
f_anualidad, k_pagos = calcular_vpa_interno(sexo, t_jub, tipo_pension, frecuencia_pension, años_t_temporal, edad_jub)

if modo_calculo == "Definir pensión objetivo":
    monto_pension_obj = st.number_input(f"Pensión deseada ({frecuencia_pension}) (S/):", value=350.0)
    fondo_necesario = (monto_pension_obj * k_pagos) * f_anualidad
    
    # 1. Capital Semilla
    cap_semilla = fondo_necesario / ((1 + t_acum)**edad_jub)
    
    # 2. Aporte periódico
    denominador_actuarial = 0
    for t in range(edad_inicio_aporte, edad_fin_aporte):
        p_t = obtener_prob_supervivencia(t, q_x)
        denominador_actuarial += p_t * ((1 + t_acum)**(edad_jub - t))
    
    monto_aporte_mensual = (fondo_necesario / denominador_actuarial) / 12

    st.divider()
    c1, c2 = st.columns(2)
    c1.metric("Capital Semilla Necesario", f"S/ {cap_semilla:,.2f}")
    c2.metric("Aporte Mensual Necesario", f"S/ {monto_aporte_mensual:,.2f}")

else:
    col_a, col_b = st.columns(2)
    with col_a:
        input_cap_semilla = st.number_input("Capital Semilla (S/):", value=5500.0)
    with col_b:
        input_aporte_mensual = st.number_input("Aporte Mensual (S/):", value=55.0)
    
    # Fondo desde Semilla
    fondo_semilla = input_cap_semilla * ((1 + t_acum)**edad_jub)
    pension_semilla = (fondo_semilla / f_anualidad) / k_pagos
    
    # Fondo desde Aportes (Actuarial)
    fondo_mensual_esperado = 0
    for t in range(edad_inicio_aporte, edad_fin_aporte):
        p_t = obtener_prob_supervivencia(t, q_x)
        fondo_mensual_esperado += (input_aporte_mensual * 12) * p_t * ((1 + t_acum)**(edad_jub - t))
    
    pension_mensual = (fondo_mensual_esperado / f_anualidad) / k_pagos
    
    cap_semilla = input_cap_semilla
    monto_aporte_mensual = input_aporte_mensual

# --- CÁLCULO VALOR ACTUARIAL (VALOR PRESENTE) ---
    tasa_mensual = (1 + t_acum)**(1/12) - 1
    total_meses = años_aporte * 12
    vpa_aportes = 0.0
    prob_supervivencia_acum = 1.0

    for mes in range(1, total_meses + 1):
        # Usamos la edad de inicio de aporte como base
        indice_edad = edad_inicio_aporte + ((mes - 1) // 12)
        if (mes - 1) % 12 == 0 and mes > 1:
            prob_supervivencia_acum *= (1 - q_x[indice_edad - 1])
        
        v_k = (1 + tasa_mensual)**-mes
        vpa_aportes += input_aporte_mensual * v_k * prob_supervivencia_acum

    st.divider()
    st.subheader("📊 Comparativa de Resultados")
    data_resumen = {
        "Concepto": ["Fondo Proyectado", f"Pensión {frecuencia_pension}", "Valor Actuarial (VP)"],
        "Capital Semilla": [f"S/ {fondo_semilla:,.2f}", f"S/ {pension_semilla:,.2f}", f"S/ {input_cap_semilla:,.2f}"],
        "Aportes Mensuales": [f"S/ {fondo_mensual_esperado:,.2f}", f"S/ {pension_mensual:,.2f}", f"S/ {vpa_aportes:,.2f}"]
    }
    st.table(pd.DataFrame(data_resumen))

    tasa_mensual = (1 + t_acum)**(1/12) - 1
    total_meses = años_aporte * 12
    # Fórmula de Valor Presente de una anualidad ordinaria
    if tasa_mensual > 0:
        vpa_aportes = input_aporte_mensual * ((1 - (1 + tasa_mensual)**-total_meses) / tasa_mensual)
    else:
        vpa_aportes = input_aporte_mensual * total_meses

# --- GRÁFICO PROYECCIÓN ---
st.subheader("📈 Crecimiento del fondo")
edades = np.arange(0, edad_jub + 1)
progreso_semilla = [cap_semilla * (1 + t_acum)**t for t in edades]
progreso_mensual = []
acum_m = 0
for t in edades:
    if edad_inicio_aporte <= t < edad_fin_aporte:
        p_t = obtener_prob_supervivencia(t, q_x)
        acum_m = (acum_m + (monto_aporte_mensual * 12) * p_t) * (1 + t_acum)
    elif t >= edad_fin_aporte:
        acum_m *= (1 + t_acum)
    else:
        acum_m = 0
    progreso_mensual.append(acum_m)

df_progreso = pd.DataFrame({
    "Capital semilla": progreso_semilla,
    "Aportes mensuales": progreso_mensual
}, index=edades).round(2)

#st.line_chart(df_progreso)

st.area_chart(df_progreso, color=["#06369d", "#64b5f6"])

st.caption("Nota: Los cálculos incluyen probabilidades de supervivencia según Tablas SPP-2025.")

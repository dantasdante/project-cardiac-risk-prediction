import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os
from pathlib import Path # Importe Pathlib

# --- Configurações da Página ---
st.set_page_config(
    page_title="Previsão de Doenças Cardíacas",
    page_icon="❤️",
    layout="centered"
)

# --- Definir os caminhos dos arquivos de forma robusta ---
# Base do diretório onde app.py está localizado (que é 'src/')
BASE_DIR = Path(__file__).parent

# Caminhos completos para os arquivos .pkl
MODEL_PATH = BASE_DIR / "mdl.pkl"
COLUMN_TRANSFORMER_PATH = BASE_DIR / "column_transformer.pkl"
SCALER_PATH = BASE_DIR / "scaler.pkl"

model = None
column_transformer = None
scaler = None

# Tenta carregar o ColumnTransformer
if os.path.exists(COLUMN_TRANSFORMER_PATH):
    try:
        column_transformer = joblib.load(COLUMN_TRANSFORMER_PATH)
    except Exception as e:
        st.error(f"Erro ao carregar o ColumnTransformer: {e}. O aplicativo pode não funcionar corretamente.")
        st.stop()
else:
    st.error(f"Erro: Arquivo do ColumnTransformer '{COLUMN_TRANSFORMER_PATH}' não encontrado. Certifique-se de que está no diretório correto.")
    st.stop()

# Tenta carregar o MinMaxScaler
if os.path.exists(SCALER_PATH):
    try:
        scaler = joblib.load(SCALER_PATH)
    except Exception as e:
        st.error(f"Erro ao carregar o MinMaxScaler: {e}. O aplicativo pode não funcionar corretamente.")
        st.stop()
else:
    st.error(f"Erro: Arquivo do MinMaxScaler '{SCALER_PATH}' não encontrado. Certifique-se de que está no diretório correto.")
    st.stop()

# Tenta carregar o Modelo
if os.path.exists(MODEL_PATH):
    try:
        model = joblib.load(MODEL_PATH)
    except Exception as e:
        st.error(f"Erro ao carregar o modelo: {e}. O aplicativo pode não funcionar corretamente.")
        st.stop()
else:
    st.error(f"Erro: Arquivo do modelo '{MODEL_PATH}' não encontrado. Certifique-se de que está no diretório correto.")
    st.stop()

# --- Título e Descrição da Aplicação ---
st.title("Sistema de Previsão de Doenças Cardíacas")
st.markdown("""
    Este aplicativo prediz a probabilidade de um indivíduo ter doença cardíaca
    com base em suas características de saúde. **Por favor, preencha os campos abaixo:**
""")

st.write("---")

# --- 2. Coleta de Entradas do Usuário ---
st.header("Dados do Paciente:")

col1, col2 = st.columns(2)

# Mapear as posições originais das colunas para os nomes que você usou no Streamlit
# Ajuste conforme a ordem original das colunas na sua base de dados 'features'
# [0] Idade, [1] Sexo, [2] Tipo de Dor no Peito, [3] Pressão Arterial, [4] Colesterol,
# [5] Glicemia em Jejum, [6] Eletrocardiograma, [7] Frequência Cardíaca Máxima,
# [8] Angina Exercício, [9] Oldpeak, [10] Inclinação ST
with col1:
    age = st.number_input("Idade", min_value=1, max_value=120, step=1, value=50, key="age_input")
    restingBP = st.number_input("Pressão Arterial em Repouso (mm/Hg)", min_value=50, max_value=200, step=1, value=120, key="restingBP_input")
    cholesterol = st.number_input("Colesterol (mg/dl)", min_value=100, max_value=600, step=1, value=200, key="cholesterol_input")
    maxHR = st.number_input("Frequência Cardíaca Máxima", min_value=50, max_value=250, step=1, value=150, key="maxHR_input")
    oldpeak = st.number_input("Oldpeak (Depressão do ST)", min_value=0.0, max_value=10.0, step=0.1, value=1.0, key="oldpeak_input")

with col2:
    sex = st.radio("Sexo", ["Masculino", "Feminino"], horizontal=True, key="sex_input")
    chest_pain_type = st.selectbox("Tipo de Dor no Peito", ["ASY", "ATA", "NAP", "TA"], index=0, key="cp_input")
    resting_ecg = st.selectbox("Eletrocardiograma em Repouso", ["LVH", "Normal", "ST"], index=1, key="ecg_input")
    fastingBS = st.radio("Glicemia em Jejum > 120 mg/dl?", ["Não", "Sim"], horizontal=True, key="fbs_input")
    exercise_angina = st.radio("Angina Induzida por Exercício?", ["Não", "Sim"], horizontal=True, key="exang_input")
    st_slope = st.selectbox("Inclinação do Segmento ST", ["Down", "Flat", "Up"], index=1, key="slope_input")

st.write("---")

# --- 3. Função para Preparar Dados e Fazer Previsão ---
def fazer_previsao(age, sex, chest_pain_type, restingBP, cholesterol, fastingBS, maxHR, exercise_angina, oldpeak, st_slope, resting_ecg, column_transformer, scaler, model):
    # Crie um array numpy com os dados na ordem original das suas 'features'
    # Use 0 ou 1 para categorias que não são One-Hot Encoded ainda.
    # Exemplo: 'Não' -> 0, 'Sim' -> 1
    sex_val = "M" if sex == "Masculino" else "F" # Ou 0/1 se for o caso
    fastingBS_val = 1 if fastingBS == "Sim" else 0
    exercise_angina_val = "Y" if exercise_angina == "Sim" else "N" # Ou 0/1 se for o caso

    # ATENÇÃO: Esta é a ordem ORIGINAL das colunas que seu ColumnTransformer espera!
    # Ajuste os valores abaixo para corresponder à ordem exata das suas 'features' originais
    # Exemplo: se features.iloc[:,0] é 'age', features.iloc[:,1] é 'sex', etc.
    input_array_original = np.array([[
        age,                         # col 0
        sex_val,                     # col 1 (categórica)
        chest_pain_type,             # col 2 (categórica)
        restingBP,                   # col 3
        cholesterol,                 # col 4
        fastingBS_val,               # col 5
        resting_ecg,                 # col 6 (categórica)
        maxHR,                       # col 7
        exercise_angina_val,         # col 8 (categórica)
        oldpeak,                     # col 9
        st_slope                     # col 10 (categórica)
    ]])

    # 1. Aplicar o ColumnTransformer
    try:
        # column_transformer.transform espera um array 2D
        transformed_data = column_transformer.transform(input_array_original)
    except Exception as e:
        st.error(f"Erro ao aplicar o ColumnTransformer: {e}. Verifique a ordem e os tipos das entradas.")
        return None, None

    # 2. Aplicar o MinMaxScaler
    try:
        final_processed_data = scaler.transform(transformed_data)
    except Exception as e:
        st.error(f"Erro ao aplicar o MinMaxScaler: {e}. Verifique se os dados estão na escala correta após o ColumnTransformer.")
        return None, None

    # 3. Fazer a previsão com o modelo
    if model is not None:
        try:
            predicao = model.predict(final_processed_data)
            if hasattr(model, 'predict_proba'):
                prob_positiva = model.predict_proba(final_processed_data)[0][1]
                return predicao[0], prob_positiva
            else:
                return predicao[0], None
        except Exception as e:
            st.error(f"Erro ao fazer a previsão com o modelo: {e}. Verifique se o modelo foi treinado com o formato de dados esperado.")
            return None, None
    else:
        st.error("Modelo não carregado. Não é possível fazer a previsão.")
        return None, None

# --- 4. Botão para Fazer a Previsão ---
if st.button("Prever Doença Cardíaca", type="primary"):
    if model and column_transformer and scaler: # Verifica se todos os objetos foram carregados
        predicao_resultado, probabilidade = fazer_previsao(
            age, sex, chest_pain_type, restingBP, cholesterol, fastingBS,
            maxHR, exercise_angina, oldpeak, st_slope, resting_ecg,
            column_transformer, scaler, model
        )

        st.subheader("Resultado da Previsão:")
        if predicao_resultado is not None:
            if predicao_resultado == 1:
                st.error("🚨 **ALERTA!** De acordo com os dados fornecidos, há uma **ALTA PROBABILIDADE** de o paciente ter doença cardíaca.")
                if probabilidade is not None:
                    st.write(f"Probabilidade estimada: **{probabilidade*100:.2f}%**")
                st.warning("⚠️ **Recomendação:** É **altamente aconselhável** procurar um médico para uma avaliação e diagnóstico profissional.")
            else:
                st.success("✅ De acordo com os dados fornecidos, o paciente **não apresenta alta probabilidade** de ter doença cardíaca.")
                if probabilidade is not None:
                    st.write(f"Probabilidade estimada (de ter doença cardíaca): **{probabilidade*100:.2f}%**")
                st.info("ℹ️ **Lembrete:** Este é um resultado de modelo preditivo e **não substitui** o diagnóstico médico. Continue com exames de rotina.")
        else:
            st.warning("Não foi possível gerar uma previsão. Por favor, verifique os dados e tente novamente.")
    else:
        st.warning("Componentes essenciais do modelo (ColumnTransformer, MinMaxScaler, ou o Modelo) não foram carregados corretamente. Por favor, tente recarregar a página ou verifique os arquivos.")

st.write("---")
st.caption("Aviso: Esta aplicação é apenas para fins demonstrativos e não deve ser utilizada para diagnóstico médico. Consulte sempre um profissional de saúde qualificado.")

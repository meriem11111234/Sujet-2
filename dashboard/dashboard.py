import streamlit as st
import pandas as pd
import psycopg2

conn = psycopg2.connect("dbname=fraud user=user password=password")
df = pd.read_sql("SELECT * FROM fraud_transactions ORDER BY detected_at DESC", conn)

st.title("📈 Tableau de Fraudes")
st.dataframe(df)

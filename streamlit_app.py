import pandas as pd
import streamlit as st
import os

st.write("""# Ergo token rich-lists""")
st.write("""Last scan: Feb 12, 2022""")

tokens = [i.replace('.csv','') for i in os.listdir('dataframes')]

token = st.radio("Select a token:", tokens)

df = pd.read_csv('dataframes/%s.csv'%token)
df = df.drop(columns=[i for i in df.columns.values if 'unnamed' in i.lower()])

st.write("Rich-list for %s"%token)
st.dataframe(df)


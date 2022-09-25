import streamlit as st
from sklearn.datasets import load_wine
import plotly.express as px
import pandas as pd
wine_data = load_wine()
labels = wine_data.feature_names
targets = wine_data.target
print(labels)
df_form = pd.DataFrame(wine_data.data, columns = labels)
df_form['targets'] = targets
st.write("""
# Italian Wine Dataset
How are malic acid and alcohol correlated in Italian wines?
""")
fig = px.scatter(df_form, x="alcohol", y="malic_acid")
# fig.show()
st.plotly_chart(fig)
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# st.title("Streamlit: Build and Share Data Apps")
st.markdown("## Streamlit: Build and Share Data Apps", unsafe_allow_html=True)


link  =  "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_car  =  pd.read_csv(link)

# creation du bouton de filtre appliqué à la page entière
selected_continents  =  st.multiselect("Select continents", df_car['continent'].unique(), default = df_car['continent'].unique())
filtered_df = df_car[df_car['continent'].isin(selected_continents)]

# lecture du df entier
st.write(filtered_df)

# heatmap pour recherche de corrélation
st.write("Recherche de corrélation")
correlation_matrix = filtered_df.select_dtypes(include=['float64', 'int64']).corr()
fig, ax = plt.subplots()
sns.heatmap(correlation_matrix, center=0, cmap="vlag", annot = True)
st.pyplot(fig)

# corrélation négative
st.write("scatterplot mgp / hp")
fig, ax  =  plt.subplots()
sns.scatterplot(x = 'mpg', y = 'hp', data = filtered_df, ax = ax)
plt.xlabel('mpg')
plt.ylabel('hp')
st.pyplot(fig)

# corrélation possive
st.write("scatterplot hp / weightlbs")
fig, ax  =  plt.subplots()
sns.scatterplot(x = 'hp', y = 'weightlbs', data = filtered_df, ax = ax)
plt.xlabel('hp')
plt.ylabel('weightlbs')
st.pyplot(fig)

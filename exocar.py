import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Streamlit : build and share data apps")
st.write("plop plop")


link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_car = pd.read_csv(link)

# st.write(df_car)
# st.line_chart(df_car['hp'])


numeric_columns = df_car.select_dtypes(include=['float64', 'int64'])


st.write("Recherche de corrélation")
correlation_matrix = numeric_columns.corr()
fig,ax=plt.subplots()
sns.heatmap(correlation_matrix, center=0, cmap="vlag", annot = True)
st.pyplot(fig)

st.write("scatterplot mgp / hp")
fig, ax = plt.subplots()
sns.scatterplot(x='mpg', y='hp', data=df_car, ax=ax)
plt.xlabel('mpg')
plt.ylabel('hp')
st.pyplot(fig)

st.write("scatterplot hp / weightlbs")
fig, ax = plt.subplots()
sns.scatterplot(x='hp', y='weightlbs', data=df_car, ax=ax)
plt.xlabel('hp')
plt.ylabel('weightlbs')
st.pyplot(fig)



# fig, ax = plt.subplots()
# fig = sns.pairplot(df_car.select_dtypes(include=['float64', 'int64']))
# st.pyplot(fig)

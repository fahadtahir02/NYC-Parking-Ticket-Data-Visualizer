
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


d = {'Years' : [2013,2014,2015,2016,2017], 'Total Earned' : [575170.0,291945.0,895710,243395.0,271130.0]}
df = pd.DataFrame(data = d)

fig = plt.figure(figsize=(10,4))
sns.barplot(data = df, x = 'Years', y = 'Total Earned')

print("Creating bar chart")

st.write("Total amount made per year off of tickets.")
st.pyplot(fig) 
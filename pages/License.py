import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt 
import seaborn as sns
import streamlit as st

df = pd.read_csv("data/NYC_Parking_Data.csv")

st.header("Find your liscense plate 👋")

liscense_values = np.insert(df['Plate ID'].unique(),0,values="All")

input = st.text_input('Put in your liscense plate')

if input in liscense_values:
    st.write("We have your parking ticket")
elif input not in liscense_values:
    st.write("There is no record of a parkting ticket for that plate")


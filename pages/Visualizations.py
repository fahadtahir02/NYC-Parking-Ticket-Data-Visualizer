import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt 
import seaborn as sns
import streamlit as st

df = pd.read_csv("data/NYC_Parking_Data.csv")

st.header("Choose a visualization to view 👋")

visuals = ["Hotspots", "Common Kinds of Tickets", "Time of Day", "Most Spotted Color", "Fines Over the Years"]

option = st.selectbox(
     'Choose a visualization below',
    visuals)

st.write('You selected:', option)

# can use a switch structure to choose what graph to display based on option 
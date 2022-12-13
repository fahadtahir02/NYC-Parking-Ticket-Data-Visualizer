import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt 
import seaborn as sns
import streamlit as st

df = pd.read_csv("https://raw.githubusercontent.com/fahadtahir02/NYC-Parking-Ticket-Data-Visualizer/main/data/NYC_Parking_Data.csv")

st.header("🔍 Find your license plate! 🔍")

license_values = np.insert(df['Plate ID'].unique(),0,values="All")

input = st.text_input('Put in your license plate, try some examples such as (41768JM , GUD1201)')



if input in license_values:
    st.write("We have your parking ticket.\nGathering data on it:")
    
    #drop unused columns
    df = df.drop('Unnamed: 0.3', axis = 1)
    df = df.drop('Unnamed: 0.2', axis = 1)
    df = df.drop('Unnamed: 0.1', axis = 1)
    df = df.drop('Unnamed: 0', axis = 1)
    df = df.drop('level_0', axis = 1)
    df = df.drop('index', axis = 1)
    df = df.drop('In NYC', axis = 1)
    df = df.drop('Feet From Curb',axis = 1)
    df = df.drop('Violation Post Code',axis = 1)
    df = df.drop('Violation Description',axis = 1)
    df = df.drop('No Standing or Stopping Violation',axis = 1)
    df = df.drop('Hydrant Violation',axis = 1)
    df = df.drop('Double Parking Violation', axis = 1)
    df = df.drop('IntTime', axis = 1)
    df = df.drop('below 96th', axis = 1)
    df = df.drop('Meter Number',axis = 1)

    cond = (df['Plate ID'] == input)
    plate_info = df[cond]

    total = plate_info['Price of Ticket'].sum()
    low = plate_info['Hour'].min()
    high = plate_info['Hour'].max()

    st.write("The total amount this plate owes is $", total, "\nTaking place from hours ", low, " to ", high)
    pd.set_option('display.max_columns',99)
    st.dataframe(plate_info)

elif input not in license_values:
    st.write("There is no record of a parkting ticket for that plate")


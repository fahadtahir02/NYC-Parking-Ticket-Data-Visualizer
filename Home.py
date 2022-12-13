import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="NYC Parking Ticket Data Visualizer",
    page_icon="🚗",
)

st.header("🚗 NYC Parking Ticket Data Visualizer! 🚗")

st.image('images/nyc_map_image.jpg')


st.write('We are creating data visualizations of NYC Parking Tickets data to analyze and draw conclusions. We want to see if there are any patterns we can identify in this data. The data we are using is around 30,000 rows of tickets that includes information such as Registration State, Violation Code, Violation Time, etc. Navigate to the Visualizations page to interact with the different models we made. Navigate tot he License page to interact with our dataset.')
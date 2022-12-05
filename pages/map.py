import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache
def display_map(): #suppress_st_warning=True
    try:
        df = pd.read_csv('https://raw.githubusercontent.com/conor7276/CTP-Parking-Data-Visualization-Project/main/src/app/data/NYC_Parking_Data_Updated.csv?token=GHSAT0AAAAAABZI3OWLFMW4ZGAAYVEW5YCUY4NB3AA')
        print("Loading github data")
    except Exception as e:
        df = pd.read_csv('data/NYC_Parking_Data_Updated(1).csv')
        print('Loading local data')

    #df = df[df['IntTime'] > 1200] testing with only showing specific times
    fig = px.scatter_mapbox(df,
                            lon = df['Longitude'],
                            lat = df['Latitude'],                        
                            zoom = 9,
                            color = df['Price of Ticket'], # this option can change as long as it is of type int
                            color_continuous_scale = "bluyl",
                            center = {'lat' : 40.7,'lon' : -74},
                            title = "Park it like it's hot",
                            hover_name = df['Full Address'],
                            hover_data = [df['Time'],df['Issue Date'],df['Violation'],df['Price of Ticket']])
    fig.update_layout(mapbox_style = "carto-positron") #other mapbox styles are available such as: 'open-street-map', 'white-bg',
    # 'carto-positron', 'carto-darkmatter', 'stamen- terrain', 'stamen-toner', 'stamen-watercolor'
    # Other mapbox styles are available but require an api key.
    #fig.show()
    return fig
    
print("Creating map")
fig = display_map()
st.plotly_chart(fig)
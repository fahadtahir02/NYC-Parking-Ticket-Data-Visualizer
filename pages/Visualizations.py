import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt 
import seaborn as sns
import streamlit as st
import plotly.express as px

df = pd.read_csv("data/NYC_Parking_Data.csv")

st.header("Choose a visualization to view 👋")

visuals = ["Hotspots", "Common Kinds of Tickets", "Time of Day", "Most Spotted Color", "Fines Over the Years"]

option = st.selectbox(
     'Choose a visualization below',
    visuals)

st.write('You selected:', option)

if(option == "Hotspots"):
    @st.cache
    def display_map(hour,year): #suppress_st_warning=True
        try:
            df = pd.read_csv('https://raw.githubusercontent.com/fahadtahir02/NYC-Parking-Ticket-Data-Visualizer/main/data/NYC_Parking_Data.csv')
            print("Loading github data")
        except Exception as e:
            df = pd.read_csv('data/NYC_Parking_Data_Updated(1).csv')
            print('Loading local data')
            
            
        condition = ((df['Hour'] == hour) & (df['Year'] == year))
        new_df = df[((df['Hour'] == hour) & (df['Year'] == year))].copy()
        #df = df[df['IntTime'] > 1200] testing with only showing specific times
        fig = px.scatter_mapbox(new_df,
                                lon = new_df['Longitude'],
                                lat = new_df['Latitude'],                        
                                zoom = 9,
                                color = new_df['Hour'], # this option can change as long as it is of type int
                                #color_continuous_scale = "bluyl", #bluyl
                                center = {'lat' : 40.7,'lon' : -74},
                                title = "Park it like it's hot",
                                hover_name = new_df['Full Address'],
                                hover_data = [new_df['Time'],new_df['Issue Date'],new_df['Violation'],new_df['Price of Ticket']],
                                height = 700,
                                width = 700)
        fig.update_layout(mapbox_style = "carto-positron") #other mapbox styles are available such as: 'open-street-map', 'white-bg',
        # 'carto-positron', 'carto-darkmatter', 'stamen- terrain', 'stamen-toner', 'stamen-watercolor'
        # Other mapbox styles are available but require an api key.
        #fig.update_mapboxes()
        #fig.show()
        return fig


    year = st.slider(label="Year",min_value=2013,max_value=2017,value=2015,step=1, help = "Select the year of the day to be displayed:"''',on_change = display_map(month)''')
    hour = st.slider(label= "Hour", min_value=0,max_value= 23, value = 12, step = 1, help = "Select the hour to be displayed:"''', on_change = display_map(year)''') 
    #year_options = [2013,2014,2015,2016,2017]
    #hour_options = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    #year = st.select_slider(label="Year",options = year_options,value=2015,help = "Select the year of the day to be displayed:"''',on_change = display_map(month)''')
    #hour = st.select_slider(label= "Hour", options = hour_options, value = 12, help = "Select the hour to be displayed:"''', on_change = display_map(year)''') 
    print("Creating map")

    fig = display_map(hour,year)

    print(type(fig))
    st.plotly_chart(fig, use_container_width = True)
    del fig
elif(option == "Fines Over the Years"):
    d = {'Years' : [2013,2014,2015,2016,2017], 'Total Earned' : [575170.0,291945.0,895710,243395.0,271130.0]}
    df = pd.DataFrame(data = d)

    fig = plt.figure(figsize=(10,4))
    sns.barplot(data = df, x = 'Years', y = 'Total Earned')

    print("Creating bar chart")

    st.write("Total amount made per year off of tickets.")
    st.pyplot(fig) 
    for year in range(len(df['Years'])):
        st.write(df['Years'].iloc[year], ": $", df['Total Earned'].iloc[year])
    # can use a switch structure to choose what graph to display based on option 
elif(option == "Common Kinds of Tickets"):
    gb = df.groupby('Violation Code').size().reset_index(name="Total Amount").sort_values(by = "Total Amount")
    #out_vs_in = gb['Violation Code'].count().sort_values()
    #out_vs_in.plot(kind='barh', figsize = (34,21))

    fig = plt.figure(figsize=(13,8))
    ax = sns.barplot(data = gb.nlargest(10, "Total Amount"), x = 'Violation Code', y = 'Total Amount',  order=gb["Violation Code"])
    ax.set(xlim=(68,79))

    st.pyplot(fig)


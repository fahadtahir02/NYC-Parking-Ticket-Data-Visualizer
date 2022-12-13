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

if(option == "Time of Day"):
    def load_data():
        try:
            df = pd.read_csv('https://raw.githubusercontent.com/fahadtahir02/NYC-Parking-Ticket-Data-Visualizer/main/data/NYC_Parking_Data.csv')
            print("Loading github data")
        except Exception as e:
            df = pd.read_csv('data/NYC_Parking_Data_Updated(1).csv')
            print('Loading local data')
        return df

    df = load_data()
    @st.cache
    def display_map(df, hour,year): #suppress_st_warning=True
        
        
        condition = ((df['Hour'] == hour) & (df['Year'] == year))
        new_df = df[condition]
        #df = df[df['IntTime'] > 1200] testing with only showing specific times
        fig = px.scatter_mapbox(new_df,
                                lon = new_df['Longitude'],
                                lat = new_df['Latitude'],                        
                                zoom = 9,
                                color = new_df['Price of Ticket'], # this option can change as long as it is of type int
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
        #fig.show()
        #fig.update_traces(marker_line_width = 0)
        return fig


    #year = st.slider(label="Year",min_value=2013,max_value=2017,value=2015,step=1, help = "Select the year of the day to be displayed:"''',on_change = display_map(month)''')
    #hour = st.slider(label= "Hour", min_value=0,max_value= 23, value = 12, step = 1, help = "Select the hour to be displayed:"''', on_change = display_map(year)''') 
    year_options = [2013,2014,2015,2016,2017]
    hour_options = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    year = st.select_slider(label="Year",options = year_options,value=2015,help = "Select the year of the day to be displayed:")
    hour = st.select_slider(label= "Hour", options = hour_options, value = 12, help = "Select the hour to be displayed:") 
    print("Creating map")

    fig = display_map(df,hour,year)

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
elif(option == "Hotspots"):
    def load_data():
        try:
            df = pd.read_csv('https://raw.githubusercontent.com/fahadtahir02/NYC-Parking-Ticket-Data-Visualizer/main/data/NYC_Parking_Data.csv')
            print("Loading github data")
        except Exception as e:
            df = pd.read_csv('data/NYC_Parking_Data_Updated(1).csv')
            print('Loading local data')
        return df

    df = load_data()
    @st.cache
    def display_map(df, hour,year): #suppress_st_warning=True
        
        
        condition = ((df['Hour'] == hour) & (df['Year'] == year))
        new_df = df[condition]
        #df = df[df['IntTime'] > 1200] testing with only showing specific times
        fig = px.density_mapbox(new_df,
                                lon = new_df['Longitude'],
                                lat = new_df['Latitude'],                        
                                zoom = 9,
                                #color = new_df['Price of Ticket'], # this option can change as long as it is of type int
                                #color_continuous_scale = "bluyl", #bluyl
                                center = {'lat' : 40.7,'lon' : -74},
                                title = "Park it like it's hot",
                                hover_name = new_df['Full Address'],
                                hover_data = [new_df['Time'],new_df['Issue Date'],new_df['Violation'],new_df['Price of Ticket']],
                                opacity = 0.75,
                                height = 700,
                                width = 700)
        fig.update_layout(mapbox_style = "carto-positron") #other mapbox styles are available such as: 'open-street-map', 'white-bg',
        # 'carto-positron', 'carto-darkmatter', 'stamen- terrain', 'stamen-toner', 'stamen-watercolor'
        # Other mapbox styles are available but require an api key.
        #fig.show()
        #fig.update_traces(marker_line_width = 0)
        return fig


    #year = st.slider(label="Year",min_value=2013,max_value=2017,value=2015,step=1, help = "Select the year of the day to be displayed:"''',on_change = display_map(month)''')
    #hour = st.slider(label= "Hour", min_value=0,max_value= 23, value = 12, step = 1, help = "Select the hour to be displayed:"''', on_change = display_map(year)''') 
    year_options = [2013,2014,2015,2016,2017]
    hour_options = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    year = st.select_slider(label="Year",options = year_options,value=2015,help = "Select the year of the day to be displayed:")
    hour = st.select_slider(label= "Hour", options = hour_options, value = 12, help = "Select the hour to be displayed:") 
    print("Creating map")

    fig = display_map(df,hour,year)

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
elif(option == "Most Spotted Color"):
    data = pd.read_csv('https://raw.githubusercontent.com/fahadtahir02/NYC-Parking-Ticket-Data-Visualizer/main/data/NYC_Parking_Data.csv')
    ndata = data[["Violation Code", "Issue Date"]].copy()
    ndata.transpose()
    vCode = ndata["Violation Code"].unique()
    frequency = data['Vehicle Color'].map(data['Vehicle Color'].value_counts())
    df1 = pd.DataFrame(frequency)
    df1.rename(columns={"Vehicle Color": "Frequency"}, inplace = "True")
    cData = data[['Vehicle Color', 'Violation Code']].copy()
    df_main = pd.concat([cData, df1], axis = 1)
    df_main = df_main.sort_values('Frequency', ascending=False)
    df_main = df_main.dropna()
    
    color_ticket = {
    "White" : 9,
    "Silver" : 8,
    "Grey" : 5,
    "Black" : 4

    }

    # Data to plot
    labels = []
    sizes = []

    for x, y in color_ticket.items():
        labels.append(x)
        sizes.append(y)

    # Plot
    fig = plt.figure(figsize=(13,8))
    dig = plt.pie(sizes, labels=labels, autopct = '%1.0f%%')

    #plt.axis('equal')
    #plt.show()
    st.write()
    st.pyplot(fig)
elif(option == "Common Kinds of Tickets"):
    gb = df.groupby('Violation Code').size().reset_index(name="Total Amount").sort_values(by = "Total Amount")
    #out_vs_in = gb['Violation Code'].count().sort_values()
    #out_vs_in.plot(kind='barh', figsize = (34,21))

    fig = plt.figure(figsize=(13,8))
    ax = sns.barplot(data = gb.nlargest(10, "Total Amount"), x = 'Violation Code', y = 'Total Amount',  order=gb["Violation Code"])
    ax.set(xlim=(68,79))

    st.pyplot(fig)
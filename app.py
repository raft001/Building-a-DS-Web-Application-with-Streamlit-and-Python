import streamlit as st
import pandas as pd
import numpy as np

data_url = ("/home/rhyme/Desktop/Project/Motor_Vehicle_Collisions_-_Crashes.csv")


st.title("motor vehicle collisions in new york city")
st.markdown("it is a dashboard that analyses motor vehicles collissions in nyc")
@st.cache(persist= True) #only does computations when there is new data or code changes
def load_data(nrows):
    data=pd.read_csv(data_url, nrows=nrows, parse_dates=[['CRASH_DATE', 'CRASH_TIME']])
    data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
    lowercase=lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data.rename(columns={'crash_date_crash_time':'date/time'}, inplace=True)
    return data

data=load_data(100000)

if st.checkbox("show raw dara", False):
    st.subheader('raw data')
    st.write(data)

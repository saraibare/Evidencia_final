# -*- coding: utf-8 -*-
"""3_EvidenciaFinal_A01734979.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SA1jrcDr8p2CwDZvgqTcHpPCPEmCQrSx
"""

import streamlit as st
import pandas as pd 
import numpy as np 
import plotly as px 
import plotly.figure_factory as ff
from bokeh.plotting import figure 
import matplotlib.pyplot as plt 
from datetime import date, time, datetime

st.title('Police Incident Reports from 2018 to 2020 in San Francisco')
df = pd.read_csv("Police_Department_Incident_Reports__2018_to_Present (1).csv")


st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.')

mapa = pd.DataFrame()
mapa['Date'] = df['Incident Date']
mapa['Day'] = df['Incident Day of Week']
mapa['Police District'] = df['Police District']
mapa['Neighborhood'] = df['Analysis Neighborhood']
mapa['Incident Category'] = df['Incident Category']
mapa['Incident Subcategory'] = df['Incident Subcategory']
mapa['Incident Year'] = df['Incident Year']
mapa['Resolution'] = df['Resolution']
mapa['lat'] = df['Latitude']
mapa['lon'] = df['Longitude']
mapa['Supervisor District'] = df['Supervisor District']


df['Incident Datetime'] = pd.to_datetime(df['Incident Datetime'])
df['MONTH'] = df['Incident Datetime'].dt.month
mapa['MONTH'] = df['MONTH']

mapa=mapa.dropna()

subset_data2 = mapa
police_district_input = st.sidebar.multiselect(
'Police District',
mapa.groupby('Police District').count().reset_index()['Police District'].tolist())
if len(police_district_input) > 0:
    subset_data2 = mapa[mapa['Police District'].isin(police_district_input)]

subset_data1 = subset_data2
neighborhood_input = st.sidebar.multiselect(
'Neighborhood',
subset_data2.groupby('Neighborhood').count().reset_index()['Neighborhood'].tolist())
if len(neighborhood_input) > 0:
    subset_data1 = subset_data2[subset_data2['Neighborhood'].isin(neighborhood_input)]

subset_data = subset_data1
year_input = st.sidebar.multiselect(
'Incident Year',
subset_data1.groupby('Incident Year').count().reset_index()['Incident Year'].tolist())
if len(year_input) > 0:
    subset_data = subset_data1[subset_data1['Incident Year'].isin(year_input)]
            

st.markdown('It is important to mention that any police district can answer to any incident, the neighborhood in which it happened is not related to the police district.')
st.markdown('Crime locations in San Francisco')
st.map(subset_data)

col1,col2=st.columns(2)
with col1:
    st.markdown('Crimes ocurred per month')
    st.bar_chart(df['MONTH'].value_counts())
with col2:
    st.markdown('Crimes ocurred per day of the week')
    st.bar_chart(subset_data['Day'].value_counts())

st.markdown('Crimes occured per date')
st.line_chart(subset_data['Date'].value_counts())

st.markdown('Type of crimes committed')
st.bar_chart(subset_data['Incident Category'].value_counts())
st.markdown('Subtype of crimes committed')
st.bar_chart(subset_data['Incident Subcategory'].value_counts())


col3,col4=st.columns(2)
with col3:
    st.markdown('Resolution status')
    fig1,ax1 = plt.subplots()
    labels = subset_data['Resolution'].unique()
    ax1.pie(subset_data['Resolution'].value_counts(),labels=labels, autopct = '%1.1f%%',startangle=20,colors = ['blue','darkblue','skyblue','cyan','lightgray',])
    st.pyplot(fig1)
with col4:
    st.markdown('Supervisor District')
    fig1,ax1 = plt.subplots()
    labels = subset_data['Supervisor District'].unique()
    ax1.pie(subset_data['Supervisor District'].value_counts(),labels=labels, autopct = '%1.1f%%',startangle=20,colors = ['#905080','#af6d9e','#ce8abc','#efa8dc','#ffc2ef','#ffd7f4','#ffebfa'])
    st.pyplot(fig1)




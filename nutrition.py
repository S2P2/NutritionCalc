import streamlit as st
import pandas as pd
import numpy as np

st.title('Nutrition Calculator')

nutrition_data = pd.read_excel('Nutrition_data.xlsx', engine="openpyxl")
nutrition_data.set_index('Name')

x = st.sidebar.selectbox('Diet', nutrition_data['Name'])
volume_per_feed = st.sidebar.slider('Volume', min_value=50, max_value=500, value=300, step=50)
feed_per_day = st.sidebar.slider('Feed (times)', min_value=1, max_value=6, value=4)
conc = st.sidebar.slider('Concentration', min_value=0.5, max_value=2.0, value=1.0, step=0.1)
BW = st.sidebar.number_input('Body weight(kg)', value=50.0, step=1.0, format="%.1f")

st.write(x, "(",conc,": 1 ) ", volume_per_feed, " mL x ", feed_per_day, " feeds")
total_cal = conc * volume_per_feed * feed_per_day
total_protein = total_cal * nutrition_data[nutrition_data['Name']==x].Protein.values[0]
st.write("TC ", int(total_cal), "TP ", round(total_protein/1000/BW,2))


with st.beta_expander('See Detail'):
    'Total Calories'
    st.write(conc, "x ", volume_per_feed, "x ", feed_per_day, "= ", int(total_cal), "kcal" )
    st.write(int(total_cal), "/", BW, "=", int(total_cal)/BW, "kcal/kg")

    'Total Protein'
    st.write(nutrition_data[nutrition_data['Name']==x].Protein.values[0],"/ 1000 kcal x ", total_cal , " = ", total_protein/1000, " g")
    st.write(total_protein/1000, "/", BW, " = ", round(total_protein / BW / 1000, 2), "g/kg/day")

' '

if st.checkbox('Show Raw Table'):
    nutrition_data
import pickle
import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import datetime

### LIBRARIES REQUIRED
## pip install streamlit
## pip install plotly


euros = pickle.load(open('euros1.pkl','rb'))
dollars = pickle.load(open('dollars2.pkl','rb'))
pounds = pickle.load(open('pounds3.pkl','rb'))

option = st.sidebar.selectbox('Select Currency',('Euros', 'Dollars', 'Pounds'))

if option == 'Euros':

    date = st.sidebar.date_input('Select a date', min_value= datetime.date(2021,10,24),max_value= datetime.date(2026,10,20))

    if st.sidebar.button('Forecast'):
        euros_on_date = int(euros[euros['ds'] == pd.to_datetime(date)]['yhat'])
        p= euros[euros['ds'] == pd.to_datetime(date)]['yhat'].values[0]
        st.title(p)
        st.subheader("Rupees")

    fig1 = px.line(dollars, x="ds", y="yhat", title='Forecast of Euros')
    fig1.add_annotation(x=date, y=p,
                        text=date.strftime('%Y-%m-%d'),
                        showarrow=True,
                        arrowhead=1)
    fig1.update_layout(width=940, height=500)
    st.plotly_chart(fig1)

if option == 'Dollars':

    date = st.sidebar.date_input('Select a date', min_value= datetime.date(2021,10,24),max_value= datetime.date(2026,10,20))

    if st.sidebar.button('Forecast'):
        dollars_on_date = int(dollars[dollars['ds'] == pd.to_datetime(date)]['yhat'])
        p = dollars[dollars['ds'] == pd.to_datetime(date)]['yhat'].values[0]
        st.title(p)
        st.subheader("Rupees")

        fig2 = px.line(dollars, x="ds", y="yhat", title='Forecast of Dollars')
        fig2.add_annotation(x=date, y=p,
                           text=date.strftime('%Y-%m-%d'),
                           showarrow=True,
                           arrowhead=1)
        fig2.update_layout(width=940,height=500)
        st.plotly_chart(fig2)


if option == 'Pounds':

    date = st.sidebar.date_input('Select a date', min_value= datetime.date(2021,10,24),max_value= datetime.date(2026,10,20))

    if st.sidebar.button('Forecast'):
        pounds_on_date = int(pounds[pounds['ds'] == pd.to_datetime(date)]['yhat'])
        p = pounds[pounds['ds'] == pd.to_datetime(date)]['yhat'].values[0]
        st.title(p)
        st.subheader("Rupees")

    fig3 = px.line(dollars, x="ds", y="yhat", title='Forecast of Pounds')
    fig3.add_annotation(x=date, y=p,
                        text=date.strftime('%Y-%m-%d'),
                        showarrow=True,
                        arrowhead=1)
    fig3.update_layout(width=940, height=500)
    st.plotly_chart(fig3)

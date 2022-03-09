from flask import request
import streamlit as st
import requests


def app():
    # -- hidden
    hide_st_style = """
            <style>
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    # -- modeling
    URL = 'http://127.0.0.1:5000/'
    with st.container():
        st.title(':red_car: Model Prediksi Harga Mobil')
    with st.container():
        st.write('---')
        col1, col2, col3 = st.columns(3)
        col4, col5, col6, col7 =  st.columns(4)
        cl = col1.text_input('Car Length', value=0)
        cw = col2.text_input('Car Width', value=0)
        cb = col3.text_input('Cub Weight', value=0)
        en = col4.text_input('Engine Size', value=0)
        hp = col5.text_input('Horsepower', value=0)
        ct = col6.text_input('City Mpg', value=0)
        hh = col7.text_input('Highway Mpg', value=0)
        # ft = st.text_input('Fuel Type')
        # dw = st.text_input('Drive Wheel Type')
        ft = st.selectbox(
            'What is fuel type?',
            ('gas', 'diesel'))
        dw = st.selectbox(
            'What is drive wheel type?',
            ('fwd', 'rwd', '4wd'))
        # ft = st.write('You selected:', option)
        # dw = st.write('You selected:', option1)

    # Param input
    URL = URL + f'?cl={cl}&cw={cw}&cb={cb}&en={en}&hp={hp}&ct={ct}&hh={hh}&ft={ft}&dw={dw}' 

    # komunikasi dengan server
    r = requests.get(URL)
    res = r.json()
    with st.container():
        st.write('---')
        st.subheader(f':pushpin: Hasil Prediksi Harga Mobil adalah ${res["data"]["result"]}')
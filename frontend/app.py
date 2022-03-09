import Page1, Page2, Page3
import streamlit as st

 # config
st.set_page_config(
    page_title="Webapps Prediksi Mobil",
    page_icon=":car:",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "My Github Profile : " 'https://github.com/dwikikresnadi'
    }
)
PAGES = {
    "Profile & Problem Explanation": Page1,
    "EDA (Exploratory Data Analysis)": Page2,
    "Car Price Prediction": Page3
}

st.sidebar.title("Menu Utama")
selection = st.sidebar.selectbox("Select a Page", list(PAGES.keys()))
page = PAGES[selection]
page.app()
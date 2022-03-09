# -- import module
import streamlit as st
from PIL import Image
import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie

 

# -- import function & varible
def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
img = Image.open('tesla_.jpg')
lottie_hello = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_3vbOcw.json")
lottie_discord = load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_b7zhs33r.json')
lottie_email = load_lottieurl('https://assets8.lottiefiles.com/packages/lf20_9yi1cm7i.json')
lottie_git = load_lottieurl('https://assets3.lottiefiles.com/packages/lf20_kq6zs04j.json')
def app():
    hide_st_style = """
            <style>
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)
    # -- HEADER
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:   
            st.title('Hello, Welcome to My WebApps! :wave:')
            st.subheader('Pada webapps sederhana ini akan menjelaskan mengenai bagaimana melakukan **Prediksi Harga Mobil**')
            with st.container():
                st.write('Dataset dapat dilihat [disini](https://www.kaggle.com/hellbuoy/car-price-prediction)')
            with st.container():
                st.image(img, clamp=False)
        with right_column:
            st_lottie(
            lottie_hello,
            speed=1,
            reverse=False,
            loop=True,
            quality="medium", # low ; medium ; high
            # renderer="canvas", # canvas
            height=None,
            width=None,
            key=None,
            )
    # -- Main Goals
    with st.container():
        st.write('---')
        st.header(':warning: Problem Description')
        st.write('##')
        st.write(
            """
            ##### :notebook: Description 

            Perusahaan mobil atau otomotif dari negeri china ingin mencoba untuk memasuki pasar US dengan melakukan produksi secara lokal di US. 
            Hal ini bertujuan agar perusahaan dapat bersaing secara kompetitif terhadap rekan-rekan yang berada di US dan Eropa.

            Lalu, perusahaan ini melakukan kerjasama dengan perusahaan konsultan otomotif untuk memberikan masukan part apa saja yang dapat mempengaruhi harga mobil 
            secara keseluruhan dan perusahaan konsultan dapat memberikan saran dan prediksi terkait harga mobil yang ingin dibuat dengan part - part yang ada berdasarkan sejumlah dataset yang ada

             ##### :memo: Objective

            Berdasarkan deskripsi permasalahan, didapatkan objective penelitian yang dilakukan :

            1. Perusahaan dapat mengetahui cara untuk melakukan prediksi

            2. Perusahaan mendapatkan insight terkait perkiraan atau prediksi harga jual mobil dari kombinasi part - part baru

            ##### :exclamation: Problem Statement

            Permasalahan yang dapat didefinisikan adalah sebagai berikut.

            1. Bagaimana melakukan prediksi harga jual mobil dengan kombinasi part - part baru?
            """
        )
    # -- CONTACT
    
    with st.container():
        st.write('---')
        st.title('Get in Touch with Me!')
        st.write('##')
        contact_icon, contact_dis = st.columns((0.05, 1))
        with contact_icon:
            dis = st_lottie(
                lottie_discord,
                height=50,
                key='discord',
                )
        with contact_dis:
            st.subheader(f"Naufal Dwiki #8342")
    with st.container():
        contact_icons, contact_email = st.columns((0.05, 1))
        with contact_icons:
            st_lottie(
                lottie_email,
                height=50,
                key='email',
                )
        with contact_email:
            st.subheader("[naufaldwiki08@gmail.com](naufaldwiki08@gmail.com)")
    with st.container():
        contact_iconss, contact_git = st.columns((0.05, 1))
        with contact_iconss:
            st_lottie(
                lottie_git,
                height=50,
                key='git',
                )
        with contact_git:
            st.subheader("[github.com/dwikikresnadi](https://github.com/dwikikresnadi)")
    # with st.container():
    #     col1, col2 = st.columns(2)
    #     with col2:
    #         pages = ['Page1','Page2','Page3']
    #         st.button('Go to next page')
    #         # selection = list(PAGES1.keys())
    #         page1 = PAGES1[Page2]
    #         page1.app()

            
    
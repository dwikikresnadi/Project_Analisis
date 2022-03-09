import streamlit as st
import pandas as pd
import plotly.express as px

value_list = ['sedan', 'hatchback', 'wagon', 'hardtop', 'convertible']
def app():
    # -- hidden
    hide_st_style = """
            <style>
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    # -- HEADER
    st.title('EDA (Exploratory Data Analysis) 📊')
    st.subheader('Import Dataset 🗄️')

    upload_file = st.file_uploader('Import Dataset', type='csv')
    if upload_file:
        with st.container():
            st.markdown('---')
            st.subheader('Dataframe Original')
            df =  pd.read_csv(upload_file)
            st.dataframe(df)
        with st.container():
            st.markdown('---')
            groupy_column = st.multiselect(
                'Select Type of Car :',
                value_list,
                default=value_list
            )
        
            # -- FILTER DATAFRAME
            st.subheader('Dataframe Filter')
            x = df.carbody.isin(groupy_column)
            filtered_df = df[x]
            st.dataframe(filtered_df)
            count_car = len(filtered_df)
            st.markdown(f'*Jumlah kendaraan sebanyak :{count_car}*')

            # -- Pie chart
            pie_group = pd.DataFrame(df['carbody'].value_counts())
            lis1 = (96, 70, 25, 8, 6)
            pie_chart = px.pie(
                pie_group,
                title = 'Persebaran jumlah kendaraan',
                values = pie_group['carbody'],
                names = pie_group.index
            )
            st.plotly_chart(pie_chart)

            # -- Bar Chart
            # df_grouped = df[x].groupby('carbody')['fueltype'].value_counts()
            # df_grouped = pd.DataFrame(df_grouped)
            # df_grouped.rename(columns={'fueltype' : 'jumlah'}, inplace=True)
            # df_grouped.reset_index(inplace=True)

            # sns.barplot(x="carbody", y="jumlah", hue="fueltype", data=df_grouped)
            # st.pyplot()
            # bar_chart = px.bar(
            #     df_grouped,
            #     x='carbody',
            #     y='fueltype',
            #     title='bartest',
            #     color_discrete_sequence= ['#F63366']*len(df_grouped),
            #     template='plotly_white',
            # )
            # st.plotly_chart(bar_chart)
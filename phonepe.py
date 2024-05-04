import streamlit as st
from streamlit_option_menu import option_menu
import PIL
from PIL import Image
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import plotly.express as px

mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="")
mycursor = mydb.cursor(buffered=True)

# creating option menu 
SELECT = option_menu(
     menu_title = None,
     options = ["About", "Home", "Top Charts", "Explore Data"], 
     icons =["exclamation-circle", "house", "bar-chart", "toggles"],
     default_index=0,
     orientation="horizontal",
     styles={"container": {"padding": "0!important", "background-color": "white", "size":"cover", "width": "100"},
            "icon": {"color": "black", "font-size": "20px"},
     "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6836AD"},
     "nav-link-selected" : {"background-color":"#6836AD"}})

# option 1 --> About 
if SELECT=='About':
    col1,col2=st.columns(2)
    col2.image(Image.open("C:\\Users\\user\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-04-30 115426.png"),width=300)
    with col1: 
        st.text('')
        st.text('')
        #st.vedio("C:\\Users\\user\\OneDrive\\Desktop\\PhonePe_Introduction_aXnNA4mv1dU_136.mp4")
        video_file = open('C:\\Users\\user\\OneDrive\\Desktop\\PhonePe_Introduction_aXnNA4mv1dU_136.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes,loop=True)
        st.markdown("""---""")
        st.subheader('India First Fintech Company Phonepe launched the Cross-Border UPI Payments System')
        st.text("Phonepe became a leading digital payments company")
        st.image('C:\\Users\\user\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-04-30 130328.png',width=450,caption='ONE APP FOR ALL THINGS MONEY!!')

    with col2: 
        st.subheader(':blue[PhonePe is a digital payments and financial services app in India that allows users to send and receive money, recharge mobile, pay bills, and shop online. The app was founded in December 2015 by Sameer Nigam, Rahul Chari, and Burzin Engineer, and went live in August 2016. PhonePe is based on the Unified Payments Interface (UPI) and is available in over 11 Indian languages.]')
        st.markdown("""---""")
        st.markdown('The current launch supports all international merchant outlets in UAE, Singapore, Mauritius, Nepal and Bhutan that have a local QR code.')
        st.markdown("""---""")
        st.image("C:\\Users\\user\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-04-30 121033.png",width=550)

#option 2 --> Home
elif SELECT=='Home': 
    col1,col2=st.columns(2) 
    with col2: 
        video_file = open('C:\\Users\\user\\OneDrive\\Desktop\\home-fast-secure-v3.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes,loop=True)
        st.markdown("""---""")
        st.title(":blue[What's new]")
        st.subheader('Rupay Credit Card on UPI')
        st.markdown("No need for CVV and OTP; pay with PIN")
        st.markdown('Check credit card balance')
        st.markdown("""---""")
        st.subheader('PhonePe Insurance')
        st.markdown('Compare and buy health, life, car and bike insurance plans seamlessly.')
        st.markdown("""---""")

    with col1: 
        st.text('')
        st.header(':blue[Simple, Fast & Secure]')
        st.subheader('One app for all things money.')
        st.caption('Pay bills, recharge, send money, buy gold, invest and shop at your favourite stores.')
        st.markdown("""---""")
        st.subheader('Pay whenever you like, wherever you like.')
        st.caption('Choose from options like UPI, the PhonePe wallet or your Debit and Credit Card.')
        st.markdown("""---""")
        st.subheader('Find all your favourite apps on PhonePe Switch.')
        st.caption('Book flights, order food or buy groceries. Use all your favourite apps without downloading them.')
        st.link_button("DOWNLOAD THE APP NOW","https://www.phonepe.com/app-download/")
        st.caption("This app is available for all of your devices")
        st.text('')
        st.markdown("""---""")
        st.image('C:\\Users\\user\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-04-30 130256.png',width=550)
        st.subheader('PhonePe Lending')
        st.markdown('Add upto ₹2,000, withdraw anytime, no charges.')
        st.markdown('Pay upto ₹500 without any PIN.')
        st.markdown('Experience super-fast payments with near-zero failures')
        st.markdown("""---""")

#option 3 --> Top chart page

elif SELECT=='Top Charts':

    st.subheader(':blue[TOP CHARTS]')
    option = st.selectbox("Type",("Transaction", "Users"),index=0)
    co1,co2=st.columns(2)
    with co1:
        Year= st.select_slider('Year',options=['2018', '2019', '2020', '2021', '2022', '2023'])
        Quarter=st.select_slider('Quarter',options=['1', '2', '3', '4'])
        States=st.selectbox('State',('Andaman & Nicobar','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar',
                    'Chandigarh','Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat',
                    'Haryana','Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Ladakh',
                    'Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry',
                    'Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal'))
    with co2: 
        st.text('FROM THIS MENU WE CAN GET THE DETAILS LIKE:')
        st.caption('Top 10 states based on Total amount transaction on phonepe.')
        st.caption('Top 10 states based on Total number of  transaction on phonepe.')
        st.caption('Top 10 mobile brand based on the how many people use phonepe.')
        st.caption('Top 10 State,District based on Total phonepe users and their app opening')
    # option Transaction
    if option=='Transaction':
        mycursor.execute('use phonepe')
        mycursor.execute('''select * from maptrans''')
        out=mycursor.fetchall()
        header=[i[0] for i in mycursor.description]
        df=pd.DataFrame(out,columns=header)
        # Filter the DataFrame for the year 2018 and quarter 1
        if Year=='2018' and Quarter=='1':
            filtered_df = df[(df['Year'] == 2018) & (df['Quarter'] == 1)]
            filter_df=df[(df['Year'] == 2018) & (df['Quarter'] == 1) & (df['State'] == States)]
        
        elif Year=='2018' and Quarter=='2':
            filtered_df = df[(df['Year'] == 2018) & (df['Quarter'] == 2)]
            filter_df=df[(df['Year'] == 2018) & (df['Quarter'] == 2) & (df['State'] == States)]
        
        elif Year=='2018' and Quarter=='3':
            filtered_df = df[(df['Year'] == 2018) & (df['Quarter'] == 3)]
            filter_df=df[(df['Year'] == 2018) & (df['Quarter'] == 3) & (df['State'] == States)]
        
        elif Year=='2018' and Quarter=='4':
            filtered_df = df[(df['Year'] == 2018) & (df['Quarter'] == 4)]
            filter_df=df[(df['Year'] == 2018) & (df['Quarter'] == 4) & (df['State'] == States)]

        elif Year=='2019' and Quarter=='1':
            filtered_df = df[(df['Year'] == 2019) & (df['Quarter'] == 1)]
            filter_df=df[(df['Year'] == 2019) & (df['Quarter'] == 1) & (df['State'] == States)]
        
        elif Year=='2019' and Quarter=='2':
            filtered_df = df[(df['Year'] == 2019) & (df['Quarter'] == 2)]
            filter_df=df[(df['Year'] == 2019) & (df['Quarter'] == 2) & (df['State'] == States)]
        
        elif Year=='2019' and Quarter=='3':
            filtered_df = df[(df['Year'] == 2019) & (df['Quarter'] == 3)]
            filter_df=df[(df['Year'] == 2019) & (df['Quarter'] == 3) & (df['State'] == States)]
        
        elif Year=='2019' and Quarter=='4':
            filtered_df = df[(df['Year'] == 2019) & (df['Quarter'] == 4)]
            filter_df=df[(df['Year'] == 2019) & (df['Quarter'] == 4) & (df['State'] == States)]

        elif Year=='2020' and Quarter=='1':
            filtered_df = df[(df['Year'] == 2020) & (df['Quarter'] == 1)]
            filter_df=df[(df['Year'] == 2020) & (df['Quarter'] == 1) & (df['State'] == States)]
        
        elif Year=='2020' and Quarter=='2':
            filtered_df = df[(df['Year'] == 2020) & (df['Quarter'] == 2)]
            filter_df=df[(df['Year'] == 2020) & (df['Quarter'] == 2) & (df['State'] == States)]
        
        elif Year=='2020' and Quarter=='3':
            filtered_df = df[(df['Year'] == 2020) & (df['Quarter'] == 3)]
            filter_df=df[(df['Year'] == 2020) & (df['Quarter'] == 3) & (df['State'] == States)]
        
        elif Year=='2020' and Quarter=='4':
            filtered_df = df[(df['Year'] == 2020) & (df['Quarter'] == 4)]
            filter_df=df[(df['Year'] == 2020) & (df['Quarter'] == 4) & (df['State'] == States)]

        elif Year=='2021' and Quarter=='1':
            filtered_df = df[(df['Year'] == 2021) & (df['Quarter'] == 1)]
            filter_df=df[(df['Year'] == 2021) & (df['Quarter'] == 1) & (df['State'] == States)]
        
        elif Year=='2021' and Quarter=='2':
            filtered_df = df[(df['Year'] == 2021) & (df['Quarter'] == 2)]
            filter_df=df[(df['Year'] == 2021) & (df['Quarter'] == 2) & (df['State'] == States)]
        
        elif Year=='2021' and Quarter=='3':
            filtered_df = df[(df['Year'] == 2021) & (df['Quarter'] == 3)]
            filter_df=df[(df['Year'] == 2021) & (df['Quarter'] == 3) & (df['State'] == States)]
        
        elif Year=='2021' and Quarter=='4':
            filtered_df = df[(df['Year'] == 2021) & (df['Quarter'] == 4)]
            filter_df=df[(df['Year'] == 2021) & (df['Quarter'] == 4) & (df['State'] == States)]

        elif Year=='2022' and Quarter=='1':
            filtered_df = df[(df['Year'] == 2022) & (df['Quarter'] == 1)]
            filter_df=df[(df['Year'] == 2022) & (df['Quarter'] == 1) & (df['State'] == States)]
        
        elif Year=='2022' and Quarter=='2':
            filtered_df = df[(df['Year'] == 2022) & (df['Quarter'] == 2)]
            filter_df=df[(df['Year'] == 2022) & (df['Quarter'] == 2) & (df['State'] == States)]
        
        elif Year=='2022' and Quarter=='3':
            filtered_df = df[(df['Year'] == 2022) & (df['Quarter'] == 3)]
            filter_df=df[(df['Year'] == 2022) & (df['Quarter'] == 3) & (df['State'] == States)]
        
        elif Year=='2022' and Quarter=='4':
            filtered_df = df[(df['Year'] == 2022) & (df['Quarter'] == 4)]
            filter_df=df[(df['Year'] == 2022) & (df['Quarter'] == 4) & (df['State'] == States)]

        elif Year=='2023' and Quarter=='1':
            filtered_df = df[(df['Year'] == 2023) & (df['Quarter'] == 1)]
            filter_df=df[(df['Year'] == 2023) & (df['Quarter'] == 1) & (df['State'] == States)]
        
        elif Year=='2023' and Quarter=='2':
            filtered_df = df[(df['Year'] == 2023) & (df['Quarter'] == 2)]
            filter_df=df[(df['Year'] == 2023) & (df['Quarter'] == 2) & (df['State'] == States)]
        
        elif Year=='2023' and Quarter=='3':
            filtered_df = df[(df['Year'] == 2023) & (df['Quarter'] == 3)]
            filter_df=df[(df['Year'] == 2023) & (df['Quarter'] == 3) & (df['State'] == States)]
        
        elif Year=='2023' and Quarter=='4':
            filtered_df = df[(df['Year'] == 2023) & (df['Quarter'] == 4)]
            filter_df=df[(df['Year'] == 2023) & (df['Quarter'] == 4) & (df['State'] == States)]
        # Group by state and sum the transaction amount
        result_amount = filtered_df.groupby('State')['Transaction_amount'].sum().reset_index()
        result_count = filtered_df.groupby('State')['Transaction_Count'].sum().reset_index()
    
        top_10_states_amount = result_amount.nlargest(10, 'Transaction_amount')
        top_10_states_count = result_count.nlargest(10, 'Transaction_Count')
        top10_distict_amount = filter_df.nlargest(10, 'Transaction_amount')
        top10_distict_count = filter_df.nlargest(10, 'Transaction_Count')
        col1,col2=st.columns(2)
        custom_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666', '#c2f0c2', '#c2f0f0', '#ffb3b3']

        with col1:
            st.subheader(':blue[Top 10 states based on Total amount transaction.]')
            fig1, ax1 = plt.subplots(figsize=(4,4))
            ax1.pie(top_10_states_amount['Transaction_amount'], labels=top_10_states_amount['State'], autopct='%1.1f%%',colors=custom_colors)
            st.pyplot(fig1)
            st.subheader('')
            st.markdown("""---""")
            st.subheader('')
            fig1, ax1 = plt.subplots(figsize=(10, 6))  # Adjust the figsize as needed
            ax1.bar(top_10_states_amount['State'], top_10_states_amount['Transaction_amount'], color=custom_colors)
            ax1.set_title("Transaction Amount Distribution by State")
            ax1.set_xlabel('State')
            ax1.set_ylabel('Transaction Amount')
            ax1.ticklabel_format(style='plain', axis='y')  # Display y-axis labels as plain numbers
            plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
            st.pyplot(fig1)

            st.markdown("""---""")
            st.subheader(':blue[Transaction Amount Distribution by Districts]')
            fig5, ax5 = plt.subplots(figsize=(10, 6))  # Adjust the figsize as needed
            ax5.bar(top10_distict_amount['Districts'], top10_distict_amount['Transaction_amount'],color=custom_colors)
            ax5.set_xlabel('Districts')
            ax5.set_ylabel('Transaction Amount')
            ax5.ticklabel_format(style='plain', axis='y')  # Display y-axis labels as plain numbers
            plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
            st.pyplot(fig5)

        with col2:
            st.subheader(':blue[Top 10 states based on Total number of transaction.]')
            fig2, ax2 = plt.subplots(figsize=(4,4))
            ax2.pie(top_10_states_count['Transaction_Count'], labels=top_10_states_count['State'], autopct='%1.1f%%',colors=custom_colors)
            st.pyplot(fig2)
            st.markdown("""---""")
            st.title('')
            fig1, ax1 = plt.subplots(figsize=(10, 6))  # Adjust the figsize as needed
            ax1.bar(top_10_states_count['State'], top_10_states_count['Transaction_Count'], color=custom_colors)
            ax1.set_title('Transaction Count Distribution by State')
            ax1.set_xlabel('State')
            ax1.set_ylabel('Transaction Cmount')
            ax1.ticklabel_format(style='plain', axis='y')  # Display y-axis labels as plain numbers
            plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
            st.pyplot(fig1)
            st.markdown("""---""")
            st.subheader(':blue[Transaction Count Distribution by Districts]')
            fig5, ax5 = plt.subplots(figsize=(10, 6))  # Adjust the figsize as needed
            ax5.bar(top10_distict_amount['Districts'], top10_distict_amount['Transaction_Count'],color=custom_colors)
            ax5.set_xlabel('Districts')
            ax5.set_ylabel('Transaction Count')
            ax5.ticklabel_format(style='plain', axis='y')  # Display y-axis labels as plain numbers
            plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
            st.pyplot(fig5)        

    if option=='Users':
        col1,col2=st.columns(2)
        custom_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666', '#c2f0c2', '#c2f0f0', '#ffb3b3']
        mycursor.execute('use phonepe')

        mycursor.execute('''select * from aggusers''')
        out=mycursor.fetchall()
        header=[i[0] for i in mycursor.description]
        brands=pd.DataFrame(out,columns=header)

        mycursor.execute('select * from mapusers')
        out1=mycursor.fetchall()
        header=[i[0] for i in mycursor.description]
        data=pd.DataFrame(out1,columns=header)

        if Year=='2018' and Quarter=='1':

            filtered_df=brands[(brands['Year']==2018) & (brands['Quarter']==1)] 
            filter_df=brands[(brands['Year']==2018) & (brands['Quarter']==1) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2018) & (data['Quarter']==1)]
            RegUsers_dis=data[(data['Year']==2018) & (data['Quarter']==1) & (data['State'] == States)]

        elif Year=='2018' and Quarter=='2':

            filtered_df=brands[(brands['Year']==2018) & (brands['Quarter']==2)]    
            filter_df=brands[(brands['Year']==2018) & (brands['Quarter']==2) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2018) & (data['Quarter']==2)]
            RegUsers_dis=data[(data['Year']==2018) & (data['Quarter']==2) & (data['State'] == States)]

        elif Year=='2018' and Quarter=='3':

            filtered_df=brands[(brands['Year']==2018) & (brands['Quarter']==3)]   
            filter_df=brands[(brands['Year']==2018) & (brands['Quarter']==3) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2018) & (data['Quarter']==3)]
            RegUsers_dis=data[(data['Year']==2018) & (data['Quarter']==3) & (data['State'] == States)]

        elif Year=='2018' and Quarter=='4':

            filtered_df=brands[(brands['Year']==2018) & (brands['Quarter']==4)]  
            filter_df=brands[(brands['Year']==2018) & (brands['Quarter']==4) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2018) & (data['Quarter']==4)]
            RegUsers_dis=data[(data['Year']==2018) & (data['Quarter']==4) & (data['State'] == States)]

        elif Year=='2019' and Quarter=='1':

            filtered_df=brands[(brands['Year']==2019) & (brands['Quarter']==1)]   
            filter_df=brands[(brands['Year']==2019) & (brands['Quarter']==1) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2019) & (data['Quarter']==1)]
            RegUsers_dis=data[(data['Year']==2019) & (data['Quarter']==1) & (data['State'] == States)]

        elif Year=='2019' and Quarter=='2':

            filtered_df=brands[(brands['Year']==2019) & (brands['Quarter']==2)] 
            filter_df=brands[(brands['Year']==2019) & (brands['Quarter']==2) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2019) & (data['Quarter']==2)]
            RegUsers_dis=data[(data['Year']==2019) & (data['Quarter']==2) & (data['State'] == States)]

        elif Year=='2019' and Quarter=='3':

            filtered_df=brands[(brands['Year']==2019) & (brands['Quarter']==3)]   
            filter_df=brands[(brands['Year']==2019) & (brands['Quarter']==3) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2019) & (data['Quarter']==3)]
            RegUsers_dis=data[(data['Year']==2019) & (data['Quarter']==3) & (data['State'] == States)]

        elif Year=='2019' and Quarter=='4':

            filtered_df=brands[(brands['Year']==2019) & (brands['Quarter']==4)] 
            filter_df=brands[(brands['Year']==2019) & (brands['Quarter']==4) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2019) & (data['Quarter']==4)]
            RegUsers_dis=data[(data['Year']==2019) & (data['Quarter']==4) & (data['State'] == States)]

        elif Year=='2020' and Quarter=='1':

            filtered_df=brands[(brands['Year']==2020) & (brands['Quarter']==1)]
            filter_df=brands[(brands['Year']==2020) & (brands['Quarter']==1) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2020) & (data['Quarter']==1)]
            RegUsers_dis=data[(data['Year']==2020) & (data['Quarter']==1) & (data['State'] == States)]

        elif Year=='2020' and Quarter=='2':

            filtered_df=brands[(brands['Year']==2020) & (brands['Quarter']==2)]  
            filter_df=brands[(brands['Year']==2020) & (brands['Quarter']==2) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2020) & (data['Quarter']==2)]
            RegUsers_dis=data[(data['Year']==2020) & (data['Quarter']==2) & (data['State'] == States)]

        elif Year=='2020' and Quarter=='3':

            filtered_df=brands[(brands['Year']==2020) & (brands['Quarter']==3)]
            filter_df=brands[(brands['Year']==2020) & (brands['Quarter']==3) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2020) & (data['Quarter']==3)]
            RegUsers_dis=data[(data['Year']==2020) & (data['Quarter']==3) & (data['State'] == States)]

        elif Year=='2020' and Quarter=='4':

            filtered_df=brands[(brands['Year']==2020) & (brands['Quarter']==4)]   
            filter_df=brands[(brands['Year']==2020) & (brands['Quarter']==4) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2020) & (data['Quarter']==4)]
            RegUsers_dis=data[(data['Year']==2020) & (data['Quarter']==4) & (data['State'] == States)]

        elif Year=='2021' and Quarter=='1':

            filtered_df=brands[(brands['Year']==2021) & (brands['Quarter']==1)]   
            filter_df=brands[(brands['Year']==2021) & (brands['Quarter']==1) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2021) & (data['Quarter']==1)]
            RegUsers_dis=data[(data['Year']==2021) & (data['Quarter']==1) & (data['State'] == States)]

        elif Year=='2021' and Quarter=='2':

            filtered_df=brands[(brands['Year']==2021) & (brands['Quarter']==2)]
            filter_df=brands[(brands['Year']==2021) & (brands['Quarter']==2) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2021) & (data['Quarter']==2)]
            RegUsers_dis=data[(data['Year']==2021) & (data['Quarter']==2) & (data['State'] == States)]

        elif Year=='2021' and Quarter=='3':

            filtered_df=brands[(brands['Year']==2021) & (brands['Quarter']==3)]  
            filter_df=brands[(brands['Year']==2021) & (brands['Quarter']==3) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2021) & (data['Quarter']==3)]
            RegUsers_dis=data[(data['Year']==2021) & (data['Quarter']==3) & (data['State'] == States)]

        elif Year=='2021' and Quarter=='4':

            filtered_df=brands[(brands['Year']==2021) & (brands['Quarter']==4)]  
            filter_df=brands[(brands['Year']==2021) & (brands['Quarter']==4) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2021) & (data['Quarter']==4)]
            RegUsers_dis=data[(data['Year']==2021) & (data['Quarter']==4) & (data['State'] == States)]

        elif Year=='2022' and Quarter=='1':

            filtered_df=brands[(brands['Year']==2022) & (brands['Quarter']==1)] 
            filter_df=brands[(brands['Year']==2022) & (brands['Quarter']==1) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2022) & (data['Quarter']==1)]
            RegUsers_dis=data[(data['Year']==2022) & (data['Quarter']==1) & (data['State'] == States)]

        elif Year=='2022' and Quarter=='2':

            filtered_df=brands[(brands['Year']==2022) & (brands['Quarter']==1)]    
            filter_df=brands[(brands['Year']==2022) & (brands['Quarter']==1) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2022) & (data['Quarter']==2)]
            RegUsers_dis=data[(data['Year']==2022) & (data['Quarter']==2) & (data['State'] == States)]

        elif Year=='2022' and Quarter=='3':

            filtered_df=brands[(brands['Year']==2022) & (brands['Quarter']==1)]   
            filter_df=brands[(brands['Year']==2022) & (brands['Quarter']==1) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2022) & (data['Quarter']==3)]
            RegUsers_dis=data[(data['Year']==2022) & (data['Quarter']==3) & (data['State'] == States)]

        elif Year=='2022' and Quarter=='4':

            filtered_df=brands[(brands['Year']==2022) & (brands['Quarter']==1)]    
            filter_df=brands[(brands['Year']==2022) & (brands['Quarter']==1) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2022) & (data['Quarter']==4)]
            RegUsers_dis=data[(data['Year']==2022) & (data['Quarter']==4) & (data['State'] == States)]

        elif Year=='2023' and Quarter=='1':

            filtered_df=brands[(brands['Year']==2020) & (brands['Quarter']==1)]
            filter_df=brands[(brands['Year']==2020) & (brands['Quarter']==1) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2023) & (data['Quarter']==1)]
            RegUsers_dis=data[(data['Year']==2023) & (data['Quarter']==1) & (data['State'] == States)]

        elif Year=='2023' and Quarter=='2':

            filtered_df=brands[(brands['Year']==2020) & (brands['Quarter']==2)]
            filter_df=brands[(brands['Year']==2020) & (brands['Quarter']==2) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2023) & (data['Quarter']==2)]
            RegUsers_dis=data[(data['Year']==2023) & (data['Quarter']==2) & (data['State'] == States)]

        elif Year=='2023' and Quarter=='3':

            filtered_df=brands[(brands['Year']==2020) & (brands['Quarter']==3)]
            filter_df=brands[(brands['Year']==2020) & (brands['Quarter']==3) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2023) & (data['Quarter']==3)]
            RegUsers_dis=data[(data['Year']==2023) & (data['Quarter']==3) & (data['State'] == States)]

        elif Year=='2023' and Quarter=='4':

            filtered_df=brands[(brands['Year']==2020) & (brands['Quarter']==4)]
            filter_df=brands[(brands['Year']==2020) & (brands['Quarter']==4) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2023) & (data['Quarter']==4)]
            RegUsers_dis=data[(data['Year']==2023) & (data['Quarter']==4) & (data['State'] == States)]

        result_count = filtered_df.groupby('brand')['Count'].sum().reset_index()
        result_state = filter_df.groupby('brand')['Count'].sum().reset_index()

        result_reguser=RegUsers.groupby('State')['RegisteredUsers'].sum().reset_index()
        top_10_RegUsers=result_reguser.nlargest(10,'RegisteredUsers')

        result_reguser_dis=RegUsers_dis.groupby('Districts')['RegisteredUsers'].sum().reset_index()
        top_10_RegUsers_dis=result_reguser_dis.nlargest(10,'RegisteredUsers')
                                                    
        result_open=RegUsers.groupby('State')['AppOpens'].sum().reset_index()
        top_10_OpenUsers=result_open.nlargest(10,'AppOpens')

        result_open_dis=RegUsers_dis.groupby('Districts')['AppOpens'].sum().reset_index()
        top_10_OpenUsers_dis=result_open_dis.nlargest(10,'AppOpens')
            
        with col1:

            st.subheader(':blue[Overall Users Distribution by Brands]')
            fig5, ax5 = plt.subplots(figsize=(10, 6))  # Adjust the figsize as needed
            ax5.bar(result_count['brand'], result_count['Count'],color=custom_colors)
            ax5.set_xlabel('Brands')
            ax5.set_ylabel('Counts')
            ax5.ticklabel_format(style='plain', axis='y')  # Display y-axis labels as plain numbers
            plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
            st.pyplot(fig5)
            st.markdown("""---""")

            st.subheader(':blue[Number of Registered Users Distribution by State]')
            fig1, ax1 = plt.subplots(figsize=(4,4))
            ax1.pie(top_10_RegUsers['RegisteredUsers'], labels=top_10_RegUsers['State'], autopct='%1.1f%%',colors=custom_colors)
            st.pyplot(fig1) 
            st.markdown("""---""")

            st.subheader(':blue[Number of Registered Users Distribution by Districts]')
            fig2, ax2 = plt.subplots(figsize=(10, 6))  # Adjust the figsize as needed
            ax2.bar(top_10_RegUsers_dis['Districts'],top_10_RegUsers_dis['RegisteredUsers'],color=custom_colors)
            ax2.set_xlabel('Districts')
            ax2.set_ylabel('RegisteredUsers')
            ax2.ticklabel_format(style='plain', axis='y')  # Display y-axis labels as plain numbers
            plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
            st.pyplot(fig2)

        with col2:
            st.subheader(':blue[State Wise Users Distribution by Brands]')
            fig1, ax1 = plt.subplots(figsize=(10, 6))  # Adjust the figsize as needed
            ax1.bar(result_state['brand'], result_state['Count'],color=custom_colors)
            ax1.set_xlabel('Brands')
            ax1.set_ylabel('Counts')
            ax1.ticklabel_format(style='plain', axis='y')  # Display y-axis labels as plain numbers
            plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
            st.pyplot(fig1)
            st.markdown("""---""")

            st.subheader(':blue[Active Users Distribution by State]')
            fig1, ax1 = plt.subplots(figsize=(10, 6))  # Adjust the figsize as needed
            ax1.bar(top_10_OpenUsers['State'],top_10_OpenUsers['AppOpens'],color=custom_colors)
            ax1.set_xlabel('State')
            ax1.set_ylabel('AppOpens')
            ax1.ticklabel_format(style='plain', axis='y')  # Display y-axis labels as plain numbers
            plt.xticks(rotation=65)  # Rotate x-axis labels for better readability
            st.pyplot(fig1) 
            st.markdown("""---""")     

            st.subheader(':blue[Active Users Distribution by Districts]')
            fig1, ax1 = plt.subplots(figsize=(10, 6))  # Adjust the figsize as needed
            ax1.bar(top_10_OpenUsers_dis['Districts'],top_10_OpenUsers_dis['AppOpens'],color=custom_colors)
            ax1.set_xlabel('Districts')
            ax1.set_ylabel('AppOpens')
            ax1.ticklabel_format(style='plain', axis='y')  # Display y-axis labels as plain numbers
            plt.xticks(rotation=65)  # Rotate x-axis labels for better readability
            st.pyplot(fig1)

# option --> Explore data 
if SELECT=='Explore Data':
    st.subheader(':blue[EXPLORE DATA]')
    option = st.selectbox("Type",("Transaction", "Users"),index=0)
    co1,co2=st.columns(2)
    with co1:
        Year= st.select_slider('Year',options=['2018', '2019', '2020', '2021', '2022', '2023'])
        Quarter=st.select_slider('Quarter',options=['1', '2', '3', '4'])
        States=st.selectbox('State',('Andaman & Nicobar','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar',
                    'Chandigarh','Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat',
                    'Haryana','Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Ladakh',
                    'Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry',
                    'Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal'))
    with co2: 
        st.text('FROM THIS MENU WE CAN GET THE DETAILS LIKE:')
        st.caption('overall states based on Total amount transaction on phonepe.')
        st.caption('overall states based on Total number of  transaction on phonepe.')
        st.caption('overall mobile brand based on the how many people use phonepe.')
        st.caption('overall State,District based on Total phonepe users and their app opening')
    # option Transaction
    if option=='Transaction':

        mycursor.execute('use phonepe')

        mycursor.execute('''select * from maptrans''')
        out=mycursor.fetchall()
        header=[i[0] for i in mycursor.description]
        df=pd.DataFrame(out,columns=header)

        mycursor.execute('''select * from aggtrans''')
        out=mycursor.fetchall()
        header=[i[0] for i in mycursor.description]
        data=pd.DataFrame(out,columns=header)
        # Filter the DataFrame for the year 2018 and quarter 1
        if Year=='2018' and Quarter=='1':
            filtered_df = df[(df['Year'] == 2018) & (df['Quarter'] == 1)]
            filter_df=df[(df['Year'] == 2018) & (df['Quarter'] == 1) & (df['State'] == States)]
            
            filtered_data=data[(data['Year']==2018) & (data['Quarter']==1)]

        elif Year=='2018' and Quarter=='2':
            filtered_df = df[(df['Year'] == 2018) & (df['Quarter'] == 2)]
            filter_df=df[(df['Year'] == 2018) & (df['Quarter'] == 2) & (df['State'] == States)]

            filtered_data=data[(data['Year']==2018) & (data['Quarter']==2)]
        
        elif Year=='2018' and Quarter=='3':
            filtered_df = df[(df['Year'] == 2018) & (df['Quarter'] == 3)]
            filter_df=df[(df['Year'] == 2018) & (df['Quarter'] == 3) & (df['State'] == States)]

            filtered_data=data[(data['Year']==2018) & (data['Quarter']==3)]
        
        elif Year=='2018' and Quarter=='4':
            filtered_df = df[(df['Year'] == 2018) & (df['Quarter'] == 4)]
            filter_df=df[(df['Year'] == 2018) & (df['Quarter'] == 4) & (df['State'] == States)]
            filtered_data=data[(data['Year']==2018) & (data['Quarter']==4)]

        elif Year=='2019' and Quarter=='1':
            filtered_df = df[(df['Year'] == 2019) & (df['Quarter'] == 1)]
            filter_df=df[(df['Year'] == 2019) & (df['Quarter'] == 1) & (df['State'] == States)]
            filtered_data=data[(data['Year']==2019) & (data['Quarter']==1)]
        
        elif Year=='2019' and Quarter=='2':
            filtered_df = df[(df['Year'] == 2019) & (df['Quarter'] == 2)]
            filter_df=df[(df['Year'] == 2019) & (df['Quarter'] == 2) & (df['State'] == States)]
            filtered_data=data[(data['Year']==2019) & (data['Quarter']==2)]
        
        elif Year=='2019' and Quarter=='3':
            filtered_df = df[(df['Year'] == 2019) & (df['Quarter'] == 3)]
            filter_df=df[(df['Year'] == 2019) & (df['Quarter'] == 3) & (df['State'] == States)]
            filtered_data=data[(data['Year']==2019) & (data['Quarter']==3)]
        
        elif Year=='2019' and Quarter=='4':
            filtered_df = df[(df['Year'] == 2019) & (df['Quarter'] == 4)]
            filter_df=df[(df['Year'] == 2019) & (df['Quarter'] == 4) & (df['State'] == States)]
            filtered_data=data[(data['Year']==2019) & (data['Quarter']==4)] 

        elif Year=='2020' and Quarter=='1':
            filtered_df = df[(df['Year'] == 2020) & (df['Quarter'] == 1)]
            filter_df=df[(df['Year'] == 2020) & (df['Quarter'] == 1) & (df['State'] == States)]
            filtered_data=data[(data['Year']==2020) & (data['Quarter']==1)]
        
        elif Year=='2020' and Quarter=='2':
            filtered_df = df[(df['Year'] == 2020) & (df['Quarter'] == 2)]
            filter_df=df[(df['Year'] == 2020) & (df['Quarter'] == 2) & (df['State'] == States)]
            filtered_data=data[(data['Year']==2020) & (data['Quarter']==2)]

        elif Year=='2020' and Quarter=='3':
            filtered_df = df[(df['Year'] == 2020) & (df['Quarter'] == 3)]
            filter_df=df[(df['Year'] == 2020) & (df['Quarter'] == 3) & (df['State'] == States)]
            filtered_data=data[(data['Year']==2020) & (data['Quarter']==3)]
        
        elif Year=='2020' and Quarter=='4':
            filtered_df = df[(df['Year'] == 2020) & (df['Quarter'] == 4)]
            filter_df=df[(df['Year'] == 2020) & (df['Quarter'] == 4) & (df['State'] == States)]
            filtered_data=data[(data['Year']==2020) & (data['Quarter']==4)]

        elif Year=='2021' and Quarter=='1':
            filtered_df = df[(df['Year'] == 2021) & (df['Quarter'] == 1)]
            filter_df=df[(df['Year'] == 2021) & (df['Quarter'] == 1) & (df['State'] == States)]
            filtered_data=data[(data['Year']==2021) & (data['Quarter']==1)]
        
        elif Year=='2021' and Quarter=='2':
            filtered_df = df[(df['Year'] == 2021) & (df['Quarter'] == 2)]
            filter_df=df[(df['Year'] == 2021) & (df['Quarter'] == 2) & (df['State'] == States)]
            filtered_data=data[(data['Year']==2021) & (data['Quarter']==2)]
        
        elif Year=='2021' and Quarter=='3':
            filtered_df = df[(df['Year'] == 2021) & (df['Quarter'] == 3)]
            filter_df=df[(df['Year'] == 2021) & (df['Quarter'] == 3) & (df['State'] == States)]
            filtered_data=data[(data['Year']==2021) & (data['Quarter']==3)]
        
        elif Year=='2021' and Quarter=='4':
            filtered_df = df[(df['Year'] == 2021) & (df['Quarter'] == 4)]
            filter_df=df[(df['Year'] == 2021) & (df['Quarter'] == 4) & (df['State'] == States)]
            filtered_data=data[(data['Year']==2021) & (data['Quarter']==4)]

        elif Year=='2022' and Quarter=='1':
            filtered_df = df[(df['Year'] == 2022) & (df['Quarter'] == 1)]
            filter_df=df[(df['Year'] == 2022) & (df['Quarter'] == 1) & (df['State'] == States)]
            filtered_data=data[(data['Year']==2022) & (data['Quarter']==1)]
        
        elif Year=='2022' and Quarter=='2':
            filtered_df = df[(df['Year'] == 2022) & (df['Quarter'] == 2)]
            filter_df=df[(df['Year'] == 2022) & (df['Quarter'] == 2) & (df['State'] == States)]
            filtered_data=data[(data['Year']==2022) & (data['Quarter']==2)]
        
        elif Year=='2022' and Quarter=='3':
            filtered_df = df[(df['Year'] == 2022) & (df['Quarter'] == 3)]
            filter_df=df[(df['Year'] == 2022) & (df['Quarter'] == 3) & (df['State'] == States)]
            filtered_data=data[(data['Year']==2022) & (data['Quarter']==3)]
        
        elif Year=='2022' and Quarter=='4':
            filtered_df = df[(df['Year'] == 2022) & (df['Quarter'] == 4)]
            filter_df=df[(df['Year'] == 2022) & (df['Quarter'] == 4) & (df['State'] == States)]
            filtered_data=data[(data['Year']==2022) & (data['Quarter']==4)]

        elif Year=='2023' and Quarter=='1':
            filtered_df = df[(df['Year'] == 2023) & (df['Quarter'] == 1)]
            filter_df=df[(df['Year'] == 2023) & (df['Quarter'] == 1) & (df['State'] == States)]
            filtered_data=data[(data['Year']==2023) & (data['Quarter']==1)]
        
        elif Year=='2023' and Quarter=='2':
            filtered_df = df[(df['Year'] == 2023) & (df['Quarter'] == 2)]
            filter_df=df[(df['Year'] == 2023) & (df['Quarter'] == 2) & (df['State'] == States)]
            filtered_data=data[(data['Year']==2023) & (data['Quarter']==2)]

        
        elif Year=='2023' and Quarter=='3':
            filtered_df = df[(df['Year'] == 2023) & (df['Quarter'] == 3)]
            filter_df=df[(df['Year'] == 2023) & (df['Quarter'] == 3) & (df['State'] == States)]
            filtered_data=data[(data['Year']==2023) & (data['Quarter']==3)]
        
        elif Year=='2023' and Quarter=='4':
            filtered_df = df[(df['Year'] == 2023) & (df['Quarter'] == 4)]
            filter_df=df[(df['Year'] == 2023) & (df['Quarter'] == 4) & (df['State'] == States)]
            filtered_data=data[(data['Year']==2023) & (data['Quarter']==4)]
            # Group by state and sum the transaction amount
        
        
        result_amount = filtered_df.groupby('State')['Transaction_amount'].sum().reset_index()
        result_count = filtered_df.groupby('State')['Transaction_Count'].sum().reset_index()

        result_data_amount=filtered_data.groupby('Transaction_type')['Transaction_amount'].sum().reset_index()
        result_data_count=filtered_data.groupby('Transaction_type')['Transaction_count'].sum().reset_index()

        col1,col2=st.columns(2)
        custom_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666', '#c2f0c2', '#c2f0f0', '#ffb3b3', '#b3ffb3', '#b3b3ff', '#ffccff', '#ffff99', '#ccccff',
                        '#ff99cc', '#ffccff', '#ccffcc', '#ff6666', '#66ff66', '#6666ff', '#ff9933', '#ffff00', '#33ccff', '#ff99cc', '#ff99ff', '#ccff99', '#99ccff', '#ff3399', '#ffcc66', 
                        '#6699ff', '#ff9933', '#99ff99', '#ff99cc', '#ff6666']

        with col1:
            st.subheader(':blue[Explore Transaction amount distribution by state.]')
            fig1 = px.choropleth(
                df,
                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM',
                locations=result_amount['State'],
                color=result_amount['Transaction_amount'],
                color_continuous_scale='tropic'
            )
            fig1.update_geos(fitbounds="locations",visible=False)
            fig1.update_layout(width=600, height=400)
            st.plotly_chart(fig1)

            st.markdown("""---""")
            st.subheader(":blue[Explore Transaction Types by year wise]")
            fig1, ax1 = plt.subplots(figsize=(6,6))
            ax1.pie(result_data_count['Transaction_count'], labels=result_data_count['Transaction_type'],autopct='%1.1f%%')
            ax1.set_title('Number of Transaction  Distribution by Types')
            st.pyplot(fig1)

        with col2:
            st.subheader(':blue[Explore Transaction Count distribution by state.]')
            fig1 = px.choropleth(
                df,
                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM',
                locations=result_count['State'],
                color=result_count['Transaction_Count'],
                color_continuous_scale='tropic'
            )
            fig1.update_geos(fitbounds="locations",visible=False)
            fig1.update_layout(width=600, height=400)
            st.plotly_chart(fig1)
            st.title('')
            st.markdown("""---""")
            st.title('')
            st.caption('')
            fig1, ax1 = plt.subplots(figsize=(6,6))
            ax1.pie(result_data_amount['Transaction_amount'], labels=result_data_amount['Transaction_type'],autopct='%1.1f%%')
            ax1.set_title('Transaction Amount Distribution by Types')
            st.pyplot(fig1)
        st.markdown("""---""")
        st.subheader(':blue[Explore Transaction Amount by District Wise]')
        fig5, ax5 = plt.subplots(figsize=(18,8))  # Adjust the figsize as needed
        ax5.bar(filter_df['Districts'], filter_df['Transaction_amount'],color=custom_colors)
        ax5.set_xlabel('Districts')
        ax5.set_ylabel('Transaction Amount')
        ax5.ticklabel_format(style='plain', axis='y')  # Display y-axis labels as plain numbers
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        st.pyplot(fig5)

        st.markdown("""---""")
        st.subheader(':blue[Explore Number of Transaction Distribution by District Wise]')
        fig5, ax5 = plt.subplots(figsize=(18,8))  # Adjust the figsize as needed
        ax5.bar(filter_df['Districts'], filter_df['Transaction_Count'],color=custom_colors)
        ax5.set_xlabel('Districts')
        ax5.set_ylabel('Transaction Count')
        ax5.ticklabel_format(style='plain', axis='y')  # Display y-axis labels as plain numbers
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        st.pyplot(fig5)        

    if option=='Users':
        col1,col2=st.columns(2)
        custom_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666', '#c2f0c2', '#c2f0f0', '#ffb3b3', '#b3ffb3', '#b3b3ff', '#ffccff', '#ffff99', '#ccccff',
                        '#ff99cc', '#ffccff', '#ccffcc', '#ff6666', '#66ff66', '#6666ff', '#ff9933', '#ffff00', '#33ccff', '#ff99cc', '#ff99ff', '#ccff99', '#99ccff', '#ff3399', '#ffcc66', 
                        '#6699ff', '#ff9933', '#99ff99', '#ff99cc', '#ff6666']

        mycursor.execute('use phonepe')

        mycursor.execute('''select * from aggusers''')
        out=mycursor.fetchall()
        header=[i[0] for i in mycursor.description]
        brands=pd.DataFrame(out,columns=header)

        mycursor.execute('select * from mapusers')
        out1=mycursor.fetchall()
        header=[i[0] for i in mycursor.description]
        data=pd.DataFrame(out1,columns=header)

        mycursor.execute('''select * from aggtrans''')
        out2=mycursor.fetchall()
        header=[i[0] for i in mycursor.description]
        data1=pd.DataFrame(out2,columns=header)

        if Year=='2018' and Quarter=='1':

            filtered_df=brands[(brands['Year']==2018) & (brands['Quarter']==1)] 
            filter_df=brands[(brands['Year']==2018) & (brands['Quarter']==1) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2018) & (data['Quarter']==1)]
            RegUsers_dis=data[(data['Year']==2018) & (data['Quarter']==1) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2018) & (data1['Quarter']==1)]

        elif Year=='2018' and Quarter=='2':

            filtered_df=brands[(brands['Year']==2018) & (brands['Quarter']==2)]    
            filter_df=brands[(brands['Year']==2018) & (brands['Quarter']==2) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2018) & (data['Quarter']==2)]
            RegUsers_dis=data[(data['Year']==2018) & (data['Quarter']==2) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2018) & (data1['Quarter']==2)]

        elif Year=='2018' and Quarter=='3':

            filtered_df=brands[(brands['Year']==2018) & (brands['Quarter']==3)]   
            filter_df=brands[(brands['Year']==2018) & (brands['Quarter']==3) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2018) & (data['Quarter']==3)]
            RegUsers_dis=data[(data['Year']==2018) & (data['Quarter']==3) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2018) & (data1['Quarter']==3)]

        elif Year=='2018' and Quarter=='4':

            filtered_df=brands[(brands['Year']==2018) & (brands['Quarter']==4)]  
            filter_df=brands[(brands['Year']==2018) & (brands['Quarter']==4) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2018) & (data['Quarter']==4)]
            RegUsers_dis=data[(data['Year']==2018) & (data['Quarter']==4) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2018) & (data1['Quarter']==4)]

        elif Year=='2019' and Quarter=='1':

            filtered_df=brands[(brands['Year']==2019) & (brands['Quarter']==1)]   
            filter_df=brands[(brands['Year']==2019) & (brands['Quarter']==1) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2019) & (data['Quarter']==1)]
            RegUsers_dis=data[(data['Year']==2019) & (data['Quarter']==1) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2019) & (data1['Quarter']==1)]

        elif Year=='2019' and Quarter=='2':

            filtered_df=brands[(brands['Year']==2019) & (brands['Quarter']==2)] 
            filter_df=brands[(brands['Year']==2019) & (brands['Quarter']==2) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2019) & (data['Quarter']==2)]
            RegUsers_dis=data[(data['Year']==2019) & (data['Quarter']==2) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2019) & (data1['Quarter']==2)]

        elif Year=='2019' and Quarter=='3':

            filtered_df=brands[(brands['Year']==2019) & (brands['Quarter']==3)]   
            filter_df=brands[(brands['Year']==2019) & (brands['Quarter']==3) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2019) & (data['Quarter']==3)]
            RegUsers_dis=data[(data['Year']==2019) & (data['Quarter']==3) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2019) & (data1['Quarter']==3)]

        elif Year=='2019' and Quarter=='4':

            filtered_df=brands[(brands['Year']==2019) & (brands['Quarter']==4)] 
            filter_df=brands[(brands['Year']==2019) & (brands['Quarter']==4) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2019) & (data['Quarter']==4)]
            RegUsers_dis=data[(data['Year']==2019) & (data['Quarter']==4) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2019) & (data1['Quarter']==4)]

        elif Year=='2020' and Quarter=='1':

            filtered_df=brands[(brands['Year']==2020) & (brands['Quarter']==1)]
            filter_df=brands[(brands['Year']==2020) & (brands['Quarter']==1) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2020) & (data['Quarter']==1)]
            RegUsers_dis=data[(data['Year']==2020) & (data['Quarter']==1) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2020) & (data1['Quarter']==1)]

        elif Year=='2020' and Quarter=='2':

            filtered_df=brands[(brands['Year']==2020) & (brands['Quarter']==2)]  
            filter_df=brands[(brands['Year']==2020) & (brands['Quarter']==2) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2020) & (data['Quarter']==2)]
            RegUsers_dis=data[(data['Year']==2020) & (data['Quarter']==2) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2020) & (data1['Quarter']==2)]

        elif Year=='2020' and Quarter=='3':

            filtered_df=brands[(brands['Year']==2020) & (brands['Quarter']==3)]
            filter_df=brands[(brands['Year']==2020) & (brands['Quarter']==3) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2020) & (data['Quarter']==3)]
            RegUsers_dis=data[(data['Year']==2020) & (data['Quarter']==3) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2020) & (data1['Quarter']==3)]

        elif Year=='2020' and Quarter=='4':

            filtered_df=brands[(brands['Year']==2020) & (brands['Quarter']==4)]   
            filter_df=brands[(brands['Year']==2020) & (brands['Quarter']==4) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2020) & (data['Quarter']==4)]
            RegUsers_dis=data[(data['Year']==2020) & (data['Quarter']==4) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2020) & (data1['Quarter']==4)]

        elif Year=='2021' and Quarter=='1':

            filtered_df=brands[(brands['Year']==2021) & (brands['Quarter']==1)]   
            filter_df=brands[(brands['Year']==2021) & (brands['Quarter']==1) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2021) & (data['Quarter']==1)]
            RegUsers_dis=data[(data['Year']==2021) & (data['Quarter']==1) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2021) & (data1['Quarter']==1)]

        elif Year=='2021' and Quarter=='2':

            filtered_df=brands[(brands['Year']==2021) & (brands['Quarter']==2)]
            filter_df=brands[(brands['Year']==2021) & (brands['Quarter']==2) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2021) & (data['Quarter']==2)]
            RegUsers_dis=data[(data['Year']==2021) & (data['Quarter']==2) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2021) & (data1['Quarter']==2)]

        elif Year=='2021' and Quarter=='3':

            filtered_df=brands[(brands['Year']==2021) & (brands['Quarter']==3)]  
            filter_df=brands[(brands['Year']==2021) & (brands['Quarter']==3) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2021) & (data['Quarter']==3)]
            RegUsers_dis=data[(data['Year']==2021) & (data['Quarter']==3) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2021) & (data1['Quarter']==3)]

        elif Year=='2021' and Quarter=='4':

            filtered_df=brands[(brands['Year']==2021) & (brands['Quarter']==4)]  
            filter_df=brands[(brands['Year']==2021) & (brands['Quarter']==4) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2021) & (data['Quarter']==4)]
            RegUsers_dis=data[(data['Year']==2021) & (data['Quarter']==4) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2021) & (data1['Quarter']==4)]

        elif Year=='2022' and Quarter=='1':

            filtered_df=brands[(brands['Year']==2022) & (brands['Quarter']==1)] 
            filter_df=brands[(brands['Year']==2022) & (brands['Quarter']==1) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2022) & (data['Quarter']==1)]
            RegUsers_dis=data[(data['Year']==2022) & (data['Quarter']==1) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2022) & (data1['Quarter']==1)]

        elif Year=='2022' and Quarter=='2':

            filtered_df=brands[(brands['Year']==2022) & (brands['Quarter']==1)]    
            filter_df=brands[(brands['Year']==2022) & (brands['Quarter']==1) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2022) & (data['Quarter']==2)]
            RegUsers_dis=data[(data['Year']==2022) & (data['Quarter']==2) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2022) & (data1['Quarter']==2)]

        elif Year=='2022' and Quarter=='3':

            filtered_df=brands[(brands['Year']==2022) & (brands['Quarter']==1)]   
            filter_df=brands[(brands['Year']==2022) & (brands['Quarter']==1) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2022) & (data['Quarter']==3)]
            RegUsers_dis=data[(data['Year']==2022) & (data['Quarter']==3) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2022) & (data1['Quarter']==3)]

        elif Year=='2022' and Quarter=='4':

            filtered_df=brands[(brands['Year']==2022) & (brands['Quarter']==1)]    
            filter_df=brands[(brands['Year']==2022) & (brands['Quarter']==1) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2022) & (data['Quarter']==4)]
            RegUsers_dis=data[(data['Year']==2022) & (data['Quarter']==4) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2022) & (data1['Quarter']==4)]

        elif Year=='2023' and Quarter=='1':

            filtered_df=brands[(brands['Year']==2020) & (brands['Quarter']==1)]
            filter_df=brands[(brands['Year']==2020) & (brands['Quarter']==1) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2023) & (data['Quarter']==1)]
            RegUsers_dis=data[(data['Year']==2023) & (data['Quarter']==1) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2023) & (data1['Quarter']==1)]

        elif Year=='2023' and Quarter=='2':

            filtered_df=brands[(brands['Year']==2020) & (brands['Quarter']==2)]
            filter_df=brands[(brands['Year']==2020) & (brands['Quarter']==2) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2023) & (data['Quarter']==2)]
            RegUsers_dis=data[(data['Year']==2023) & (data['Quarter']==2) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2023) & (data1['Quarter']==2)]

        elif Year=='2023' and Quarter=='3':

            filtered_df=brands[(brands['Year']==2020) & (brands['Quarter']==3)]
            filter_df=brands[(brands['Year']==2020) & (brands['Quarter']==3) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2023) & (data['Quarter']==3)]
            RegUsers_dis=data[(data['Year']==2023) & (data['Quarter']==3) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2023) & (data1['Quarter']==3)]

        elif Year=='2023' and Quarter=='4':

            filtered_df=brands[(brands['Year']==2020) & (brands['Quarter']==4)]
            filter_df=brands[(brands['Year']==2020) & (brands['Quarter']==4) & (brands['State'] == States)]
            RegUsers=data[(data['Year']==2023) & (data['Quarter']==4)]
            RegUsers_dis=data[(data['Year']==2023) & (data['Quarter']==4) & (data['State'] == States)]
            filtered_data=data1[(data1['Year']==2023) & (data1['Quarter']==4)]

        result_count = filtered_df.groupby('brand')['Count'].sum().reset_index()
        result_state = filter_df.groupby('brand')['Count'].sum().reset_index()

        result_reguser=RegUsers.groupby('State')['RegisteredUsers'].sum().reset_index()
        top_10_RegUsers=result_reguser.nlargest(10,'RegisteredUsers')

        result_reguser_dis=RegUsers_dis.groupby('Districts')['RegisteredUsers'].sum().reset_index()
        top_10_RegUsers_dis=result_reguser_dis.nlargest(10,'RegisteredUsers')
                                                    
        result_open=RegUsers.groupby('State')['AppOpens'].sum().reset_index()
        top_10_OpenUsers=result_open.nlargest(10,'AppOpens')

        result_open_dis=RegUsers_dis.groupby('Districts')['AppOpens'].sum().reset_index()
        top_10_OpenUsers_dis=result_open_dis.nlargest(10,'AppOpens')

        result_data_count=filtered_data.groupby('Transaction_type')['Transaction_count'].sum().reset_index()
        result_data_amount=filtered_data.groupby('Transaction_type')['Transaction_amount'].sum().reset_index()
            
        with col1:

            st.title('')
            st.subheader(':blue[Overall Users Distribution by Brands]')
            fig5, ax5 = plt.subplots(figsize=(10, 6))  # Adjust the figsize as needed
            ax5.bar(result_count['brand'], result_count['Count'],color=custom_colors)
            ax5.set_xlabel('Brands')
            ax5.set_ylabel('Counts')
            ax5.ticklabel_format(style='plain', axis='y')  # Display y-axis labels as plain numbers
            plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
            st.pyplot(fig5)
            
            st.subheader(':blue[Over All Transaction Amount Distribution by Types]')
            fig1, ax1 = plt.subplots(figsize=(6,6))
            ax1.pie(result_data_amount['Transaction_amount'], labels=result_data_amount['Transaction_type'],autopct='%1.1f%%')
            st.pyplot(fig1)

        with col2:
            st.title('')
            st.subheader(':blue[State Wise Users Distribution by Brands]')
            fig1, ax1 = plt.subplots(figsize=(10, 6))  # Adjust the figsize as needed
            ax1.bar(result_state['brand'], result_state['Count'],color=custom_colors)
            ax1.set_xlabel('Brands')
            ax1.set_ylabel('Counts')
            ax1.ticklabel_format(style='plain', axis='y')  # Display y-axis labels as plain numbers
            plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
            st.pyplot(fig1)
            
            st.subheader(':blue[Over All Number of Transaction  Distribution by Types]')
            fig1, ax1 = plt.subplots(figsize=(6,6))
            ax1.pie(result_data_count['Transaction_count'], labels=result_data_count['Transaction_type'],autopct='%1.1f%%')
            st.pyplot(fig1)

        st.markdown("""---""")
        st.subheader(':blue[Number of Registered Users Distribution by State]')
        fig8, ax8 = plt.subplots(figsize=(18,8))  # Adjust the figsize as needed
        ax8.bar(result_reguser['State'],result_reguser['RegisteredUsers'],color=custom_colors)
        ax8.set_xlabel('State')
        ax8.set_ylabel('AppOpens')
        ax8.ticklabel_format(style='plain', axis='y')  # Display y-axis labels as plain numbers
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        st.pyplot(fig8)  

        st.markdown("""---""")
        st.subheader(':blue[Active Users Distribution by State]')
        fig1, ax1 = plt.subplots(figsize=(18,8))  # Adjust the figsize as needed
        ax1.bar(result_open['State'],result_open['AppOpens'],color=custom_colors)
        ax1.set_xlabel('State')
        ax1.set_ylabel('AppOpens')
        ax1.ticklabel_format(style='plain', axis='y')  # Display y-axis labels as plain numbers
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        st.pyplot(fig1) 

        st.markdown("""---""")
        st.subheader(':blue[Number of Registered Users Distribution by Districts]')
        fig2, ax2 = plt.subplots(figsize=(18,8))  # Adjust the figsize as needed
        ax2.bar(result_reguser_dis['Districts'],result_reguser_dis['RegisteredUsers'],color=custom_colors)
        ax2.set_xlabel('Districts')
        ax2.set_ylabel('RegisteredUsers')
        ax2.ticklabel_format(style='plain', axis='y')  # Display y-axis labels as plain numbers
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        st.pyplot(fig2)

        st.markdown("""---""")
        st.subheader(':blue[Active Users Distribution by Districts]')
        fig1, ax1 = plt.subplots(figsize=(18,8))  # Adjust the figsize as needed
        ax1.bar(result_open_dis['Districts'],result_open_dis['AppOpens'],color=custom_colors)
        ax1.set_xlabel('Districts')
        ax1.set_ylabel('AppOpens')
        ax1.ticklabel_format(style='plain', axis='y')  # Display y-axis labels as plain numbers
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        st.pyplot(fig1)
import streamlit as st

email = st.text_input('Enter your email: ')
password = st.text_input('Enter your password')
bus = st.button('Login')

if bus:
    if email == 'amangupta@gmail.com' and password =='12345':
        st.balloons()
        st.success('Logged In')

    else:
        st.error('Login Failed')
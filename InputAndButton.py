import streamlit as st

city_list = ['kolkata','mumbai','kochi','patna']

city = st.text_input("Type a City")
button = st.button('Click')

st.write(city,button)

if button == True:
    have_it = city.lower() in city_list
    if have_it:
        st.write("\nAvailable")
    else:
        st.write("\nCity Not Listed")
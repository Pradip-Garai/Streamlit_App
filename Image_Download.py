import streamlit as st


st.image("media_stocks/jaguar.jpg",caption="Jaguar Image")

file_name = st.text_input('Enter Image Name Before Download (with .jpg / .png / .jpeg)')

st.write(file_name)

with open('media_stocks/Jaguar.jpg',"rb") as file:
    btn = st.download_button(
        label="Download Image",
        data=file,
        file_name=file_name,
        mime='Jaugar/jpg'
    )
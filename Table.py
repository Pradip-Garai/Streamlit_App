import streamlit as st
import pandas as pd

table = ({"Name":["Pradip","Raj","Ankita"],
          "City":["Kolkata","Jaypur","Indore"]})

st.table(table)

st.dataframe(table)


# 
st.metric(label='Win Speed',value='70ms',delta='-5.3')
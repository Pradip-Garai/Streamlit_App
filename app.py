import streamlit as st

st.title("Hi!! I am Pradip Garai")
st.header("Hello Guys")
st.subheader("Hey Bro ")
st.text("I am Software Engineer at TCS, I want to join GOOGLE")

# markdown Heading
st.markdown('# Hello')
st.markdown('## Hello')
st.markdown('### Hello')


# Bold text
st.markdown("**Hello** I am Pradip")

# Italic 
st.markdown("*I am Pradip Garai*")

# code format
str = "print('Hello World !!!')"
st.code(str)

# Horizontal line 
st.markdown("---")

# Link
st.markdown('[GitHub](https://github.com/Pradip-Garai)')

# table 
table = '''
| Syntax | Description |
|--------- | ---------- |
|Header | Title |
|Paragraph | Text |
'''

st.markdown(table)



# Json Feature
json = {
  "Name":"Pradip Garai",
  "Age":20,
  "Designation":"System Engineer"
}

st.json(json)


# add imoge
st.markdown(':joy:')
st.markdown(':angry:')
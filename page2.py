import streamlit as st
import numpy as np

st.title("This is page 2")

# Get info from sidebar
st.title('Gettin info from the sidebar')
player=st.session_state['Players']
team=st.session_state['Teams']
st.write('The player is:', player)
st.write('The team is:', team)

# Column object notation
st.title("We are using columns")
col1, col2=st.columns(2)
col1.header('Tennis')
col1.image("https://www.mouratoglou.com/wp-content/uploads/2024/11/11dd1227-f3e1-4903-8755-cdbeeea0d97b-JUL01675-1534x1534-c-center.webp")
col2.header('Soccer')
col2.image("https://cdn.britannica.com/51/190751-050-147B93F7/soccer-ball-goal.jpg?w=600&q=60")

col3, col4=st.columns([0.7, 0.3])
col3.header('Tennis')
col3.image("https://www.mouratoglou.com/wp-content/uploads/2024/11/11dd1227-f3e1-4903-8755-cdbeeea0d97b-JUL01675-1534x1534-c-center.webp")
col4.header('Soccer')
col4.image("https://cdn.britannica.com/51/190751-050-147B93F7/soccer-ball-goal.jpg?w=600&q=60")

# Column with notation
st.title("More columns")
data=np.random.rand(20, 1)
colA, colB=st.columns([3, 1])   #the first column is three times the second one
with colA:
    st.header('Data viz')
    st.bar_chart(data)
with colB:
    st.header('Table')
    st.table(data)

# Tabs
st.title("Here we are using tabs")
tab1, tab2=st.tabs(['Football', 'Skiing'])
tab1.subheader("Football")
tab1.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/American_football.svg/768px-American_football.svg.png")
tab2.subheader("Skiing")
tab2.image("https://amc-p-001.sitecorecontenthub.cloud/api/public/content/5fcf04a21fd0499c9e57389b6c2d6cb4?v=6576abc8")

# Expanders
st.title("We are working with expanders")
with st.expander("Data viz", expanded=True):    #the expander is already open
    st.subheader('My data')
    st.line_chart(data)

with st.expander("Table", expanded=False):  #the expander is close
    st.subheader('My table')
    st.table(data)

# Secrets
st.title("Display some secrets")
username=st.secrets["username"]
st.write(username)

import os
password=os.environ["password"] #environmental variable
st.write(password)

secrets_psw=st.secrets.further_secrets.secret_password
st.write(secret_psw)
import streamlit as st
import pandas as pd
import numpy as np

# METRIC
st.title("Metric")

st.metric(label="Number of assists", value="25", delta="+6")

st.metric(label="Goals", value="13", delta="-5")

# DATAFRAME
st.title(":blue[Dataframe]")

data={
    "Player's name": ["Pelè", "Maradona", "Baggio"],
    "Goals": [13, 25, 24],
    "Team": ["Juve", "Napoli", "Inter"]
}

df1=pd.DataFrame(data)

st.subheader("Dataframe")
st.dataframe(df1)    #to display the dataframe

st.subheader("Static table")    #static means that you can't interact with the table
st.table(df1)

# CHARTS
# Data to create the charts
n_goals=np.random.randint(4, 21, size=(38, 3))
player_names=['Baggio', 'Fonseca', 'Maradona']
df2=pd.DataFrame(n_goals, columns=player_names)

# Line chart
st.title('Line chart')
st.line_chart(df2) #check out the documentation: https://docs.streamlit.io/develop/api-reference/charts/st.line_chart

# Area chart
st.title('Area chart')
st.area_chart(df2)

# Bar chart
st.title('Bar chart')
st.bar_chart(df2)

# New dataframe for the scatter chart
n_matches=38
x_coord=np.random.rand(n_matches)*100
y_coord=np.random.rand(n_matches)*100
goal_values=np.random.randint(0, 15, size=(n_matches))

goal_colors=np.random.rand(n_matches, 3)    #3 since we have 3 channels: red, green and blue
goal_colors_lot=[tuple(c) for c in goal_colors]  #facciamo questa cosa perchè altriment goal_colors non andrebbe bene, dato che non è monodimensionale, ma ha 3 colonne. Abbiamo fatto una lista di tuple

goal_data={
    "X": x_coord,
    "Y": y_coord,
    "Goals": goal_values,
    "Colors": goal_colors_lot
}

df3=pd.DataFrame(goal_data)

# Scatter chart
st.title('Scatter chart')
st.scatter_chart(df3, x="X", y="Y", size="Goals", color="Colors")

# MAP
n_pos=100
latitude=np.random.uniform(45.8, 45.9, n_pos)   #latitude of Lecco
longitude=np.random.uniform(9.35, 9.45, n_pos)   #longitude of Lecco
locations={
    "lat": latitude,
    "lon": longitude
}

df4=pd.DataFrame(locations)
st.map(df4)

# ESERCITAZIONE 10/04/2025
# Session state
st.title("Session state")
st.session_state['Player']="Diego"
st.session_state['Goals']=35

st.write("The name is:", st.session_state['Player'])    #used to save the data

# Error
st.error('This is an error message') #we could add also , icon=... to ad an icon

# Warning
st.warning('This is a warning message!')

# Success
st.success('This is a success message!')

# Info
st.info('This is an info message!')

# Progress bar
import time as t

st.title("Progress bar")
progress_bar=st.progress(0)
for i in range(101):
    t.sleep(0.05)   #to use this we need to import time
    progress_bar.progress(i)
st.success('Computation is complete')

# Spinner
st.title("Here we have a spinner")
with st.spinner('You have to wait!', show_time=True):    #we use with to define a block of code that is safe
    t.sleep(5)  #we are waiting for 5 seconds
st.success('Task is complete')

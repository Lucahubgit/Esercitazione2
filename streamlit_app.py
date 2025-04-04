import streamlit as st
import pandas as pd

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

df=pd.DataFrame(data)

st.subheader("Dataframe")
st.dataframe(df)    #to display the dataframe

st.subheader("Static table")    #static means that you can't interact with the table
st.table(df)
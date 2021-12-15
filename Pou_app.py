import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('POU app')

DATA_URL = ('project data.csv')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)

    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

@st.cache
def load_data(nrows):
    data_load_state.text("Done! (using st.cache)")
st.subheader('Raw data')
st.write(data)

fig, ax = plt.subplots()

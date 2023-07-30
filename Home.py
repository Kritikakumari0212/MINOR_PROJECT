import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go

st.title('Energy Consumption Analysis')
st.image("energy.jpg")

@st.cache_data
def load_data():
    df = pd.read_csv('datasets/energy_dataset.csv')
    return df

with st.spinner('Loading Data ...'):
    df = load_data()

if st.checkbox("Show Dataset"):
    st.subheader("Dataset")
    st.write(df)


import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


st.title("KMeans Clustering App")
st.subheader("Data Science With Poresh")

#Sidebar

st.sidebar.header("Upload CSV Data or Use Sample")
use_example = st.sidebar.checkbox("Use Example Dataset")

#Load Data

if use_example:
  df = sns.load_dataset('IRIS')
  df = df.dropna()
  st.success("Loaded sample dataset:'IRIS'")
else:
  uploaded_file = st.sidebar.file_uploader("Upload Your CSV File", type = ['csv'])
  if uploaded_file:
    df = pd.read_csv(uploaded_file)
  else:
    st.warning("Please upload your csv file or use the sample dataset")
    st.stop()

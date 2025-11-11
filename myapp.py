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
  df = sns.load_dataset('iris')
  df = df.dropna()
  st.success("Loaded sample dataset:'IRIS'")
else:
  uploaded_file = st.sidebar.file_uploader("Upload Your CSV File", type = ['csv'])
  if uploaded_file:
    df = pd.read_csv(uploaded_file)
  else:
    st.warning("Please upload your csv file or use the sample dataset")
    st.stop()



#Show Dataset

st.subheader("Dataset Preview")
st.write(df.head())

st.subheader("Data Preprocessing")
numeric_cols = df.select_dtypes(include = np.number).columns.tolist()

if len(numeric_cols) < 2:
  st.error("Need atleast two numeric columns for clustering")
  st.stop()

features = st.multiselect("Select feature columns for clustering", numeric_cols, default=numeric_cols)

if len(features) == 0:
  st.write("Please select atleast one feature")
  st.stop()

import streamlit as st
import pickle
import pandas as pd
import numpy as np
import gdown
import os



st.set_page_config(page_title="Price Prediction")

# Function to download the pipeline file from Google Drive
@st.cache_resource  # Cache the file to avoid re-downloading
def download_pipeline():
    # Use the correct Google Drive download URL format
    url = "https://drive.google.com/uc?id=1ZAbJWCt5sfC4srJlRhykQOtviCZVJv_m"
    output = "pipeline.pkl"
    if not os.path.exists(output):
        gdown.download(url, output, quiet=False)
    return output

# Download and load the pipeline
pipeline_file = download_pipeline()
with open(pipeline_file, 'rb') as file:
    pipeline = pickle.load(file)

with open('datasets/df.pkl','rb') as file:
    df = pickle.load(file)



st.header('Enter your inputs')

# property_type
property_type = st.selectbox('Property Type',['flat','house'])

# sector
sector = st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

bedrooms = float(st.selectbox('Number of Bedroom',sorted(df['bedRoom'].unique().tolist())))

bathroom = float(st.selectbox('Number of Bathrooms',sorted(df['bathroom'].unique().tolist())))

balcony = st.selectbox('Balconies',sorted(df['balcony'].unique().tolist()))

property_age = st.selectbox('Property Age',sorted(df['agePossession'].unique().tolist()))

built_up_area = float(st.number_input('Built Up Area'))

servant_room = float(st.selectbox('Servant Room',[0.0, 1.0]))
store_room = float(st.selectbox('Store Room',[0.0, 1.0]))

furnishing_type = st.selectbox('Furnishing Type',sorted(df['furnishing_type'].unique().tolist()))
luxury_category = st.selectbox('Luxury Category',sorted(df['luxury_category'].unique().tolist()))
floor_category = st.selectbox('Floor Category',sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):

    # form a dataframe
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    #st.dataframe(one_df)

    # predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    # display
    st.text(f"The price of the flat is between {round(low,2)} Cr and {round(high,2)} Cr.")
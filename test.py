import streamlit as st
import pandas as pd

## Créer un DataFrame d'échantillon avec des valeurs de latitude et de longitude
data = pd.DataFrame({
    'latitude': [47.25],
    'longitude': [6.03333 ]
})

## Créer une carte avec les données
st.title("Cordonnées GPS de la photo au dessus ")
latitude = data['latitude'].iloc[0]
longitude = data['longitude'].iloc[0]
st.write(f"Latitude: {latitude}")
st.write(f"Longitude: {longitude}")
st.map(data,zoom = 5)

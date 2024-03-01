import requests
import streamlit as st

api_key = st.secrets.GIPHY.api_key_2

url = 'https://api.giphy.com/v1/gifs/random'

gif = st.text_input('Please, select a random giphy', 'dog')

params = {'api_key':api_key, 'tag':gif}

response = requests.get(url, params=params).json()

giphy_url = response['data']['embed_url']

st.write(f"<iframe src={giphy_url}>", unsafe_allow_html=True)

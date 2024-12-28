import streamlit as st
import requests

# Prepare Api key and API Url
api_key = "D0uidDFXjuIaF3nXbH8eBeS94F4sok22R4xmL4id"
api_key = "BK4Vfn6bfRxIgedDzAhrOSOiifspMHtu9iOz9YWS"  //28thdec2024
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

# Get the request data as  dictionary
response1 = requests.get(url)
data = response1.json()

# Extract the Image title,url and Explanation
title = data["title"]
image_url = data['url']
explanation = data['explanation']

# Download the Image
image_filepath = 'image.png'
response2 = requests.get(image_url)
with open (image_filepath, 'wb') as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)



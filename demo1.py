import streamlit as st

with st.sidebar:
  st.text('Dog in sidebar')
  st.image('https://static.streamlit.io/examples/dog.jpg')

col1, col2 = st.columns(2)

with col1:
  st.header("Main Window")
  st.text('Animals')
  st.image("https://i.imgur.com/L3o3B9y.jpg")

with col2:
  st.text("Relax video")
  st.video("https://www.youtube.com/watch?v=M8C-oEs0uT0")
from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
### News & Twitter search tool

"""

options = ['News','Tweets']
selected_option = st.selectbox('Select a data source', options)
           
language = ['English','Dutch']
selected_language = st.selectbox('Select the language', language)

# Create a text box for user input
daterange_input = st.text_input("Enter the keywords here")

# Create a text box for user input
datefrequency_input = st.text_input("Enter the keywords here")

# Create a text box for user input
keywords_input = st.text_input("Enter the keywords here")

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
selected_language = st.multiselect('Select the language', language)

location = ['USA','UK']
selected_language = st.multiselect('Select the location', location)

# Create a text box for user input
daterange_input = st.text_input("Enter the keywords here")

output_type = ['csv','excel']
selected_option = st.selectbox('Select a file format', output_type)


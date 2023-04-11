from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import datetime

"""
### News & Twitter search tool

"""

options = ['News','Tweets']
selected_option = st.selectbox('Select a data source', options)

date_start = st.date_input("Enter a start date")
date_end = st.date_input("Enter an end date")
           
language = ['English','Dutch']
selected_language = st.multiselect('Select the language', language)

location = ['USA','UK']
selected_language = st.multiselect('Select the location', location)

# Create a text box for user input
keyword_input = st.text_input("Enter the keywords here")

# Create a text box for user input
domains_input = st.text_input("Enter specific domain(s) here. If more than one separate by ',' ")

output_type = ['csv','excel']
selected_option = st.selectbox('Select a file format', output_type)

final_button=st.button('request query')

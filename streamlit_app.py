from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import datetime
import subprocess
#import nbconvert

"""
### News & Twitter search tool

"""

options = ['News','Tweets']
data_source = st.selectbox('Select a data source', options)

date_start = st.date_input("Enter a start date")
date_end = st.date_input("Enter an end date")

date_frequency= ['yearly','monthly','daily']
selected_date_frequency = st.selectbox('Select date frequency', date_frequency)
           
language = ['English','Dutch']
selected_language = st.multiselect('Select the language', language)

location = ['USA','UK']
selected_location = st.multiselect('Select the location', location)

# Create a text box for user input
keyword_input = st.text_input("Enter the keywords here")

# Create a text box for user input
domains_input = st.text_input("Enter specific domain(s) here. Separate with ';' ")

# Words to include or exclude
include = st.text_input("Enter words to include in your query. Separate with ';'")
exclude = st.text_input("Enter words to exclude from your query. Separate with ';'")
# We can use a radio button to make the textbox include or exclude but a separate box could be better because the user
# might want both functionalities.
# include or exclude Radio
# choice = st.radio('Choose One', ('Include', 'Exclude'))

# output
output_type = ['csv','excel']
selected_option = st.selectbox('Select a file format', output_type)

final_button=st.button('request query')

notebook_path='00_SERP.ipynb'
# Create a function that runs the notebook when the button is clicked
def run_notebook(notebook_path):
    subprocess.run(['jupyter', 'nbconvert', '--execute', notebook_path])

# Create a Streamlit button that runs the function when clicked
if final_button:
    run_notebook('00_SERP.ipynb')

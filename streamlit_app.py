from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

# Create a text box for user input
user_input = st.text_input("Enter text here")

# Display the user input
st.write("You entered:", user_input)

def main():
    st.title("Suspended List")
    suspended_items = ["Item 1", "Item 2", "Item 3", "Item 4"]
    container = st.beta_container()
    with container:
        for item in suspended_items:
            checked = st.checkbox(item)
            if checked:
                suspended_items.remove(item)

if __name__ == "__main__":
    main()

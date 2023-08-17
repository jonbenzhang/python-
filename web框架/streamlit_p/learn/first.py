import streamlit as st
import pandas as pd
import numpy as np

text_input = st.text_area(
    "Enter some text 👇",
)

if text_input:
    st.write("You entered: ", text_input)

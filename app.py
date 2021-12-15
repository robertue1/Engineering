import streamlit as st
import os

import matplotlib.pyplot as plt
import pandas as pd

from multiapp import MultiApp
from apps import main



#PART 1

st.write('''
# Understanding the Venezuelan Crisis
## Analysis of 20 years of news articles. 
''')

st.markdown(
    """
 <style>
.stApp {
  background-image: url("https://images.unsplash.com/photo-1621622633934-b910be06148d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=3538&q=80,%s");
  background-size: cover;
}
</style>
    """,
    unsafe_allow_html=True
)

link = "[Let's begin the journey](http://github.com)"
st.markdown(link, unsafe_allow_html=True)


# Add all your application here
app.add_app("Main", main.app)

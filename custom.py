import streamlit as st
import pandas as pd
from database import custom_query

def query():
    lst = st.text_input("Enter comma seperated list of Column Names :").split(",")
    q = st.text_input("Enter the sql quer :")
    result = custom_query(q)
    df = pd.DataFrame(result,columns = lst)
    with st.expander("Query output : "):
        st.dataframe(df)
import streamlit as st
import pandas as pd
from database import agg_j

def read_op():
    result = agg_j()
    # st.write(result)
    df = pd.DataFrame(result, columns=['count(srns)','hostel_id'])
    with st.expander("The output : "):
        st.dataframe(df)
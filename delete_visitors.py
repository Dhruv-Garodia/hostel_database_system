import pandas as pd
import streamlit as st
from database import delete_visitors_data

def delete_visitors(ids):
    selected_id = st.selectbox("Choose the visitors id :",ids)
    st.warning("Do you want to delete ::{}".format(selected_id))
    if st.button("Delete visitor detail"):
        delete_visitors_data(selected_id)
        st.success("Visitor has been deleted successfully")
        st.write("In delete")
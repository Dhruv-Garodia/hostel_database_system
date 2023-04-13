import pandas as pd
import streamlit as st
from database import update_cloak_data

def update_cloak(srns):
    selected_id = st.selectbox("Choose the srn :",srns)
    st.warning("Do you want to delete ::{}".format(selected_id))
    duration = st.slider("Enter the number of months :",1,6)

    if st.button("Update room detials"):
        update_cloak_data(duration,selected_id)
        st.success("Updated details for room number : {}".format(selected_id))
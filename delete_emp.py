import pandas as pd
import streamlit as st
from database import delete_employee_data

def delete_emp(ids):
    selected_id = st.selectbox("Choose the employee id :",ids)
    st.warning("Do you want to delete ::{}".format(selected_id))
    if st.button("Delete employee detail"):
        delete_employee_data(selected_id)
        st.success("Hostel has been deleted successfully")
import pandas as pd
import streamlit as st
from database import delete_hostel_data

def delete_hostel(selected_id):
    if st.button("Delete hostel detail"):
        delete_hostel_data(selected_id)
        st.success("Hostel has been deleted successfully")
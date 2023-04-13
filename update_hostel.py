import pandas as pd
import streamlit as st
from database import update_hostel_data

def update_hostel(selected_id):
    col1, col2 = st.columns(2)
    with col1:
        hostel_name = st.text_input("Enter your Block name :")
        manager_name = st.text_input("Enter the hostel block managers name :")
        
    with col2:
        no_of_rooms = st.number_input("Enter the number of rooms in the block :")
        no_of_students = st.number_input("Enter the students occupancy :")

    if st.button("Update hostel detail"):
        update_hostel_data(hostel_name,manager_name,no_of_rooms,no_of_students,selected_id)
        st.success("Hostel has been updated successfully")